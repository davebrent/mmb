import os
from setuptools import setup


def read(filename):
    path = os.path.join(os.path.dirname(__file__), filename)
    return open(path).read()


setup(
    name="mmb",
    version="0.0.1",
    packages=["mmb"],
    description="A backup tool for the elektron monomachine",
    author="Dave Poulter",
    author_email="dapoulter@gmail.com",
    url="https://github.com/davebrent/mmb",
    license="MIT",
    long_description=read("README.rst"),
    keywords='elektron monomachine backup',
    platforms="any",
    install_requires=[
        "rtmidi-python",
        "click>=3"
    ],
    entry_points={
        "console_scripts": [
            "mmb = mmb:main",
        ]
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Topic :: Multimedia :: Sound/Audio :: MIDI",
        "Topic :: System :: Archiving :: Backup",
    ],
)
