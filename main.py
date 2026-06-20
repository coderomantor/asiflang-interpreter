import sys

from interpreter import Interpreter
from lexer import Lexer
from parser import Parser


def run_file(file_path):
    """Run one AsifLang source file."""
    try:
        with open(file_path, "r") as file:
            source_code = file.read()

        lexer = Lexer(source_code)
        tokens = lexer.tokenize()

        parser = Parser(tokens)
        program = parser.parse()

        interpreter = Interpreter()
        interpreter.interpret(program)
    except FileNotFoundError:
        print(f"Error: File not found: {file_path}")
    except Exception as error:
        print(f"Error: {error}")


if len(sys.argv) != 2:
    print("Usage: python main.py examples/basic.asif")
else:
    run_file(sys.argv[1])

