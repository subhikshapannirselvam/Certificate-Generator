# Certificate-generator-using-Python

Language used: Python

Automating this job can easily save tons of time and manual work and thus also reducing the error rate. 
This Python script generates certificates with the person’s name, reading from an excel file after loading a template certificate in the script.

Package used:
1 .PILLOW
This library provides extensive file format support, an efficient internal representation, and fairly powerful image processing capabilities.
The core image library is designed for fast access to data stored in a few basic pixel formats. It should provide a solid foundation for a general image processing tool.
2 .PANDAS
pandas is a Python package that provides fast, flexible, and expressive data structures designed to make working with structured (tabular, multidimensional, potentially heterogeneous) and time series data both easy and intuitive.
3 .OS
The OS module in python provides functions for interacting with the operating system. This module provides a portable way of using operating system dependent functionality.

Steps involved:
1 .Import PIL package to access stored in Sample Certificate in jpf format that is going to be used.
2 .Import pandas to access the data (names to be printed) that is stored in an csv file.
3 .Import os package to access directories and paths.
4 .Read the names in the csv file and Give the font type if needed.
5 .Open the template image.
6 .Provide co ordinates (x,y) , color (rgb code) and other attributed and write name using ImageDraw.
7 .Finally provide the path to save the Generated file.
