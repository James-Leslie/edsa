from setuptools import setup, find_packages

setup(
    name='edsa',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA analyse hackathon model solution',
    long_description=open('README.md').read(),
    url='https://github.com/James-Leslie/edsa',
    author='James Leslie',
    author_email='james@explore-ai.net'
)
