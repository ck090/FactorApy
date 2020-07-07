# FactorApy <a href="https://pypi.org/project/fa-py/" target="_blank"><img alt="PyPI" src="https://img.shields.io/pypi/v/fa-py?style=for-the-badge"></a>
A Python package to for performing Factor analysis on any given data.

## Installation

This library is available on Pypi
```
pip install fa_py
pip3 install fa_py
```  

All the dependencies are maintained by the project library itself

## Usage

There are 2 base classes in this library. <br>
1. FA_Tests()
2. FA()  

To use the library
```
import fa_py
...
fa = fa_py.FA_Tests() ## Class initializer
fa.kmo(X) ## Pass the dataframe to calculate the KMO test scores
...
```
