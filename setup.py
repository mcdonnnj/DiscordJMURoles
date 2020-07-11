"""
This is the setup module for the example project.

Based on:

- https://packaging.python.org/distributing/
- https://github.com/pypa/sampleproject/blob/master/setup.py
- https://blog.ionelmc.ro/2014/05/25/python-packaging/#the-structure
"""

# Standard Python Libraries
from glob import glob
import pathlib
from os.path import basename, splitext

# Third-Party Libraries
from setuptools import find_packages, setup


def readme():
    """Read in and return the contents of the project's README.md file."""
    here = pathlib.Path(__file__).parent.resolve()
    return (here / "README.md").read_text(encoding="utf-8")


def package_vars(version_file):
    """Read in and return the variables defined by the version_file."""
    pkg_vars = {}
    with open(version_file) as f:
        exec(f.read(), pkg_vars)  # nosec
    return pkg_vars


setup(
    name="lazybot",
    # Versions should comply with PEP440
    version=package_vars("src/lazybot/_version.py")["__version__"],
    description="Discord bot to handle roles on the JMU Grad server",
    long_description=readme(),
    long_description_content_type="text/markdown",
    # The project's main homepage
    url="https://github.com/ajsnarr98/DiscordJMURoles",
    # Author details
    author="AJ Snarr",
    author_email="ajsnarr98@gmail.com",
    license="License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        "Development Status :: 3 - Alpha",
        # Indicate who your project is intended for
        "Intended Audience :: Developers",
        # Pick your license as you wish (should match "license" above)
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    python_requires=">=3.7, <4",
    # What does your project relate to?
    keywords="Discord",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    py_modules=[splitext(basename(path))[0] for path in glob("src/*.py")],
    install_requires=["discord.py", "docopt", "GitPython", "requests", "setuptools >= 24.2.0"],
    # Conveniently allows one to run the CLI tool as `example`
    entry_points={"console_scripts": ["lazybot = lazybot.bot:main"]},
)
