from setuptools import setup, find_packages

setup(
    name="codec",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        # Add any dependencies your package requires, if any.
    ],
    entry_points={
        "console_scripts": [
            "codec=codec.codec:main",
        ],
    },
    author="Niccolo' Favari",
    author_email="niccolo.favari@gmail.com",
    description="A simple utility to concatenate and reconstruct Python projects",
    license="MIT",
    keywords="codec concatenate reconstruct python projects",
    url="https://github.com/niccolofavari/codec",
)