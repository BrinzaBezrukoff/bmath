from enum import Enum


basicStates = {  # машина состояний??? надо ли так...
    "expression": ({
        "unary": ({}, ["number", "lbrace"]),
        "number": ({}, ["binary", "rbrace", None]),
        "binary": ({}, ["number", "lbrace"]),
        "lbrace": ({}, ["expression"]),
        "rbrace": ({}, ["binary", None]),
        None: ({}, [])
    }, [])
}


class Parser:
    def __init__(self, states=basicStates, ):
        self.states = states
        self.state_stack = list()

    def parse(self, expression: str):
        pass

