import simplejson as json

from rest_framework.renderers import JSONRenderer
from rest_framework import status
from rest_framework_swagger.renderers import OpenAPIRenderer, OpenAPICodec

from .utils import append_schemas


class CustomOpenAPIRenderer(OpenAPIRenderer):

    def render(self, data, accepted_media_type=None, renderer_context=None):
        if renderer_context['response'].status_code != status.HTTP_200_OK:
            return JSONRenderer().render(data)
        extra = self.get_customizations()
        swagger_doc = json.loads(OpenAPICodec().encode(data, extra=extra))
        result = append_schemas(swagger_doc)  # Append more information to documentation
        return result
