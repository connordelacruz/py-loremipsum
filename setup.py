from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

with open('VERSION') as version_file:
    version = version_file.read().strip()

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

download_url = url + 'archive/{}.tar.gz'.format(version)

project_urls = {
    'Documentation': 'https://connordelacruz.com/py-loremipsum/',
    'Source': url,
}

setup(name='py-loremipsum',
      version=version,
      description='Python module for generating placeholder text using the https://loripsum.net/ API',
      long_description=readme(),
      url=url,
      download_url=download_url,
      project_urls=project_urls,
      author='Connor de la Cruz',
      author_email='connor.c.delacruz@gmail.com',
      license='MIT',
      classifiers=[x for x in CLASSIFIERS.split("\n") if x],
      install_requires=[
          'pyperclip>=1.6.4,<1.7',
      ],
      py_modules=['loremipsum'],
      entry_points = {
          'console_scripts': [
              'loremipsum = loremipsum:main',
              'lorem-copy = loremipsum:copy',
          ],
      },
      zip_safe=False)

