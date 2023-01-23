import abc
from typing import List, Optional, Deque
from collections import deque

from bmath.token import Token


class Node (metaclass=abc.ABCMeta):
    parent: "Node" = None
    children: List["Node"] = list()
    token: Token


class AST:
    root: Optional[Node]

    def __init__(self):
        pass
