from setuptools import setup, find_packages

# Get __version__
with open('./loremipsum/version.py') as f:
    exec(f.read())

setup(name='py-loremipsum',
      version=__version__,
      description='Python class for generating placeholder text using https://loripsum.net/ API',
      url='https://github.com/connordelacruz/python-loremipsum/',
      download_url='https://github.com/connordelacruz/python-loremipsum/archive/{}.tar.gz'.format(__version__),
      author='Connor de la Cruz',
      author_email='connor.c.delacruz@gmail.com',
      license='MIT',
      packages=find_packages(),
      zip_safe=False)

