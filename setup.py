from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

# Get __version__
with open('./loremipsum.py') as f:
    exec(f.read())

# Metadata

dev_status = 'Development Status :: 5 - Production/Stable'

CLASSIFIERS = '''
Intended Audience :: Developers
License :: OSI Approved :: MIT License
Programming Language :: Python
Programming Language :: Python :: 3
Topic :: Software Development :: Testing
Topic :: Utilities
{}
'''.format(dev_status)

url = 'https://github.com/connordelacruz/py-loremipsum/'

download_url = url + 'archive/{}.tar.gz'.format(__version__)

project_urls = {
    'Documentation': 'http://connordelacruz.com/py-loremipsum/',
    'Source': url,
}

setup(name='py-loremipsum',
      version=__version__,
      description='Python module for generating placeholder text using the https://loripsum.net/ API',
      long_description=readme(),
      url=url,
      download_url=download_url,
      project_urls=project_urls,
      author='Connor de la Cruz',
      author_email='connor.c.delacruz@gmail.com',
      license='MIT',
      classifiers=[x for x in CLASSIFIERS.split("\n") if x],
      py_modules=['loremipsum'],
      zip_safe=False)

