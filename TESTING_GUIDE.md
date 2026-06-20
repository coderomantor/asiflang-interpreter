# Testing Guide

This guide explains how to test AsifLang after the interpreter is implemented.

## Testing Goal

The goal of testing is to confirm that AsifLang correctly handles valid programs and gives simple error messages for invalid programs.

## Valid Program Tests

### Test 1: Simple Assignment

Input:

```text
x = 10
show x
```

Expected output:

```text
10
```

### Test 2: Addition

Input:

```text
a = 5
b = 7
show a + b
```

Expected output:

```text
12
```

### Test 3: Operator Precedence

Input:

```text
result = 10 + 5 * 2
show result
```

Expected output:

```text
20
```

### Test 4: Parentheses

Input:

```text
result = (10 + 5) * 2
show result
```

Expected output:

```text
30
```

### Test 5: Division

Input:

```text
x = 20 / 4
show x
```

Expected output:

```text
5
```

## Invalid Program Tests

### Test 6: Undefined Variable

Input:

```text
show total
```

Expected error:

```text
Error: Variable not defined
```

### Test 7: Invalid Syntax

Input:

```text
x = + 10
```

Expected error:

```text
Error: Invalid syntax
```

### Test 8: Division by Zero

Input:

```text
x = 10 / 0
show x
```

Expected error:

```text
Error: Division by zero
```

### Test 9: Missing Parenthesis

Input:

```text
x = (10 + 5
show x
```

Expected error:

```text
Error: Missing closing parenthesis
```

### Test 10: Unknown Character

Input:

```text
x = 10 @ 5
```

Expected error:

```text
Error: Unknown character
```

## Manual Testing Checklist

- Check variable assignment
- Check arithmetic operations
- Check parentheses
- Check `show` output
- Check invalid syntax
- Check undefined variables
- Check division by zero
- Check unknown characters
