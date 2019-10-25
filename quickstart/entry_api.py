import falcon

from auth.api import LoginResource, AuthResource
from search.api import FindResource
from fetch.api import FetchResource

api = falcon.API()

# Auth endpoints
api.add_route('/', LoginResource())
api.add_route('/auth/callback', AuthResource())

# Search endpoint
api.add_route('/find', FindResource())

# Fetch endpoint
api.add_route('/fetch', FetchResource())
