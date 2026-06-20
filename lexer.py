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
    Token,
)


class Lexer:
    """Converts AsifLang source code into tokens."""

    def __init__(self, source_code):
        self.source_code = source_code
        self.position = 0
        self.current_char = self.source_code[self.position] if self.source_code else None

    def advance(self):
        """Move to the next character in the source code."""
        self.position += 1
        if self.position >= len(self.source_code):
            self.current_char = None
        else:
            self.current_char = self.source_code[self.position]

    def tokenize(self):
        """Read the full source code and return a list of tokens."""
        tokens = []

        while self.current_char is not None:
            if self.current_char in " \t\n\r":
                self.advance()
            elif self.current_char.isdigit():
                tokens.append(self.make_number())
            elif self.current_char.isalpha() or self.current_char == "_":
                tokens.append(self.make_identifier())
            elif self.current_char == "=":
                tokens.append(Token(ASSIGN, self.current_char, self.position))
                self.advance()
            elif self.current_char == "+":
                tokens.append(Token(PLUS, self.current_char, self.position))
                self.advance()
            elif self.current_char == "-":
                tokens.append(Token(MINUS, self.current_char, self.position))
                self.advance()
            elif self.current_char == "*":
                tokens.append(Token(MULTIPLY, self.current_char, self.position))
                self.advance()
            elif self.current_char == "/":
                tokens.append(Token(DIVIDE, self.current_char, self.position))
                self.advance()
            elif self.current_char == "(":
                tokens.append(Token(LPAREN, self.current_char, self.position))
                self.advance()
            elif self.current_char == ")":
                tokens.append(Token(RPAREN, self.current_char, self.position))
                self.advance()
            else:
                raise Exception(
                    f"Lexer Error: Unknown character '{self.current_char}' at position {self.position}"
                )

        tokens.append(Token(EOF, position=self.position))
        return tokens

    def make_number(self):
        """Read an integer number."""
        number_text = ""
        start_position = self.position

        while self.current_char is not None and self.current_char.isdigit():
            number_text += self.current_char
            self.advance()

        return Token(NUMBER, int(number_text), start_position)

    def make_identifier(self):
        """Read a variable name or the show keyword."""
        identifier_text = ""
        start_position = self.position

        while (
            self.current_char is not None
            and (self.current_char.isalnum() or self.current_char == "_")
        ):
            identifier_text += self.current_char
            self.advance()

        if identifier_text == "show":
            return Token(SHOW, identifier_text, start_position)

        return Token(IDENTIFIER, identifier_text, start_position)

