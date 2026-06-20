class Program:
    """The full AsifLang program."""

    def __init__(self, statements):
        self.statements = statements


class Assignment:
    """A statement such as: x = 10."""

    def __init__(self, variable_name, expression):
        self.variable_name = variable_name
        self.expression = expression


class Show:
    """A statement such as: show x."""

    def __init__(self, expression):
        self.expression = expression


class Number:
    """An integer number."""

    def __init__(self, value):
        self.value = value


class Variable:
    """A variable name."""

    def __init__(self, name):
        self.name = name


class BinaryOperation:
    """An arithmetic expression such as: x + 5."""

    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right

