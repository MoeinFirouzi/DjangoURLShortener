from django.db import models


class Url(models.Model):
    original_url = models.URLField(max_length=300)
    short_url = models.URLField(max_length=30)
    times_followed = models.PositiveIntegerField(default=0)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.short_url
