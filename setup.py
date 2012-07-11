import os
try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages


def read_file(filename):
    """Read a file into a string"""
    path = os.path.abspath(os.path.dirname(__file__))
    filepath = os.path.join(path, filename)
    try:
        return open(filepath).read()
    except IOError:
        return ''


def get_readme():
    """Return the README file contents. Supports text,rst, and markdown"""
    for name in ('README', 'README.rst', 'README.md'):
        if os.path.exists(name):
            return read_file(name)
    return ''

setup(
    name = 'Django Paginator',
    version = __import__('paginator').get_version().replace(' ', '-'),
    url = 'https://bitbucket.org/nextscreenlabs/django-paginator',
    author = 'Jason Christa',
    author_email = 'jason@zeitcode.com',
    description = 'A template tag that works with Django\'s Paginator class',
    long_description = get_readme(),
    packages = find_packages(exclude=['tests']),
    include_package_data = True,
    install_requires = read_file('requirements.txt'),
    classifiers = [
        'Environment :: Web Environment',
        'License :: OSI Approved :: BSD Liscense',
        'Framework :: Django',
        'Programming Language :: Python',
    ],
)
