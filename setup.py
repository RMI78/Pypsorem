import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pypsorem",
    version="0.0.1",
    author="John Doe",
    author_email="some.dummy@email.com",
    description="A Python package for generating Lorem Ipsum text",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/RMI78/pypsorem",
    packages=setuptools.find_packages(),
    entry_points={
        "console_scripts": [
            "pypsorem=pypsorem:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "httpx",
        "beautifulsoup4"
    ],
)
