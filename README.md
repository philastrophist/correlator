[![PyPI](https://img.shields.io/pypi/v/candid.svg)](https://pypi.python.org/pypi/candid/)
[![License](https://img.shields.io/github/license/philastrophist/decorrelator.svg)](https://github.com/philastrophist/decorrelator/blob/master/LICENSE.md)
[![Build Status](https://travis-ci.com/philastrophist/candid.svg?token=3fPC1Wwg7aekKMkBjGPa&branch=master)](https://travis-ci.com/philastrophist/candid)
# Decorrelator

Analysing correlations between parameters whilst controlling for the effects of others.

(Fancy partial correlation)

## Installation
* create new environment 
    - `conda create -n NAME python=3.7`
* activate
    - `source activate NAME`
* install high-performance libraries
    - `conda install numpy mkl scipy`
* install correlator
    - `pip install git+https://github.com/philastrophist/decorrelator.git`

## Use 
Please see `example.py` for an example which uses nearly all functionality

There are two objects of interest:
* `decorrelator.LinearRelation`
* `decorrelator.CorrelationModel`

You may use them  together as demonstrated in `example.py` or indivdually as shown in their home modules under `if __name__ == "__main__"`
