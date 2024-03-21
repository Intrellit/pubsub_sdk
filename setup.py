from setuptools import setup, find_packages

setup(
    name='pubsub_sdk',
    version='0.0.1',
    url='https://github.com/Intrellit/pubsub_sdk.git',
    author='Marek Michalik',
    author_email='marek@justpoint.com',
    description='Pub/Sub SDK',
    packages=find_packages(),
    install_requires=['requests >= 2.31.0'],
)
