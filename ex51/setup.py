try:
    from setuptools import setup
except ImportError:
    from disutils.core import setup

config = { 
    'description': 'Excercise 50 LPTHW Your First Web',
    'author': 'hungnv',
    'author_email': 'hunguyen1702@gmail.com',
    'version': '0.0.1',
    'install_requires': ['nose'],
    'packages': ['gothonweb'],
    'scripts': ['bin/gothonweb'],
    'name': 'gothonweb'
}

setup(**config)

