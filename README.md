# Project NEO

## Project description
This is the first project of the Udacity's Intermediate Python Nanodegree. It asks to explore NASA data on Near Earth Objects and write python scripts to answer questions related with Near Earth Objectss (NEOs) and their close approaches.
The part of the Python it touches are:
1. Python Data Structure, especially Lists and Dicts and Sets
1. Functional Programming Aspects of Python - like lambdas, zip , generators and iterators, etc.
1. Object Oriented Programming in Python
    - Creating Classes with custom `__init__`
    - Replacing default magic methods like `__str__` , `__repr__` with your own custom implementation.
    - Creating Subclasses.
1. Reading and writing files (File I/O) to and fro disk, especially:
    - Reading CSV files from disk in Dict format
    - Writing dicts to disk in CSV format.
    - Reading JSON files from disk
    - Writing a collection of dicts to JSON to disk.
1. Writing docstrings and proper docuemntation, which adhere to the following PEP's:
    1. Making a python script adhere to PEP 8, which provides guidelines and best practices on how to write Python code, by using `pycodestyle`.
    1. Making a python script adhere to PEP 257, which aims to standardize the high-level structure of docstrings: what they should contain, and how to say it (without touching on any markup syntax within docstrings), by using `pydocstyle`.

## A Tip

> Making a python script simultaneously adhere to `pydocstyle` and `pycodestyle` is a challenge. But one thing which greatly helps is that in your docstrings write the first line as summary of the function or class within 79 characters including `.`
>
>Then after leaving one blank line (for that using new line shortcut of your coditor is better than manually pressing `enter`) you can write whatever you want and at that time focusing only on `pycodestyle` which is slightly easier than `pydocstyle` and the main reason is that **our understanding of line and indentation is quite different than what system understands due to indentation settings, tab settings, line settings in the various code editors we use**.So in this way you will have `TODO` from `pycodestyle` which you understand and can rectify instead of banging your head against the wall on `pydocstyle` `TODO`s of 1 blank line, which you see is there but the system doesn't recognize.
>
