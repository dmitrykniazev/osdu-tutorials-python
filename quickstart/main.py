from oic import rndstr
from oic.oic import Client
from oic.oic.message import ProviderConfigurationResponse, AuthorizationResponse
from oic.utils.authn.client import CLIENT_AUTHN_METHOD
from oic.utils.http_util import Redirect

#  get TenantID, ClientID and ClientSecret from Azure portal during app registration
client = Client(client_authn_method=CLIENT_AUTHN_METHOD)
client.client_id = "yourClientID"
client.client_secret = "yourClientSecret"

# It is also possible to discover provider info by provider URL using client.provider_config("providerURL")
# Provider info can be configured accordingly (prefer):
provider_info = ProviderConfigurationResponse(
    issuer="yourCloudProviderURL",
    authorization_endpoint="providerEndpoint",
    redirect_uris=["http://localhost:8080/auth/callback"],
    scopes_supported=["profile", "email"],
)

# Now the provider_info contains all necessary information about provider includes scopes
client.provider_info = provider_info

registration_response = client.register(provider_info["registration_endpoint"])

# The response will also be stored in the client instance (registration_response attribute)
# and some of the parameters will be unpacked and set as attributes on the client instance.

session = {
    "state": rndstr(),
    "nonce": rndstr()
}


def sign_in():
    '''
        This handler initiates the sign-in process by redirecting to the provider authorization endpoint
    '''

    args = {
        "client_id": client.client_id,
        "response_type": "code",
        "scope": ["openid"],
        "nonce": session["nonce"],
        "redirect_uri": client.registration_response["redirect_uris"][0],
        "state": session["state"]
    }

    auth_req = client.construct_AuthorizationRequest(request_args=args)
    login_url = auth_req.request(client.authorization_endpoint)

    return Redirect(login_url)


# Suppose, response - is a response_object
response = "response_object"

#  this handler validates the state, so it hasn't changed during the communication
aresp = client.parse_response(AuthorizationResponse, info=response, sformat="urlencoded")
code = aresp["code"]
assert aresp["state"] == session["state"]

args = {
    "code": aresp["code"]
}

resp = client.do_access_token_request(state=aresp["state"],
                                      request_args=args,
                                      authn_method="client_secret_basic")