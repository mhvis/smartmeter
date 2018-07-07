import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="smartmeter",
    version="1.0.0",
    author="Maarten Visscher",
    author_email="mail@maartenvisscher.nl",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mhvis/smartmeter",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
