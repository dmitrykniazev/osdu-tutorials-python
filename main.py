from oic.oic import Client
from oic.oic.message import ProviderConfigurationResponse
from oic.utils.authn.client import CLIENT_AUTHN_METHOD

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
