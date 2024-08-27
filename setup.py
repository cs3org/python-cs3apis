import setuptools
import os

with open("README.md", "r") as fh:
    long_description = fh.read()

version = os.getenv("PACKAGE_VERSION", "0.0.0")

setuptools.setup(
    name="cs3apis",
    version=version,
    setup_requires=['setuptools_scm'],
    author="CS3 Organization",
    author_email="contact@cs3community.org",
    description="CS3 API bindings for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cs3org/python-cs3apis",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
