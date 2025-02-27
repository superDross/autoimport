"""Python package building configuration."""

import re
from glob import glob
from os.path import basename, splitext

from setuptools import find_packages, setup

# Avoid loading the package to extract the version

with open("src/autoimport/version.py") as fp:
    version_match = re.search(r'__version__ = "(?P<version>.*)"', fp.read())
    if version_match is None:
        raise ValueError("The version is not specified in the version.py file.")
    version = version_match["version"]

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

setup(
    name="autoimport",
    version=version,
    description="Autoimport missing python libraries.",
    author="Lyz",
    author_email="lyz-code-security-advisories@riseup.net",
    license="GNU General Public License v3",
    # SIM115: Use context handler for opening files. In this case it doesn't make sense.
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/lyz-code/autoimport",
    packages=find_packages("src"),
    package_dir={"": "src"},
    package_data={"autoimport": ["py.typed"]},
    py_modules=[splitext(basename(path))[0] for path in glob("src/*.py")],
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: Unix",
        "Operating System :: POSIX",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Utilities",
        "Natural Language :: English",
    ],
    entry_points="""
        [console_scripts]
        autoimport=autoimport.entrypoints.cli:cli
    """,
    install_requires=["autoflake", "Click", "pyprojroot", "sh", "maison"],
)
