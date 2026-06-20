# Testing Guide

This guide explains how to test AsifLang after the interpreter is implemented.

## Testing Goal

The goal of testing is to confirm that AsifLang correctly handles valid programs and gives simple error messages for invalid programs.

## Valid Program Tests

### Test 1: Valid Program

Input:

```text
x = 10
y = x + 5
show y
```

Expected output:

```text
15
```

### Test 2: Valid Arithmetic

Input:

```text
x = 2 + 3 * 4
show x
```

Expected output:

```text
14
```

### Test 3: Valid Parentheses

Input:

```text
x = (2 + 3) * 4
show x
```

Expected output:

```text
20
```

### Test 4: Assignment

Input:

```text
x = 10
show x
```

Expected output:

```text
10
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
show unknown
```

Expected error:

```text
Error: Variable not defined
```

### Test 7: Invalid Syntax

Input:

```text
x = 10 +
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
show (5 + 2
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
- Check integer numbers only
- Check parentheses
- Check `show` output
- Check invalid syntax
- Check undefined variables
- Check division by zero
- Check unknown characters
