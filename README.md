# EnergyFlip client

Client to communicate with the API behind [EnergyFlip](https://www.energyflip.com/).

EnergyFlip is an app and measuring device to monitor the usage of electricity and gas in real time.

[![Build status](https://github.com/dennisschroer/energyflip-client/actions/workflows/build.yml/badge.svg)](https://github.com/dennisschroer/energyflip-client/actions)
[![Coverage Status](https://coveralls.io/repos/github/dennisschroer/energyflip-client/badge.svg?branch=master)](https://coveralls.io/github/dennisschroer/energyflip-client?branch=master)
[![PyPI version](https://badge.fury.io/py/energyflip-client.svg)](https://pypi.org/project/energyflip-client/)

## Installation

    pip install energyflip-client

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