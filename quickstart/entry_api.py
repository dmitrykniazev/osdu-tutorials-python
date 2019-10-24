import falcon

from auth.api import LoginResource, AuthResource
from search.api import SearchResource

api = falcon.API()

# Auth endpoints
api.add_route('/', LoginResource())
api.add_route('/auth/callback', AuthResource())

# Search endpoint
api.add_route('/search', SearchResource())
