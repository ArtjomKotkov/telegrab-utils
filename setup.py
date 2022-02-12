from setuptools import setup, find_packages

requires = [
    'pydantic',
]


setup(
    name='telegrab-utils',
    version='0.0.1',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_require=requires,
)

