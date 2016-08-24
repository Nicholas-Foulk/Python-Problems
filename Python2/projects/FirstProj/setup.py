try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Nicholas Foulk',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'nickfoulksjsu@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['FirstProj'],
    'scripts': [],
    'name': 'FirsProj'
}

setup(**config)
