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
    def generate(paragraph_count=None, paragraph_length=None, plaintext=True, allcaps=False, prude=False):
        """Generate Lorem Ipsum placeholder text using the https://loripsum.net API.

        Further documentation of parameters can be found at `loripsum.net <https://loripsum.net>`_

        :param paragraph_count: (Optional) The number of paragraphs to generate. If
            unspecified, API defaults to 3
        :param paragraph_length: (Optional) The average length of a paragraph. Possible
            values are declared as attributes in ``LoremIpsum.ParagraphLength``. If
            unspecified, API defaults to 'long'
        :param plaintext: (Default = True) Return plain text, no HTML
        :param allcaps: (Default = False) Use ALL CAPS
        :param prude: (Default = False) Prude version. From the API documentation:
            "The original text contains a few instances of words like 'sex' or 'homo'.
            Personally, we don't mind, because these are just common latin words
            meaning 'six' and 'man'. However, some people (or your clients) might be
            offended by this, so if you select the 'Prude version', these words will be
            censored."
        """
        global URL
        request_url = URL
        if paragraph_count is not None:
            request_url += '{}/'.format(paragraph_count)
        if paragraph_length:
            request_url += paragraph_length + '/'
        if plaintext:
            request_url += 'plaintext/'
        if allcaps:
            request_url += 'allcaps/'
        if prude:
            request_url += 'prude/'
        placeholder_text = request.urlopen(request_url).read().decode('utf8')
        return placeholder_text

