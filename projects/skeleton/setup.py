try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
        'description': 'My Project',
        'author': 'Khin Yadanar Tun',
        'url':'C:\Users\Aspire\python-exercises\projects\skeleton',
        'download_url': ' ',
        'author_email': 'KhinYadanarTun2025@gmail.com',
        'version': '0.1',
        'install_requires': ['nose'],
        'packages': ['NAME'],
        'scripts': [],
        'name': 'projectname'
        }

setup(**config)
        
