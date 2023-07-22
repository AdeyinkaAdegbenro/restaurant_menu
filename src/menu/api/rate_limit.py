from django.core.cache import caches
from rest_framework import throttling


class CustomRateThrottling(throttling.BaseThrottle):
    cache = caches['default']

    def allow_request(self, request, view):
        return True