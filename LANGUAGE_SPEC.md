# Language Specification

## Language Name

AsifLang

## Purpose

AsifLang is a small custom language for learning how interpreters work. It is designed for a Compiler Construction mini semester project.

## Basic Rules

- Each statement is written normally as assignment or `show`.
- Variables store integer values.
- Expressions can use integer numbers, variables, arithmetic operators, and parentheses.
- The `show` statement displays the value of an expression.
- Common mistakes are shown as simple error messages.

## Variables

Variables store integer values.

Examples:

```text
x = 10
total = 25
result = x + total
```

Rules:

- A variable name starts with a letter or underscore.
- A variable name can contain letters, digits, and underscores.
- A variable must be assigned before it is used.
- The keyword `show` is not used as a variable name.

## Integer Numbers

Only integers are supported.

Valid:

```text
10
25
100
```

Not supported:

```text
3.5
```

## Assignment

Assignment stores the result of an expression in a variable.

```text
x = 10
y = x + 5
```

## Arithmetic

Supported operators:

- `+` addition
- `-` subtraction
- `*` multiplication
- `/` integer division

Multiplication and division happen before addition and subtraction.

Example:

```text
x = 2 + 3 * 4
show x
```

Expected output:

```text
14
```

## Parentheses

Parentheses change the order of calculation.

```text
x = (2 + 3) * 4
show x
```

Expected output:

```text
20
```

## Show Statement

The `show` statement prints an expression value.

```text
x = 10
y = x + 5
show y
```

Expected output:

```text
15
```

## Simple Errors

AsifLang handles common errors such as:

- Unknown character
- Invalid syntax
- Missing closing parenthesis
- Variable not defined
- Division by zero
- File not found

Invalid examples:

```text
show unknown
x = 10 +
show (5 + 2
```

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
