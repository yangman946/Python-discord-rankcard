from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'A simple discord rank card written in python.'
LONG_DESCRIPTION = 'A simple discord rank card written in python.'

# Setting up
setup(
    name="Python-discord-rankcard",
    version=VERSION,
    author="yangman946",
    author_email="clarenceyang284@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION ,
    packages=find_packages(),
    install_requires=['Pillow', 'requests'],
    keywords=['python', 'pillow', 'discord', 'discord-py'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
