try:
    from setuptools import setup
except ImportError:
    from disutils.core import setup

config = { 
    'description': 'Excercise 52 LPTHW Your First Web',
    'author': 'hungnv',
    'author_email': 'hunguyen1702@gmail.com',
    'version': '0.0.1',
    'install_requires': ['nose'],
    'packages': ['ex52'],
    'scripts': ['bin/app.py'],
    'name': 'ex52'
}

setup(**config)

