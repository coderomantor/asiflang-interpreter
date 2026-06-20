# Exam Explanation

## Short Introduction

AsifLang is a mini interpreter for a custom language. It was created for a Compiler Construction mini semester project and is named after our teacher, Asif.

It supports only integer numbers, variables, assignment, arithmetic operators, parentheses, and the `show` statement.

## One-Minute Explanation

AsifLang reads source code from a `.asif` file. The lexer converts the code into tokens. The parser checks the grammar and builds an AST. The interpreter executes the AST using a symbol table for variables. Errors such as undefined variables, invalid syntax, unknown characters, and division by zero are shown clearly.

## Compiler Construction Concepts

### 1. Lexical Analysis

The lexer breaks source code into tokens.

Example:

```text
x = 10 + 5
```

Tokens:

```text
IDENTIFIER(x), ASSIGN(=), NUMBER(10), PLUS(+), NUMBER(5)
```

### 2. Syntax Analysis and Parsing

The parser checks whether tokens follow the grammar.

Example valid statement:

```text
x = 10
```

Example invalid statement:

```text
x = 10 +
```

### 3. AST

AST means Abstract Syntax Tree. It is a structured form of the program.

Example:

```text
x = 2 + 3
```

This becomes an assignment node where the expression is a binary operation.

### 4. Interpreter

The interpreter executes the AST.

Example:

```text
x = 10
show x
```

It stores `10` in `x` and prints `10`.

### 5. Symbol Table

The symbol table is a dictionary that stores variable values.

Example:

```text
x = 10
```

Symbol table:

```text
x -> 10
```

### 6. Error Handling

Common errors are shown without long Python tracebacks.

Examples:

```text
Error: Variable not defined: unknown
Error: Division by zero
Error: Missing closing parenthesis
```

## Demo Programs

Basic:

```text
x = 10
y = x + 5
show y
```

Output:

```text
15
```

Arithmetic:

```text
x = 2 + 3 * 4
show x
```

Output:

```text
14
```

Parentheses:

```text
x = (2 + 3) * 4
show x
```

Output:

```text
20
```

## Common Viva Questions

### What is AsifLang?

AsifLang is a small custom language and mini interpreter made for learning Compiler Construction concepts.

### Why is this a Compiler Construction project?

It includes lexical analysis, parsing, AST creation, interpretation, a symbol table, and error handling.

### What is the lexer?

The lexer converts source code into tokens.

### What is the parser?

The parser checks grammar rules and creates the AST.

### What is the AST?

The AST is a tree-like structure that represents the program.

### What is the symbol table?

It is a dictionary that stores variable names and their values.

### What are the limits of AsifLang?

It does not support loops, if-else, functions, strings, arrays, classes, input, comments, or advanced data types.
