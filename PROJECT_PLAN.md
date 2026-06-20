# Project Plan

## Project Title

AsifLang: A Mini Interpreter for a Custom Language

## Goal

Build a small interpreter that demonstrates compiler construction concepts while staying simple enough for students to explain in viva or exam.

## Final Features

AsifLang includes only:

- Integer numbers
- Variables
- Assignment
- Arithmetic operators
- Parentheses
- `show` statement
- Simple error messages

## Not Included

AsifLang does not include loops, if-else, functions, strings, arrays, classes, input, comments, advanced data types, GUI, web app, or database.

## Completed Parts

### 1. Documentation

The project has documentation for language rules, grammar, testing, team explanation, and exam preparation.

### 2. Lexer

The lexer reads source code and converts it into tokens such as `IDENTIFIER`, `NUMBER`, `ASSIGN`, and `SHOW`.

### 3. Parser

The parser checks token order using grammar rules and builds an AST. It handles assignment statements, `show` statements, arithmetic expressions, and parentheses.

### 4. AST

The AST represents the program in a simple structured form using nodes such as `Program`, `Assignment`, `Show`, `Number`, `Variable`, and `BinaryOperation`.

### 5. Interpreter

The interpreter executes the AST. It stores variables in a symbol table, evaluates expressions, and prints output for `show`.

### 6. Testing

The examples in the `examples/` folder test valid programs and simple errors.

## Expected Demo Commands

```text
python main.py examples/basic.asif
python main.py examples/arithmetic.asif
python main.py examples/errors.asif
python -m py_compile main.py tokens.py lexer.py parser.py ast_nodes.py interpreter.py
```
