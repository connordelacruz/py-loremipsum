from urllib import request, error
from urllib.parse import urlencode


URL = 'https://loripsum.net/api/'


class LoremIpsum(object):
    """Class for generating "Lorem Ipsum" placeholder text"""

    class ParagraphLength(object):
        """Constants for the ``paragraph_length`` parameter in LoremIpsum.generate()"""
        SHORT = 'short'
        MEDIUM = 'medium'
        LONG = 'long'
        VERY_LONG = 'verylong'

    # TODO: make this method always be plaintext, add method for HTML with different params
    @staticmethod
    def generate(paragraph_count=None, paragraph_length=None, plaintext=True):
        # TODO: document
        # TODO: add params for remaining API options
        global URL
        request_url = URL
        if paragraph_count is not None:
            request_url += '{}/'.format(paragraph_count)
        if paragraph_length:
            request_url += paragraph_length + '/'
        if plaintext:
            request_url += 'plaintext/'
        placeholder_text = request.urlopen(request_url).read()
        # TODO: decode('utf8')?
        return placeholder_text

