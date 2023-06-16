from django.urls import path
from url_shortener.api.v1.views import ShortenerAPIView, RetrieveURLAPIView

app_name = "v-1"

urlpatterns = [
    path("create/", ShortenerAPIView.as_view(), name="url-create"),
    path("<str:url>/", RetrieveURLAPIView.as_view(), name="url-create"),
]
