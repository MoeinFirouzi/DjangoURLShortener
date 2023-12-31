from rest_framework.generics import CreateAPIView, RetrieveAPIView
from url_shortener.api.v1.serializers import URLSerializer
from django.shortcuts import get_list_or_404
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from url_shortener.models import Url


class ShortenerAPIView(CreateAPIView):
    """
    ShortenerAPIView accepts post request and converts the given url in
    the body to a shorter url, then saves both of them in database.
    Then returns original_url and short_url in the response.
    """

    serializer_class = URLSerializer
    queryset = Url.objects.all()


class RetrieveURLAPIView(RetrieveAPIView):
    """
    API view to retrieve a URL object based on the provided
    short URL slug.
    """

    serializer_class = URLSerializer

    def get_object(self):
        """
        Retrieves the URL object based on the provided short URL slug.
        """
        try:
            slug = self.kwargs["url"]
            obj = get_list_or_404(Url, short_url=slug)
            return obj[-1]
        except Exception:
            raise NotFound({"error": "URL not found."})

    def retrieve(self, request, *args, **kwargs):
        """
        Increases the times_followed counter on each retrieve.
        """
        instance = self.get_object()
        instance.times_followed = instance.times_followed + 1
        instance.save()

        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    @method_decorator(cache_page(60 * 60))
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
