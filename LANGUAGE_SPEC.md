# Language Specification

## Language Name

AsifLang

## Purpose

AsifLang is a small custom language created to demonstrate how an interpreter works. It is designed for students who are learning Compiler Construction.

## Basic Rules

- Each statement is written on a separate line.
- Variable names store integer values.
- Expressions can use integer numbers, variables, arithmetic operators, and parentheses.
- The `show` statement displays the result of an expression.
- The language gives simple error messages for invalid code.

## Variables

Variables are used to store values.

Example:

```text
x = 10
marks = 85
```

Simple variable rules:

- A variable name should start with a letter.
- A variable name can contain letters, digits, and underscores.
- Variable names are case-sensitive.
- A variable must be assigned before it is used.

Valid variable names:

```text
x
total
student_marks
value1
```

Invalid variable names:

```text
1value
total-marks
show
```

## Integer Numbers

AsifLang supports integer numbers only.

Examples:

```text
10
25
0
100
```

Decimal numbers such as `3.5` are not supported.

All values in AsifLang are integers.

## Assignment

Assignment stores the value of an expression in a variable.

Syntax:

```text
variable = expression
```

Example:

```text
total = 10 + 20
```

Required example:

```text
x = 10
```

## Arithmetic Operators

AsifLang supports:

- `+` addition
- `-` subtraction
- `*` multiplication
- `/` division

Example:

```text
result = 10 + 5 * 2
```

Multiplication and division have higher priority than addition and subtraction.

Division is used with integer values. For this mini project, test programs should use simple divisions that divide evenly, such as `20 / 4`.

Valid arithmetic example:

```text
x = 2 + 3 * 4
show x
```

## Parentheses

Parentheses can be used to control the order of calculation.

Example:

```text
result = (10 + 5) * 2
```

Valid parentheses example:

```text
x = (2 + 3) * 4
show x
```

## Show Statement

The `show` statement displays the value of an expression.

Syntax:

```text
show expression
```

Example:

```text
show total
show 10 + 5
```

Valid program example:

```text
x = 10
y = x + 5
show y
```

## Simple Error Messages

AsifLang should show beginner-friendly errors such as:

- `Error: Unknown character`
- `Error: Invalid syntax`
- `Error: Variable not defined`
- `Error: Division by zero`
- `Error: Missing closing parenthesis`

Invalid examples:

```text
show unknown
x = 10 +
show (5 + 2
```

## Not Supported

AsifLang will not support:

- Loops
- If-else
- Functions
- Strings
- Arrays
- Classes
- Input
- Comments
- Advanced data types
