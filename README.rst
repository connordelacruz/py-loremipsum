=====================
Lorem Ipsum Generator
=====================

|pypi|
|license|
|github|

.. |pypi| image:: https://img.shields.io/pypi/v/py-loremipsum.svg
    :alt: PyPI
    :target: https://pypi.python.org/pypi/py-loremipsum

.. |license| image:: https://img.shields.io/pypi/l/py-loremipsum.svg
    :alt: PyPI - License

.. |github| image:: https://img.shields.io/badge/GitHub--green.svg?style=social&logo=github
    :alt: GitHub
    :target: https://github.com/connordelacruz/py-loremipsum


Python module for generating placeholder text using the `loripsum.net API <https://loripsum.net/>`__.


Basic Usage
===========

.. code:: python

    import loremipsum

    # Generate plain text paragraphs with API default settings
    no_options = loremipsum.generate()

    # Generate 3 medium length paragraphs in plain text
    plaintext = loremipsum.generate(3, loremipsum.ParagraphLength.MEDIUM)

    # Generate 1 long paragraph with HTML tags
    simple_html = loremipsum.generate(1, loremipsum.ParagraphLength.LONG, plaintext=False)

    # Generate 1 long paragraph with HTML headers and decorated text
    options = ['headers', 'decorate']
    decorated_html = loremipsum.generate(1, loremipsum.ParagraphLength.LONG, plaintext=False, html_options=options)


Command Line
============

Basic
-----

This package includes the ``loremipsum`` command to generate text from the
command line. For details on command line options:

::

    loremipsum --help


Example Usage
~~~~~~~~~~~~~

Generate 3 short paragraphs with trailing new lines and pipe output to
``placeholder.txt``:

::
    
    loremipsum 3 --length short --trailing-newlines > placeholder.txt


Generate 4 HTML paragraphs and pipe output to ``placeholder.html``:

::

    loremipsum 4 --html > placeholder.html


Copy to Clipboard
-----------------

This package includes an additional ``lorem-copy`` command to generate text and
copy it to the clipboard using `pyperclip
<https://github.com/asweigart/pyperclip>`__. For details on command line
options:

::

    lorem-copy --help

**Note:** ``pyperclip`` should work out of the box on macOS and Windows, but may
need some additional packages on Linux distros. Check `their documentation
<https://pyperclip.readthedocs.io/en/latest/introduction.html>`__ first if
you're having difficulty with the ``lorem-copy`` command.


.. readme-only

For more details, see the `documentation <https://connordelacruz.com/py-loremipsum/>`__.

