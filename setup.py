from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

# Get __version__
with open('./loremipsum.py') as f:
    exec(f.read())

setup(name='py-loremipsum',
      version=__version__,
      description='Python module for generating placeholder text using the https://loripsum.net/ API',
      long_description=readme(),
      url='https://github.com/connordelacruz/py-loremipsum/',
      download_url='https://github.com/connordelacruz/py-loremipsum/archive/{}.tar.gz'.format(__version__),
      author='Connor de la Cruz',
      author_email='connor.c.delacruz@gmail.com',
      license='MIT',
      py_modules=['loremipsum'],
      zip_safe=False)

