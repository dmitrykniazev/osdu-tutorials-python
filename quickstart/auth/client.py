import os

from oic.oic import Client
from oic.oic.message import ProviderConfigurationResponse, RegistrationResponse
from oic.utils.authn.client import CLIENT_AUTHN_METHOD

redirect_url = 'http://localhost:8080/auth/callback'

#  get TenantID, ClientID and ClientSecret from Azure portal during app registration
meta_endpoint = os.environ.get('AUTH_META_ENDPOINT', 'https://<meta-endpoint>')
authorization_endpoint = os.environ.get('AUTH_ENDPOINT', 'https://<authorization-server-url>')
token_endpoint = os.environ.get('AUTH_TOKEN_ENDPOINT', 'https://<authorization-token-server-url>')
client_id = os.environ.get('AUTH_CLIENT_ID', 'your_client_id')
client_secret = os.environ.get('AUTH_CLIENT_SECRET', 'your_client_secret')

client = Client(client_authn_method=CLIENT_AUTHN_METHOD, verify_ssl=False)
client.provider_config(issuer=meta_endpoint)

# It is also possible to discover provider info by provider URL using client.provider_config('providerURL')
# Provider info can be configured accordingly (prefer):
provider_info = ProviderConfigurationResponse(
    authorization_endpoint=authorization_endpoint,
    token_endpoint=token_endpoint,
    scopes_supported=['openid', 'email', 'profile'],
)

# Now the provider_info contains all necessary information about provider includes scopes
client.provider_info = provider_info

# Store the registration credits in clients
registration_info = RegistrationResponse(
    client_id=client_id,
    client_secret=client_secret,
)
client.store_registration_info(registration_info)
client.redirect_uris = [redirect_url]

session = {
    'state': 'foobar'
}

