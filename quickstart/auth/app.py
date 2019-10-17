import falcon
from oic.oic import AuthorizationResponse


class IndexResource:
    client = None

    def __init__(self, **kwargs):
        self.client = kwargs.get('client', None)  # todo validation

    def on_post(self, req, resp):
        '''
        This handler initiates the sign-in process by redirecting to the provider authorization endpoint
        '''
        args = {
            "client_id": self.client.client_id,
            "response_type": "code",
            "scope": ["openid"],
            "nonce": self.client.registration_response["session"]["nonce"],
            "redirect_uri": self.client.registration_response["redirect_uris"][0],
            "state": self.client.registration_response["session"]["state"]
        }

        auth_req = self.client.construct_AuthorizationRequest(request_args=args)
        login_url = auth_req.request(self.client.authorization_endpoint)

        return falcon.HTTPMovedPermanently(login_url)


class AuthResource:
    client = None

    def __init__(self, **kwargs):
        self.client = kwargs.get('client', None)  # todo validation

    def on_post(self, req, resp):
        '''
            This handler validates the state, so it hasn't changed during the communication
        '''

        aresp = self.client.parse_response(AuthorizationResponse, info=resp, sformat="urlencoded")
        assert aresp["state"] == self.client.registration_response["session"]["state"]

        args = {
            "code": aresp["code"]
        }

        return self.client.do_access_token_request(state=aresp["state"],
                                                   request_args=args,
                                                   authn_method="client_secret_basic")
