import json

from rest_framework.renderers import JSONRenderer
from core.renderers import HackthonJSONRenderer


class UserJSONRenderer(HackthonJSONRenderer):
    object_label = 'user'

    def render(self, data, media_type=None, renderer_context=None):
        
        token = data.get('token', None)

        if token is not None and isinstance(token, bytes):
            # Also as mentioned above, we will decode `token` if it is of type
            # bytes.
            data['token'] = token.decode('utf-8')

        return super(UserJSONRenderer, self).render(data)