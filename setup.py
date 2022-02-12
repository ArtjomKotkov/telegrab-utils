from setuptools import setup

requires = [
    'pydantic',
]


setup(
    name='telegrab-utils',
    version='0.0.1',
    packages=['telegrab_utils'],
    install_require=requires,
)

