from sympy import *
from math import *
from tkinter import *
import logging
logging.basicConfig(filename="name.log", level=logging.INFO)
data=''
try:
    handle = open("test.txt", "r")
    for line in handle:
        if len(line) != 0:
            data = line
            print(data)
            a = simplify(data)
            print(solve(a))
            logging.info("\nlevelname: INFO message: equation: %s result: %s" % (data, a))

except Exception as error:
    print("error")

handle.close()