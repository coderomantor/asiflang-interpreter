# Grammar

This file defines the simple grammar of AsifLang.

## Informal Grammar

An AsifLang program is made of multiple statements.

A statement can be:

- An assignment statement
- A `show` statement

Expressions can contain:

- Numbers
- Variables
- Arithmetic operators
- Parentheses

## Grammar Rules

```text
program        -> statement*

statement      -> assignment
                | show_statement

assignment     -> IDENTIFIER "=" expression

show_statement -> "show" expression

expression     -> term (("+" | "-") term)*

term           -> factor (("*" | "/") factor)*

factor         -> NUMBER
                | IDENTIFIER
                | "(" expression ")"
```

## Token Types

The tokenizer will identify these token types:

```text
NUMBER       numeric value
IDENTIFIER   variable name
SHOW         show keyword
PLUS         +
MINUS        -
STAR         *
SLASH        /
EQUAL        =
LPAREN       (
RPAREN       )
NEWLINE      end of statement
EOF          end of file
```

## Operator Precedence

Operator priority from highest to lowest:

1. Parentheses: `( )`
2. Multiplication and division: `*`, `/`
3. Addition and subtraction: `+`, `-`

Example:

```text
result = 10 + 5 * 2
```

This is interpreted as:

```text
result = 10 + (5 * 2)
```

So the result is:

```text
20
```

## Statement Examples

Assignment:

```text
x = 10
```

Show statement:

```text
show x
```

Expression:

```text
(10 + 5) * 2
```

