import falcon

class OfferSDP:
    def __init__(self):
        self._sdp = b'corsempty'

    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.data = self._sdp
        resp.content_type = 'application/json;charset=UTF-8' #'application/sdp'
        resp.status = falcon.HTTP_200

    def on_post(self, req, resp):
        """Handles POST requests"""
        self._sdp = req.stream.read()
        print('Received SDP:')
        print(self._sdp)
        resp.status = falcon.HTTP_201

api = falcon.App(cors_enable=True)
api.add_route('/offer', OfferSDP())
api.add_route('/answer', OfferSDP())
