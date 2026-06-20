from lexer import Lexer


# Sample AsifLang program for testing the lexer only.
source_code = """x = 10
y = x + 5
show y"""

lexer = Lexer(source_code)
tokens = lexer.tokenize()

print("Generated tokens:")
for token in tokens:
    print(token)

