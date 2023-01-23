import operator

from bmath.token import Operator


# Default package priorities
PRIORITY_ADD = 1
PRIORITY_MUL = 11
PRIORITY_POW = 21


class Addition (Operator):
    _designation = "+"
    _priority = PRIORITY_ADD
    _backend_func = operator.add


class Subtraction (Operator):
    _designation = "-"
    _priority = PRIORITY_ADD
    _backend_func = operator.sub


class Multiplication (Operator):
    _designation = "*"
    _priority = PRIORITY_MUL
    _backend_func = operator.mul


class Division (Operator):
    _designation = "/"
    _priority = PRIORITY_MUL
    _backend_func = operator.truediv


class Modulo (Operator):
    _designation = "%"
    _priority = PRIORITY_MUL
    _backend_func = operator.mod


class Power (Operator):
    _designation = "^"
    _priority = PRIORITY_POW
    _backend_func = operator.pow
