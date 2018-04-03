from setuptools import setup

# Get __version__
with open('./loremipsum.py') as f:
    exec(f.read())

setup(name='py-loremipsum',
      version=__version__,
      description='Python class for generating placeholder text using https://loripsum.net/ API',
      url='https://github.com/connordelacruz/py-loremipsum/',
      download_url='https://github.com/connordelacruz/py-loremipsum/archive/{}.tar.gz'.format(__version__),
      author='Connor de la Cruz',
      author_email='connor.c.delacruz@gmail.com',
      license='MIT',
      py_modules=['loremipsum'],
      zip_safe=False)

