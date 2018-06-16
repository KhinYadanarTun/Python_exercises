try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
        'description': 'My Project',
        'author': 'My Name',
        'url': ' ',
        'download_url': 'C:/Users/Aspire/python-exercises/ex48 ',
        'author_email': 'KhinYadanarTun2025@gmail.com',
        'version': '0.1',
        'install_requires': ['nose'],
        'packages': ['NAME'],
        'scripts': [ ],
        'name': 'projectname'
        }


setup(**config)

