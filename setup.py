try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'name': 'matrix_optics',
    'version': '0.1',
    'packages': [
        'matrix_optics',
        'matrix_optics.numeric',
        'matrix_optics.symbolic'],
    'install_requires': ['numpy', 'sympy', 'nose'],
    'author': 'Evan M. Davis',
    'author_email': 'emd@mit.edu',
    'url': '',
    'description': 'Python tools for matrix optics.'
}

setup(**config)
