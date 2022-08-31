from setuptools import setup

with open('requirements.txt', 'r') as f:
    requirements = f.read().splitlines()

with open('README.md', 'r') as f:
    readme = f.read()

setup(
    name = 'tokyo.py',
    version = '0.0.1',
    description = 'Python library for interacting with Tokyo API (https://api.miduwu.ga/)',
    long_description = readme,
    url = 'https://github.com/Loxitoh/tokyo.py',
    author = 'Loxitoh',
    author_email = 'loxitoh@gmail.com',
    license = 'MIT',
    packages = [
        'tokyo',
        'tokyo.endpoints'
    ],
    include_package_data = True,
    requires = requirements
)
