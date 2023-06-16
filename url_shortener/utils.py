import hashlib


class URLShortener:
    """
    This class convert given url to hash by md5 algorithm.
    - encode_md5: returns first 16 character of hashed url.
    """

    def encode_md5(self, url):
        return str(hashlib.md5(url.encode("utf-8")).hexdigest())[:16]
