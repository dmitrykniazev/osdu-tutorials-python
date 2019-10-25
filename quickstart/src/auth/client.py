
from oic.oic import Client
from oic.oic.message import RegistrationResponse
from oic.utils.authn.client import CLIENT_AUTHN_METHOD

from settings import AUTH_BASE_URL, CLIENT_ID, CLIENT_SECRET

redirect_url = 'http://localhost:8080/auth/callback'

# get TenantID, ClientID and ClientSecret 
# from Azure portal during app registration

client = Client(client_authn_method=CLIENT_AUTHN_METHOD, verify_ssl=False)
client.provider_config(issuer=AUTH_BASE_URL)

# Store the registration credits in clients
registration_info = RegistrationResponse(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
)
client.store_registration_info(registration_info)
client.redirect_uris = [redirect_url]

session = {
    'state': 'foobar'
}
