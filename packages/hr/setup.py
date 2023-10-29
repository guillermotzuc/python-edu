# This will call the setuptools module, then import the setup and find_packages
# functions from it
from setuptools import setup, find_packages

with open('README.rst', encoding='UTF-8') as f:
     readme = f.read()

setup(
    name='hr',
    version='1.0.0',
    description='Command line user export utility',
    long_description=readme,
    author='Your Name',
    author_email='youremail@example.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[],

    # This is essentially saying:
    # When you are installed, create an executable named hr,
    # that will call the "main" method inside the "cli" module,
    # inside of the "hr" package.
    entry_points={
        'console_scripts': 'hr=hr.cli:main'
    }
)
