try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import async_actor

with open("README.rst") as readme_file:
    readme_string = readme_file.read()

setup(
    name="async-actor",
    version=async_actor.__version__,
    description="",
    author="Xin Huang",
    author_email="xinhuang.abc@gmail.com",
    url="https://github.com/xinhuang/async-actor",
    py_modules=['async_actor'],
    packages=['tests'],
    license="License :: OSI Approved :: MIT License",
    long_description=readme_string,
)
