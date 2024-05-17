#!/usr/bin/env python

from setuptools import setup, find_packages


with open("README.md") as f:
    readme = f.read()

with open("LICENSE") as f:
    license = f.read()

setup(
    name="susskind-pipe-theory",
    version="0.1.0",
    description="Leveraging graph theory and reinforcement learning to find the input for a desired output in a pipe maze.",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Suren Lockwood",
    author_email="dev@behnamlal.xyz",
    url="https://github.com/CheesyChocolate/susskind-pipe-theory",
    license=license,
    packages=find_packages(exclude=("tests", "docs")),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[],
)
