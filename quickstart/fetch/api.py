import logging
from dataclasses import dataclass
from typing import Any, Dict, Optional

import requests
from azure.storage.blob.baseblobservice import BaseBlobService
from falcon import Request, Response, HTTP_BAD_REQUEST

from settings import OSDU_API_BASE_URL

logger = logging.getLogger(__name__)


@dataclass
class AzureBlobAccessData:
    domain: str
    container_name: str
    blob_name: str
    sas: str
    account_name: str = 'Anonymous'


class FetchResource:

    def get_file_url(self, data: Dict[str, Any]) -> Optional[AzureBlobAccessData]:

        try:
            result_data: Dict = data['Result'][0]['FileLocation']
            endpoint = result_data['EndPoint']
            bucket = result_data['Bucket']
            key = result_data['Key']
            sas = result_data['TemporaryCredentials']['SAS']
        except (IndexError, KeyError):
            return None

        return AzureBlobAccessData(
            domain=endpoint,
            container_name=bucket,
            blob_name=key,
            sas=sas
        )

    def get_blob_data(self, data: AzureBlobAccessData) -> str:
        service = BaseBlobService(account_name=data.account_name, sas_token=data.sas, custom_domain=data.domain)
        data = service.get_blob_to_text(data.container_name, data.blob_name)
        return data.content

    def on_get(self, request: Request, response: Response) -> None:
        srn = request.params.get('srn')
        if srn is None:
            response.status = HTTP_BAD_REQUEST
            return

        fetch_request_body = {
            'SRNS': [srn],
            'TargetRegionId': '',
        }

        fetch_result = requests.post('%s/GetResources' % OSDU_API_BASE_URL, json=fetch_request_body)

        data = self.get_file_url(fetch_result.json())
        if data is None:
            response.status = HTTP_BAD_REQUEST
            return

        response.media = self.get_blob_data(data)
