# Grammar

This is the final grammar of AsifLang.

```text
program -> statement*

statement -> IDENTIFIER "=" expression
           | "show" expression

expression -> term (("+" | "-") term)*

term -> factor (("*" | "/") factor)*

factor -> NUMBER
        | IDENTIFIER
        | "(" expression ")"
```

## Token Types

The lexer creates these token types:

```text
NUMBER       integer number
IDENTIFIER   variable name
SHOW         show keyword
ASSIGN       =
PLUS         +
MINUS        -
MULTIPLY     *
DIVIDE       /
LPAREN       (
RPAREN       )
EOF          end of file
```

## Operator Precedence

Operator priority:

1. Parentheses: `( )`
2. Multiplication and division: `*`, `/`
3. Addition and subtraction: `+`, `-`

Example:

```text
x = 2 + 3 * 4
show x
```

Output:

```text
14
```

With parentheses:

```text
x = (2 + 3) * 4
show x
```

Output:

```text
20
```

## Valid Program

```text
x = 10
y = x + 5
show y
```

## Invalid Examples

```text
show unknown
x = 10 +
show (5 + 2
```
