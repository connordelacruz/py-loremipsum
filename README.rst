Lorem Ipsum Generator
=====================

Python module for generating placeholder text using the `loripsum.net API <https://loripsum.net/>`__.

Basic Usage
===========

.. code:: python

    import loremipsum

    # Generate 3 medium length paragraphs in plain text
    plaintext = loremipsum.generate(3, loremipsum.ParagraphLength.MEDIUM)

    # Generate 1 long paragraph with HTML tags
    simple_html = loremipsum.generate(1, loremipsum.ParagraphLength.LONG, plaintext=False)

    # Generate 1 long paragraph with HTML headers and decorated text
    options = ['headers', 'decorate']
    decorated_html = loremipsum.generate(1, loremipsum.ParagraphLength.LONG, plaintext=False, html_options=options)


.. readme-only

For more details, see the `documentation <http://connordelacruz.com/py-loremipsum/>`__.
