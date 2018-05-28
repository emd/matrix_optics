try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'name': 'matrix_optics',
    'version': '0.1',
    'packages': ['matrix_optics'],
    'install_requires': ['numpy', 'nose'],
    'author': 'Evan M. Davis',
    'author_email': 'emd@mit.edu',
    'url': '',
    'description': 'Python tools for matrix optics.'
}

setup(**config)
