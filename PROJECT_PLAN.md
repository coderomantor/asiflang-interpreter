# Project Plan

## Project Title

AsifLang: A Mini Interpreter for a Custom Language

## Project Goal

The goal is to build a small interpreter for a custom language that demonstrates basic compiler construction concepts in a clear and simple way.

## Main Objectives

- Design a small custom language
- Define simple syntax rules
- Create a tokenizer for source code
- Create a parser for statements and expressions
- Execute assignments and arithmetic expressions
- Display output using the `show` statement
- Show simple error messages for invalid programs

## Planned Features

AsifLang will include:

- Variable names such as `x`, `total`, and `marks`
- Number values such as `10`, `25`, and `3.5`
- Assignment using `=`
- Arithmetic using `+`, `-`, `*`, and `/`
- Parentheses for grouping expressions
- Output using `show`

## Features Not Included

AsifLang will not include:

- Conditions such as `if` and `else`
- Loops such as `for` and `while`
- Functions
- Classes or objects
- Strings
- Arrays or lists
- Boolean values
- User input
- File handling
- Advanced error recovery

## Development Phases

### Phase 1: Documentation

- Write project overview
- Define language rules
- Write grammar
- Prepare exam explanation

### Phase 2: Tokenizer

- Read source code
- Convert source code into tokens
- Identify numbers, variables, operators, and keywords

### Phase 3: Parser

- Check the order of tokens
- Parse assignment statements
- Parse `show` statements
- Parse arithmetic expressions

### Phase 4: Interpreter

- Store variable values
- Evaluate expressions
- Execute assignments
- Print values using `show`

### Phase 5: Testing

- Test valid programs
- Test invalid programs
- Check error messages
- Prepare demo examples for exam

## Expected Final Output

At the end of the project, AsifLang should run small programs like:

```text
a = 5
b = 10
show a + b
```

Expected output:

```text
15
```
