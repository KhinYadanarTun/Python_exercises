try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
        'description': 'My project',
        'author': 'Khin Yadanar Tun',
        'url': 'C:\Users\Aspire\python-exercises\ex47',
        'download_url':' ',
        'author_email': 'KhinYadanarTun2025@gmail.com',
        'version': '0.1',
        'install_requires': ['nose'],
        'packages':['KhinYadanarTun']
        'scripts': [],
        'name': 'ex47'
        }

setup(**config)
