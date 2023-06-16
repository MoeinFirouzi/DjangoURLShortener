from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework import status

SHORTENER_URL = reverse("url-shortener:v-1:url-create")


class TestURLAPI(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()

    def test_api_url_create_success_201(self):
        """
        Tests the successful creation of a Url object by API.
        """
        payload = {"original_url": "https://www.testurl.com"}
        res = self.client.post(SHORTENER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertIsNotNone(res.data.get("short_url"))

    def test_api_url_create_faild_400(self):
        """
        This function tests the API URL creation with a failed
        400 response. It sends an empty payload to the url-create
        endpoint and checks if the response status code is equal to 400.
        """
        payload = {}
        res = self.client.post(SHORTENER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
