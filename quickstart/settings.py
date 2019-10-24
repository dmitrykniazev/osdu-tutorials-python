import os

AUTH_BASE_URL = os.environ.get('AUTH_BASE_URL', 'https://<base-endpoint>')
CLIENT_ID = os.environ.get('AUTH_CLIENT_ID', 'your_client_id')
CLIENT_SECRET = os.environ.get('AUTH_CLIENT_SECRET', 'your_client_secret')
OSDU_API_BASE_URL = os.environ.get('OSDU_API_BASE_URL', 'osdu_base_endpoint')

