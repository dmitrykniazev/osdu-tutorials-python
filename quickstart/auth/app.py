from logging import getLogger

from falcon import Request, Response, HTTPMovedPermanently
from oic.oic import AuthorizationResponse

from auth.client import client, session, redirect_url

logger = getLogger(__name__)


class LoginResource:

    def on_get(self, request: Request, response: Response) -> None:
        """
        This handler initiates the sign-in process by redirecting to the provider authorization endpoint
        """
        args = {
            'client_id': client.client_id,
            'response_type': 'code',
            'scope': ['openid', 'email'],
            'state': session['state'],
            'redirect_uri': redirect_url,
        }

        auth_request = client.construct_AuthorizationRequest(request_args=args)
        login_url = auth_request.request(client.authorization_endpoint)

        raise HTTPMovedPermanently(login_url)


class AuthResource:

    def on_get(self, request: Request, response: Response) -> None:
        """
        This handler validates the state, so it hasn't changed during the communication
        """

        auth_response = client.parse_response(AuthorizationResponse, info=request.query_string, sformat='urlencoded')
        assert auth_response['state'] == session['state']

        args = {
            'code': auth_response['code'],
        }
        client.do_access_token_request(
            state=auth_response['state'],
            request_args=args
        )
        user_info_response = client.do_user_info_request(state=auth_response['state'])
        response.media = str(user_info_response)
