import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="saviour", # Replace with your own username
    version="0.0.3",
    author="legedith",
    author_email="jatindehmiwal@gmail.com",
    description="A helper for hackers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/legedith",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    scripts=['bin/saviour-style','bin/saviour-check','bin/saviour-help','bin/saviour-practice','bin/saviour-pseudocode'],
)