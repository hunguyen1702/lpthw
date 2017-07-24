try:
    from setuptools import setup
except ImportError:
    from disutils.core import setup

config = { 
    'description': 'My Project',
    'author': 'hungnv',
    'url': 'URL to get it at.',
    'download_url': 'where to download it',
    'author_email': 'hunguyen1702@gmail.com',
    'version': '0.0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': ['bin/skeleton'],
    'name': 'projectname'
}

setup(**config)

