from ast_nodes import Assignment, BinaryOperation, Number, Program, Show, Variable
from tokens import (
    ASSIGN,
    DIVIDE,
    EOF,
    IDENTIFIER,
    LPAREN,
    MINUS,
    MULTIPLY,
    NUMBER,
    PLUS,
    RPAREN,
    SHOW,
)


class Parser:
    """Builds an AST from AsifLang tokens."""

    def __init__(self, tokens):
        self.tokens = tokens
        self.position = 0
        self.current_token = self.tokens[self.position]

    def advance(self):
        """Move to the next token."""
        self.position += 1
        if self.position < len(self.tokens):
            self.current_token = self.tokens[self.position]

    def eat(self, token_type):
        """Accept the current token if it has the expected type."""
        if self.current_token.type == token_type:
            token = self.current_token
            self.advance()
            return token

        raise Exception(f"Invalid syntax: expected {token_type}, found {self.current_token.type}")

    def parse(self):
        """Parse all statements in the program."""
        statements = []

        while self.current_token.type != EOF:
            statements.append(self.statement())

        return Program(statements)

    def statement(self):
        """Parse an assignment statement or a show statement."""
        if self.current_token.type == IDENTIFIER:
            variable_name = self.eat(IDENTIFIER).value
            self.eat(ASSIGN)
            expression = self.expression()
            return Assignment(variable_name, expression)

        if self.current_token.type == SHOW:
            self.eat(SHOW)
            expression = self.expression()
            return Show(expression)

        raise Exception(f"Invalid syntax near {self.current_token}")

    def expression(self):
        """Parse addition and subtraction."""
        node = self.term()

        while self.current_token.type in (PLUS, MINUS):
            operator = self.current_token
            self.advance()
            right = self.term()
            node = BinaryOperation(node, operator.type, right)

        return node

    def term(self):
        """Parse multiplication and division before addition and subtraction."""
        node = self.factor()

        while self.current_token.type in (MULTIPLY, DIVIDE):
            operator = self.current_token
            self.advance()
            right = self.factor()
            node = BinaryOperation(node, operator.type, right)

        return node

    def factor(self):
        """Parse a number, variable, or parenthesized expression."""
        token = self.current_token

        if token.type == NUMBER:
            self.advance()
            return Number(token.value)

        if token.type == IDENTIFIER:
            self.advance()
            return Variable(token.value)

        if token.type == LPAREN:
            self.advance()
            node = self.expression()
            if self.current_token.type != RPAREN:
                raise Exception("Missing closing parenthesis")
            self.eat(RPAREN)
            return node

        raise Exception(f"Invalid syntax near {token}")
