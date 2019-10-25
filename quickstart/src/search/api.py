from typing import Dict, Any, List

import requests
from falcon import Request, Response

from settings import API_BASE_URL


class SearchResource:

    def get_response_from_search_result(self, search_result: List[Dict]) -> Dict[str, Any]:
        result = {}
        for entry in search_result:
            resource_type = result.setdefault(entry['resource_type'], [])
            for file_data in entry.get('files', []):
                resource_type.append({
                    'srn': file_data['srn'],
                    'filename': file_data['filename']
                })

        return result

    def on_get(self, request: Request, response: Response) -> None:
        well_name = request.params.get('wellname')
        search_request_data = {
            'fulltext': well_name,
            'metadata': {
                'resource_type': [
                    'master-data/Well',
                    'work-product-component/WellLog',
                    'work-product-component/WellborePath'
                ]
            },
            'facets': [
                'resource_type'
            ]
        }

        search_result = requests.request('post', '%s/indexSearch' % API_BASE_URL, json=search_request_data)
        response.media = self.get_response_from_search_result(search_result.json().get('results', []))
