from rest_framework.generics import CreateAPIView
from url_shortener.api.v1.serializers import URLSerializer

from url_shortener.models import Url


class ShortenerAPIView(CreateAPIView):
    """
    ShortenerAPIView accepts post request and converts the given url in
    the body to a shorter url, then saves both of them in database.
    Then returns original_url and short_url in the response.
    """

    serializer_class = URLSerializer
    queryset = Url.objects.all()
