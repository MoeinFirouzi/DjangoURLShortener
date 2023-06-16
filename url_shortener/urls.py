from django.urls import path, include

app_name = "url-shortener"

urlpatterns = [
    path("api/v1/", include("url_shortener.api.v1.urls")),
]
