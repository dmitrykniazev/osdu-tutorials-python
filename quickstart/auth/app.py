# stub for python implementation
import falcon


class IndexResource:
    def on_get(self, req, resp):
        """Handles GET requests"""
        quote = {"its the index handler"}

        resp.media = quote


class AuthResource:
    def on_get(self, req, resp):
        """Handles GET requests"""
        quote = {
            'quote': (
                "I've always been more interested in "
                "the future than in the past."
            ),
            'author': 'Grace Hopper'
        }

        resp.media = quote


api = falcon.API()
api.add_route('/', IndexResource())
api.add_route('/auth/callback', IndexResource())
