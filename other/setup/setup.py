from setuptools import find_packages, setup

with open('REDME.md', 'r') as f:
    long_description = f.read()

setup(
    name='pgbackup',
    version='0.1.0',
    author='Keith T',
    author_email='dkdkd@linuxacademy.com',
    description='A utitlity fro backing up PostgressSQL databases',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/linuxacademy/pgbackup',
    packages=find_packages('src')
)

# pipenv --python python3.7
# pipenv shell
# vim README.MD