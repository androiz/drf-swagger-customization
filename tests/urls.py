# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import

from django.conf.urls import url, include

from drf_swagger_customization.urls import urlpatterns as drf_swagger_customization_urls

urlpatterns = [
    url(r'^', include(drf_swagger_customization_urls, namespace='drf_swagger_customization')),
]
