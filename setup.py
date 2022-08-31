from setuptools import setup
import re

requirements = []

with open('requirements.txt', 'r') as f:
    requirements = f.read().splitlines()

with open('README.md', 'r') as f:
    readme = f.read()

version = ''

with open('tokyo/__init__.py') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('Could not find __version__ in __init__.py file.')

setup(
    name = 'tokyo.py',
    version = version,
    description = 'Python library for interacting with Tokyo API (https://api.miduwu.ga/)',
    long_description = readme,
    long_description_content_type = 'text/x-rst',
    url = 'https://github.com/Loxitoh/tokyo.py',
    author = 'Loxitoh',
    author_email = 'loxitoh@gmail.com',
    license = 'MIT',
    packages = [
        'tokyo',
        'tokyo.endpoints'
    ],
    include_package_data = True,
    install_requires = requirements
)
