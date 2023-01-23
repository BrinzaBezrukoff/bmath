from typing import List, Callable


NumberType = float


class Node:
    parent: "Node"
    children: List["Node"]


class ConstantNumber (Node):
    value: NumberType


class Evaluable (Node):
    eval_func: Callable[[...], NumberType]

    def __call__(self, *args, **kwargs) -> NumberType:
        return self.eval_func(*self.children)


class UnaryOperator (Node):
    pass


class BinaryOperator (Node):
    pass


class Function (Node):
    pass


class Variable (Node):
    name: str


class Derivative (Node):
    var_name: str
