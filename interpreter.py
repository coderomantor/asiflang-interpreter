from ast_nodes import Assignment, BinaryOperation, Number, Program, Show, Variable
from tokens import DIVIDE, MINUS, MULTIPLY, PLUS


class Interpreter:
    """Executes an AsifLang AST."""

    def __init__(self):
        # The symbol table stores variable names and their integer values.
        self.symbol_table = {}

    def interpret(self, program):
        """Run every statement in the program."""
        if not isinstance(program, Program):
            raise Exception("Runtime Error: Invalid program")

        for statement in program.statements:
            self.execute(statement)

    def execute(self, statement):
        """Run one statement."""
        if isinstance(statement, Assignment):
            value = self.evaluate(statement.expression)
            self.symbol_table[statement.variable_name] = value
            return

        if isinstance(statement, Show):
            value = self.evaluate(statement.expression)
            print(value)
            return

        raise Exception("Runtime Error: Unknown statement")

    def evaluate(self, expression):
        """Calculate the value of an expression."""
        if isinstance(expression, Number):
            return expression.value

        if isinstance(expression, Variable):
            if expression.name not in self.symbol_table:
                raise Exception(f"Variable not defined: {expression.name}")
            return self.symbol_table[expression.name]

        if isinstance(expression, BinaryOperation):
            left = self.evaluate(expression.left)
            right = self.evaluate(expression.right)

            if expression.operator == PLUS:
                return left + right
            if expression.operator == MINUS:
                return left - right
            if expression.operator == MULTIPLY:
                return left * right
            if expression.operator == DIVIDE:
                if right == 0:
                    raise Exception("Division by zero")
                return left // right

        raise Exception("Runtime Error: Unknown expression")
