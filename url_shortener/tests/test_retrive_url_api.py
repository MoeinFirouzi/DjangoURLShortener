from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

from url_shortener.utils import URLShortener
from url_shortener.models import Url


class TestURLAPI(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.shortener = URLShortener()

    def test_get_original_url_success_200(self):
        """
        Tests the successful retrieval of an original URL from a short URL.
        """
        original_url = "https://test.com/"
        short_url = self.shortener.encode_md5(original_url)

        url_obj = Url.objects.create(original_url=original_url,
                                     short_url=short_url)

        res = self.client.get(f"http://127.0.0.1:8000/{short_url}/")

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data["original_url"], url_obj.original_url)
        self.assertEqual(
            res.data["short_url"], f"http://127.0.0.1:8000/{url_obj.short_url}"
        )

    def test_get_original_url_not_fount_404(self):
        """
        Tests retrieval of an original URL from a non-existent short URL.
        """
        original_url = "https://test.com/"
        short_url = self.shortener.encode_md5(original_url)
        res = self.client.get(f"http://127.0.0.1:8000/{short_url}/")

        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(res.data["error"], "URL not found.")
