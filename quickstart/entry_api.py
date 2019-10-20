import falcon

from auth.app import LoginResource, AuthResource


class PingResource:
    def on_get(self, request: falcon.Request, response: falcon.Response) -> None:
        response.media = {'result': 'pong'}


api = falcon.API()

# Test endpoint
api.add_route('/ping', PingResource())

# Auth endpoints
api.add_route('/', LoginResource())
api.add_route('/auth/callback', AuthResource())
