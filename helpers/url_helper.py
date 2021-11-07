import sys

sys.path.append('../')

from helpers.string_helper import StringHelper

class UrlHelper:
    @classmethod
    def extension(cls, url):
        return StringHelper.last_substring(StringHelper.last_substring(url, '/'), '.')
