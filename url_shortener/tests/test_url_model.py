from django.test import TestCase
from url_shortener.models import Url


class TestModel(TestCase):
    def test_create_url_obj_success(self):
        """
        Tests the successful creation of a Url object.
        """
        url_obj = Url.objects.create(original_url="testurl.com",
                                     short_url="shorurl")

        self.assertEqual(url_obj.original_url, "testurl.com")
        self.assertEqual(url_obj.short_url, "shorurl")
        self.assertEqual(url_obj.times_followed, 0)
        self.assertIsNotNone(url_obj.creation_date)
