import pathlib
from setuptools import setup, find_packages

from src.sphinx_enum_extend import __version__

MODULE_ROOT_NAME='sphinx_enum_extend'
PKG_NAME='sphinx-enum-extend'
SRC_DIR='src'
ISRELEASED = True
VERSION = __version__


# The directory containing this file
HERE = pathlib.Path(__file__).parent
# The text of the README file
with open(HERE / "README.md") as fh:
    README = fh.read()

print(README)

# This call to setup() does all the work
setup(
    name=PKG_NAME,
    version=VERSION,
    python_requires='>=3.4.0',
    description="Spinx plugin for documenting enum-extend.AutoEnum",
    long_description_content_type="text/markdown",
    long_description=README,
    url="https://github.com/Amourspirit/python-sphinx-enum-extend",
    author=":Barry-Thomas-Paul: Moss",
    author_email='bigbytetech@gmail.com',
    license="MIT",
    # packages=[MODULE_ROOT_NAME],
    packages=find_packages(where='src', exclude=['tests', 'ex']),
    package_dir={'': 'src'},
    install_requires=[
        'enum-extend >=0.1.1',
    ],
    # py_modules=MODULES,
    keywords=['python', 'enum', 'autoenum', 'sphinx', 'sphinx-extension', 'enum-docstring', 'enum-extend'],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    include_package_data=True,
)
