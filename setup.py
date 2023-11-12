from setuptools import setup, find_packages
import os

with open('./README.md','r') as f:
    long_description = f.read()

VERSION = '0.1'
DESCRIPTION = 'Math Quiz Package'
LONG_DESCRIPTION = 'This package has a math quiz inbuilt in it'

# Setting up
setup(
    name="math-quiz",
    version=VERSION,
    author="Aamir (Aamir Suhail)",
    author_email="<aamir.ms.suhail@fau.de>",
    license="Apache",
    description=DESCRIPTION,
    url='https://github.com/Aamir-suhail001/dsss_homework_2-',
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(where='math_quiz'),
    keywords=['math quiz', 'quiz games', 'fun math game'],
)