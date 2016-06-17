import json

import redis

from django.test import TestCase, override_settings
from django.conf import settings
from rest_framework import status
from rest_framework.test import APIRequestFactory

from .views import policy_list

# Tests use database=10 instead of 0.
@override_settings(REDIS_CON_POOL = redis.ConnectionPool(host='localhost', port=6379, db=10))
class RegistryTestCase(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        # Using rest_framework's APIRequestFactory: http://www.django-rest-framework.org/api-guide/testing/
        self.factory = APIRequestFactory()

    def tearDown(self):
        r = redis.Redis(connection_pool=settings.REDIS_CON_POOL)
        r.flushdb()

    def test_registry_static_policy(self):
        """..."""

        # Create an instance of a GET request.
        request = self.factory.get('/registry/static_policy')
        response = policy_list(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
