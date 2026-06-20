# Team Guide

This guide helps team members understand and explain AsifLang.

## Project Summary

AsifLang is a small interpreter for a custom language. It is designed for a Compiler Construction mini semester project.

The language supports only integer numbers, variables, assignment, arithmetic operators, parentheses, and `show`.

## Project Parts

### 1. Language Rules

The language rules define what AsifLang supports.

Example:

```text
x = 10
show x
```

### 2. Lexer

File:

```text
lexer.py
```

The lexer converts source code into tokens.

Example:

```text
x = 10
```

Tokens:

```text
IDENTIFIER(x), ASSIGN(=), NUMBER(10)
```

### 3. Parser

File:

```text
parser.py
```

The parser checks grammar rules and builds the AST. It also handles operator precedence, so `*` and `/` happen before `+` and `-`.

### 4. AST

File:

```text
ast_nodes.py
```

The AST represents the program using simple node classes:

- `Program`
- `Assignment`
- `Show`
- `Number`
- `Variable`
- `BinaryOperation`

### 5. Interpreter

File:

```text
interpreter.py
```

The interpreter executes the AST. It stores variable values, evaluates expressions, and prints output for `show`.

### 6. Symbol Table

The symbol table is a Python dictionary.

Example after `x = 10`:

```text
{"x": 10}
```

### 7. Main Program

File:

```text
main.py
```

This file reads an AsifLang file and runs:

```text
Lexer -> Parser -> Interpreter
```

## How To Run

```text
python main.py examples/basic.asif
python main.py examples/arithmetic.asif
python main.py examples/errors.asif
```

## What Each Team Member Should Explain

- What AsifLang is
- Supported and unsupported features
- How source code becomes tokens
- How parser checks grammar
- What AST means
- How interpreter executes statements
- How the symbol table stores variables
- What errors are handled

## Important Scope Reminder

Do not add loops, if-else, functions, strings, arrays, classes, input, comments, GUI, web app, database, or advanced data types. The strength of this project is that it is small and easy to explain.
