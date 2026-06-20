# Token type names used by the AsifLang lexer.
NUMBER = "NUMBER"
IDENTIFIER = "IDENTIFIER"
SHOW = "SHOW"
ASSIGN = "ASSIGN"
PLUS = "PLUS"
MINUS = "MINUS"
MULTIPLY = "MULTIPLY"
DIVIDE = "DIVIDE"
LPAREN = "LPAREN"
RPAREN = "RPAREN"
EOF = "EOF"


class Token:
    """Stores one small piece of AsifLang source code."""

    def __init__(self, token_type, value=None, position=None):
        self.type = token_type
        self.value = value
        self.position = position

    def __repr__(self):
        if self.value is None:
            return self.type
        return f"{self.type}({self.value})"

