# AsifLang: A Mini Interpreter for a Custom Language

AsifLang is a small educational programming language created for a Compiler Construction mini semester project. It is named after our Compiler Construction teacher, Asif.

The goal is to demonstrate the main parts of a language processor in a simple way: lexer, parser, AST, interpreter, symbol table, and error handling.

## Supported Features

AsifLang supports only:

- Integer numbers
- Variables
- Assignment using `=`
- Arithmetic operators: `+`, `-`, `*`, `/`
- Parentheses: `(` and `)`
- `show` statement
- Simple beginner-friendly error messages

## Unsupported Features

AsifLang does not support:

- Loops
- If-else
- Functions
- Strings
- Arrays
- Classes
- Input
- Comments
- Advanced data types
- GUI, web app, or database

## Example Program

```text
x = 10
y = x + 5
show y
```

Expected output:

```text
15
```

## How To Run

Run an AsifLang file from the command line:

```text
python main.py examples/basic.asif
```

More examples:

```text
python main.py examples/arithmetic.asif
python main.py examples/errors.asif
```

If no file path is provided, the program shows:

```text
Usage: python main.py examples/basic.asif
```

## Project Flow

```text
Source Code
    |
    v
Lexer
    |
    v
Parser
    |
    v
AST
    |
    v
Interpreter
    |
    v
Output
```

## Main Files

- `tokens.py`: token names and `Token` class
- `lexer.py`: converts source code into tokens
- `ast_nodes.py`: AST node classes
- `parser.py`: converts tokens into an AST
- `interpreter.py`: executes the AST
- `main.py`: command-line runner
- `examples/`: sample AsifLang programs

## Why This Is a Compiler Construction Project

This project demonstrates:

- Lexical analysis
- Syntax analysis
- Parsing
- AST construction
- Interpretation
- Symbol table usage
- Error handling

AsifLang is not a full compiler. It is a small interpreter designed for learning and exam explanation.
