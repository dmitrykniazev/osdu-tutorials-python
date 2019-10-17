import falcon
from oic import rndstr

from oic.oic import Client
from oic.oic.message import ProviderConfigurationResponse
from oic.utils.authn.client import CLIENT_AUTHN_METHOD

#  get TenantID, ClientID and ClientSecret from Azure portal during app registration
from quickstart.auth.app import IndexResource

client = Client(client_authn_method=CLIENT_AUTHN_METHOD)
client.client_id = "your_client_id"
client.client_secret = "your_client_secret"

# It is also possible to discover provider info by provider URL using client.provider_config("providerURL")
# Provider info can be configured accordingly (prefer):
provider_info = ProviderConfigurationResponse(
    registration_endpoint="provider_registration_endpoint",
    authorization_endpoint="authorization_endpoint",
    scopes_supported=["openid", "profile", "email"],
)

# Now the provider_info contains all necessary information about provider includes scopes
client.provider_info = provider_info

args = {
    "redirect_uris": "http://localhost:8080/auth/callback",
}
registration_response = client.register(provider_info["registration_endpoint"], **args)

# The response will also be stored in the client instance (registration_response attribute)
# and some of the parameters will be unpacked and set as attributes on the client instance.

session = {
    "state": rndstr(),
    "nonce": rndstr()
}

# saving session data for later usage
client.registration_response["session"] = session

# Falcon application configuration
app = falcon.API()
app.add_route('/', IndexResource(client=client))
app.add_route('/auth/callback', IndexResource(client=client))
