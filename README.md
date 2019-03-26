[![Python](https://img.shields.io/badge/python-3.7-blue.svg)](https://img.shields.io/badge/python-3.7-blue.svg)
[![License](https://img.shields.io/github/license/philastrophist/correlator.svg)](https://github.com/philastrophist/correlator/blob/develop/LICENSE.md)
# Correlator

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
    - `pip install git+https://github.com/philastrophist/correlator.git`

## Use 
Please see `example.py` for an example which uses nearly all functionality

There are two objects of interest:
* `correlator.LinearRelation`
* `correlator.CorrelationModel`

You may use them  together as demonstrated in `example.py` or indivdually as shown in their home modules under `if __name__ == "__main__"`