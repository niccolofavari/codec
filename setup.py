from setuptools import setup, find_packages

setup(
    name="ppu",
    version="0.1.1",
    packages=find_packages(),
    install_requires=[
        # Add any dependencies your package requires, if any.
    ],
    entry_points={
        "console_scripts": [
            "ppu=ppu.ppu:main",
        ],
    },
    author="Niccolo' Favari",
    author_email="niccolo.favari@gmail.com",
    description="A simple utility to pack (concatenate) and unpack (reconstruct) Python projects",
    license="MIT",
    keywords="ppu pack unpack concatenate reconstruct python projects",
    url="https://github.com/niccolofavari/ppu",
)
