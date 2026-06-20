# Team Guide

This guide helps team members understand the AsifLang project.

## Project Summary

AsifLang is a mini interpreter for a small custom language. It is made for learning Compiler Construction concepts.

The language is intentionally simple. It only supports variables, numbers, assignment, arithmetic expressions, parentheses, and the `show` statement.

## What Every Team Member Should Understand

Every team member should be able to explain:

- What AsifLang is
- Why it is related to Compiler Construction
- What features the language supports
- What features the language does not support
- How a source program is converted into tokens
- How grammar is used to check syntax
- How expressions are evaluated
- How variables are stored
- How simple errors are displayed

## Main Parts of the Project

### 1. Language Design

This part defines the rules of AsifLang.

Example:

```text
x = 10
show x
```

### 2. Tokenizer

The tokenizer reads source code and breaks it into tokens.

Example:

```text
x = 10
```

Tokens:

```text
IDENTIFIER, EQUAL, NUMBER
```

### 3. Parser

The parser checks if tokens follow the grammar.

Example grammar idea:

```text
assignment -> IDENTIFIER "=" expression
```

### 4. Interpreter

The interpreter runs the program.

Example:

```text
x = 10
show x
```

It stores `10` in `x` and displays `10`.

### 5. Error Handling

The interpreter should show simple errors for mistakes.

Example:

```text
show x
```

If `x` was not assigned before, the output should be:

```text
Error: Variable not defined
```

## Suggested Team Roles

- Documentation member: explains project idea, language rules, and exam notes
- Tokenizer member: explains how source code becomes tokens
- Parser member: explains grammar and syntax checking
- Interpreter member: explains execution and variable storage
- Testing member: explains valid and invalid test cases

## How to Prepare for Exam

- Read `README.md` first
- Read `LANGUAGE_SPEC.md` to understand language rules
- Read `GRAMMAR.md` to understand syntax
- Read `EXAM_EXPLANATION.md` for viva answers
- Practice explaining the sample programs
- Practice drawing the flow: source code to tokens to parser to interpreter to output

## Simple Project Flow

```text
Source Code
    |
    v
Tokenizer
    |
    v
Parser
    |
    v
Interpreter
    |
    v
Output
```

## Important Reminder

Do not add advanced features unless the teacher asks for them. A small and clear project is easier to explain than a large and confusing project.
