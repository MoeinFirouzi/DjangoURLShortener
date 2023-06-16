from django.urls import path, include

app_name = "url-shortener"

urlpatterns = [
    path("", include("url_shortener.api.v1.urls")),
]
