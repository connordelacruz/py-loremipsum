import argparse
from urllib import request, error
import pyperclip


# TODO: bump version
__version__ = '1.0.3'

URL = 'https://loripsum.net/api/'


class ParagraphLength():
    """Constants for the ``paragraph_length`` parameter in generate()"""
    SHORT = 'short'
    MEDIUM = 'medium'
    LONG = 'long'
    VERY_LONG = 'verylong'

    @classmethod
    def __options__(cls):
        """Returns a list of class attributes that aren't prefixed with an underscore"""
        return [i for i in cls.__dict__.keys() if i[:1] != '_']


# Valid keys for html_options
HTML_OPTIONS = [
    'decorate',  # Add bold, italic and marked text.
    'link',  # Add links.
    'ul',  # Add unordered lists.
    'ol',  # Add numbered lists.
    'dl',  # Add description lists.
    'bq',  # Add blockquotes.
    'code',  # Add code samples.
    'headers',  # Add headers.
]


def _request_url_string(request_args):
    url_string = URL
    for arg in request_args:
        url_string += '{}/'.format(arg)
    return url_string


def _generate(request_url):
    placeholder_text = request.urlopen(request_url).read().decode('utf8')
    return placeholder_text


def generate(paragraph_count=None, paragraph_length=None, allcaps=False, prude=False, plaintext=True, html_options=None,
             trailing_newlines=False):
    """Generate Lorem Ipsum placeholder text using the https://loripsum.net API.

    Further documentation of parameters can be found at `loripsum.net <https://loripsum.net>`_

    :param paragraph_count: (Optional) The number of paragraphs to generate. If
        unspecified, API defaults to 3
    :param paragraph_length: (Optional) The average length of a paragraph. Possible
        values are declared as attributes in ``LoremIpsum.ParagraphLength``. If
        unspecified, API defaults to 'long'
    :param allcaps: (Default = False) Use ALL CAPS
    :param prude: (Default = False) Prude version. From the API documentation:
        "The original text contains a few instances of words like 'sex' or 'homo'.
        Personally, we don't mind, because these are just common latin words
        meaning 'six' and 'man'. However, some people (or your clients) might be
        offended by this, so if you select the 'Prude version', these words will be
        censored."
    :param plaintext: (Default = True) Return plain text, no HTML
    :param html_options: (Default = None) List of html options to specify in
        request. This will be ignored if plaintext = True. The following options
        are accepted

            - 'decorate' - Add bold, italic and marked text.
            - 'link'- Add links.
            - 'ul' - Add unordered lists.
            - 'ol' - Add numbered lists.
            - 'dl' - Add description lists.
            - 'bq' - Add blockquotes.
            - 'code' - Add code samples.
            - 'headers' - Add headers.
    :param trailing_newlines: (Default = False) If False, strip trailing new lines
        in generated text. If True, leave trailing new lines in.

    :return: Result of querying loripsum.net API using the specified options
    """
    request_args = []
    if paragraph_count is not None:
        request_args.append(paragraph_count)
    if paragraph_length:
        request_args.append(paragraph_length)
    if allcaps:
        request_args.append('allcaps')
    if prude:
        request_args.append('prude')
    if plaintext:
        request_args.append('plaintext')
    # If not plaintext and html_options is specified, add those args as well
    elif html_options is not None:
        # Ignore invalid options
        valid_html_options = [
            option for option in html_options if option in HTML_OPTIONS
        ]
        request_args.extend(valid_html_options)
    request_url = _request_url_string(request_args)
    placeholder_text = _generate(request_url)
    return placeholder_text if trailing_newlines else placeholder_text.rstrip()


# Command Line Functions

def _parser():
    """Returns common ArgumentParser for command line functions"""
    # TODO: add help, description, etc
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'paragraph_count', type=int, nargs='?', default=1
    )
    # TODO: ensure this is working
    parser.add_argument(
        '-l', '--length', dest='paragraph_length', type=str.upper,
        choices=ParagraphLength.__options__()
    )
    parser.add_argument(
        '--allcaps', action='store_true', default=False
    )
    parser.add_argument(
        '--prude', action='store_true', default=False
    )
    # TODO: take html options?
    parser.add_argument(
        '--html', dest='plaintext', action='store_false', default=True
    )
    parser.add_argument(
        '--trailing-newlines', action='store_true', default=False
    )
    return parser


def main():
    """Prints generated text using parsed args"""
    args = _parser().parse_args()
    print(generate(**vars(args)))

def copy():
    """Copies generated text using parsed args to clipboard"""
    args = _parser().parse_args()
    pyperclip.copy(generate(**vars(args)))
    print('Copied to clipboard.')


if __name__ == '__main__':
    main()


