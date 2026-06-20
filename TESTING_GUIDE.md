# Testing Guide

This guide explains how to test the finished AsifLang mini interpreter.

## Required Test Commands

```text
python main.py examples/basic.asif
python main.py examples/arithmetic.asif
python main.py examples/errors.asif
python -m py_compile main.py tokens.py lexer.py parser.py ast_nodes.py interpreter.py
```

## Test 1: Basic Program

File:

```text
examples/basic.asif
```

Code:

```text
x = 10
y = x + 5
show y
```

Expected output:

```text
15
```

## Test 2: Arithmetic and Parentheses

File:

```text
examples/arithmetic.asif
```

Code:

```text
x = 2 + 3 * 4
y = (2 + 3) * 4
show x
show y
```

Expected output:

```text
14
20
```

## Test 3: Undefined Variable Error

File:

```text
examples/errors.asif
```

Code:

```text
show unknown
```

Expected output:

```text
Error: Variable not defined: unknown
```

## Other Manual Error Tests

Invalid syntax:

```text
x = 10 +
```

Missing parenthesis:

```text
show (5 + 2
```

Division by zero:

```text
x = 10 / 0
show x
```

Unknown character:

```text
x = 10 @ 5
```

## Checklist

- Lexer creates correct tokens.
- Parser builds an AST from valid code.
- Parser shows clear syntax errors for invalid code.
- Interpreter stores variables in the symbol table.
- Interpreter evaluates arithmetic correctly.
- `show` prints output.
- Undefined variable error is clean.
- Division by zero error is clean.
- Python syntax check passes.
