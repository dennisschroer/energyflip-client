import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="huisbaasje-client",
    version="0.1.0",
    author="Dennis Schroer",
    author_email="dev@dennisschroer.nl",
    description="Client for Huisbaasje",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/denniss17/huisbaasje-client",
    packages=setuptools.find_packages(),
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Home Automation"
    ],
    python_requires='>=3.6'
)
