import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="timelogging",
    version="2.0.12",
    author="Tillmann Brodbeck",
    author_email="t.b@riseup.net",
    description="Small Logging Library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tbrodbeck/timelogging",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
