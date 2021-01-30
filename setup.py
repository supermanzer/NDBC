import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="NDBC",
    version="1.0.0",
    description="A package to automate the loading of NDBC data to a custom object.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/GenSci/NDBC",
    author="C. Ryan Manzer",
    author_email="ryan@gensci.org",
    packages=['NDBC'],
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],

    test_suite="tests",
    python_requires='>=3.7'  # use of data class requires higher version of Python
)
