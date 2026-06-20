# Exam Explanation

## Short Introduction

AsifLang is a mini custom programming language created for our Compiler Construction project. It is named after our teacher, Asif. The language supports integer numbers, variables, assignment, arithmetic expressions, parentheses, and a `show` statement.

## Simple Definition

AsifLang is a mini interpreter. It reads a program written in AsifLang, checks the syntax, evaluates expressions, stores variables, and displays output.

## Why We Made This Project

We made this project to understand how programming languages work internally. Instead of using a full language like Python or Java, we created a small language so that the main compiler construction concepts are easier to understand.

## Main Compiler Construction Concepts Used

### 1. Lexical Analysis

Lexical analysis breaks the source code into small units called tokens.

Example:

```text
x = 10 + 5
```

Tokens:

```text
IDENTIFIER(x), EQUAL(=), NUMBER(10), PLUS(+), NUMBER(5)
```

### 2. Syntax Analysis

Syntax analysis checks whether the tokens follow the grammar rules of the language.

Example of valid syntax:

```text
x = 10
```

Example of invalid syntax:

```text
x = + 10
```

### 3. Parsing

Parsing converts tokens into a structured form that the interpreter can understand. For expressions, parsing also handles operator precedence.

Example:

```text
10 + 5 * 2
```

The parser understands that multiplication happens before addition.

### 4. Interpretation

The interpreter executes the parsed program line by line.

Example:

```text
x = 10
show x
```

The interpreter stores `10` in `x`, then displays `10`.

### 5. Error Handling

The project includes simple error messages to help users understand mistakes.

Examples:

```text
Error: Invalid syntax
Error: Variable not defined
Error: Division by zero
```

## Features Supported

- Integer numbers
- Variables
- Assignment
- Arithmetic operators
- Parentheses
- `show` statement
- Simple error messages

## Features Not Supported

- Loops
- If-else
- Functions
- Strings
- Arrays
- Classes
- Input
- Comments
- Advanced data types

## Sample Demo Program

```text
x = 10
y = x + 5
show y
```

Expected output:

```text
15
```

## More Examples

Valid arithmetic:

```text
x = 2 + 3 * 4
show x
```

Expected output:

```text
14
```

Valid parentheses:

```text
x = (2 + 3) * 4
show x
```

Expected output:

```text
20
```

Invalid examples:

```text
show unknown
x = 10 +
show (5 + 2
```

## One-Minute Viva Answer

AsifLang is a mini interpreter for a custom language. It demonstrates compiler construction concepts such as lexical analysis, syntax analysis, parsing, interpretation, and error handling. The language is small and supports only integer numbers, variables, assignment, arithmetic operations, parentheses, and a `show` statement. We kept the language simple so that the working of each phase can be explained clearly in the exam.
