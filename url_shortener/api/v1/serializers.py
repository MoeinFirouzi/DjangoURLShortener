from rest_framework import serializers
from url_shortener.models import Url
from url_shortener.utils import URLShortener


class URLSerializer(serializers.ModelSerializer):
    class Meta:
        model = Url
        fields = ["original_url"]

    def create(self, validated_data):
        original_url = validated_data.get("original_url")
        shortener = URLShortener()

        validated_data["short_url"] = "http://127.0.0.1:8000/" \
            + shortener.encode_md5(original_url)
        return super().create(validated_data)

    def validate(self, attrs):
        """
        Checks if original_url not be empty.
        """
        original_url = attrs.get("original_url")
        if original_url is None:
            raise serializers.ValidationError("URL can't be empt!")
        return super().validate(attrs)

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["short_url"] = instance.short_url
        return rep
