from oic.oic import Client
from oic.utils.authn.client import CLIENT_AUTHN_METHOD

#  get TenantID, ClientID and ClientSecret from Azure portal during app registration
client = Client(client_authn_method=CLIENT_AUTHN_METHOD)
client.client_id = "yourClientID"
client.client_secret = "yourClientSecret"

issuer = "yourCloudProviderURL"
provider_info = None

try:
    provider_info = client.provider_config(issuer)
except Exception as e:
    print(e)

# Now the provider_info contains all necessary information about provider includes scopes
# The provider info is also automatically stored in the client instance

# Prepare args for User sign-in
args = {
    "redirect_uris": ['http://localhost:8080/auth/callback'],
    "contacts": ["contants@example.com"]
}
