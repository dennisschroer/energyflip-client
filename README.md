# Huisbaasje client

Client to communicate with the API behind [Huisbaasje](https://www.huisbaasje.nl/).

Huisbaasje is an app and measuring device to monitor the usage of electricity and gas in real time.

[![Build Status](https://travis-ci.org/denniss17/huisbaasje-client.svg?branch=master)](https://travis-ci.org/denniss17/huisbaasje-client)
[![Coverage Status](https://coveralls.io/repos/github/dennisschroer/huisbaasje-client/badge.svg?branch=master)](https://coveralls.io/github/dennisschroer/huisbaasje-client?branch=master)
[![PyPI version](https://badge.fury.io/py/huisbaasje-client.svg)](https://pypi.org/project/huisbaasje-client/)

## Installation

    pip install huisbaasje-client

## Usage

See the [example](examples/example.py) on how to use this library.

## Development

This project uses [pipenv](https://pypi.org/project/pipenv/) for dependency and environment management.

Install dependencies using

    pipenv install --dev
    
## Testing

Run all tests using

    pipenv run pytest
    
## Packaging

Create a package using

    python3 setup.py sdist bdist_wheel
    
This creates a package in `dist`

Upload the package using

    python3 -m twine upload dist/*