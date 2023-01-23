import abc
from typing import Optional, Callable
from enum import Enum


class Token (metaclass=abc.ABCMeta):
    __text: Optional[str]
    is_evaluator: bool = False  # if token can evaluate sub-nodes and replace them with Number

    def __init__(self, text):
        self.__text = text

    @property
    def text(self):
        return self.__text

    @abc.abstractmethod
    def value(self, *args) -> float:
        pass

    def __repr__(self) -> str:
        return self.__text


class Number (Token):
    _value: float

    def __init__(self, text):
        super().__init__(text)
        self._value = float(self.text)

    def value(self, *args) -> float:
        return self._value


class Operator (Token):
    class Associativity (Enum):
        Left = 0
        Right = 1

    class Ary (Enum):
        Unary = 1
        Binary = 2

    is_evaluator = True  # Operators are evaluators

    _designation: str  # how operator represented in str
    _priority: int  # precedence of operator
    _associativity: Associativity = Associativity.Left  # evaluating start
    _args_count: Ary = Ary.Binary  # operator's argument count
    _backend_func: Callable[[...], float]  # function, that make evaluating

    def value(self, *args) -> float:
        return self._backend_func(*args)

    def __repr__(self):
        return self._designation
