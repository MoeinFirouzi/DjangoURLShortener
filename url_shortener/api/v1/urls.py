from django.urls import path
from url_shortener.api.v1.views import ShortenerAPIView

app_name = "v-1"

urlpatterns = [
    path("", ShortenerAPIView.as_view(), name="url-create"),
]
