from rest_framework import renderers
import json

class UserRenderer(renderers.JSONRenderer):
    charset = 'utf-8'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        response = ''
        if 'ErrorDetail' in str(data):
            response = json.dumps({'errors': self._flatten_errors(data)})
        else:
            response = json.dumps(data)
        return response

    def _flatten_errors(self, data):
        error_messages = []
        for value in data.values():
            if isinstance(value, list) and len(value) > 0:
                error_messages.extend(value)
        return error_messages
