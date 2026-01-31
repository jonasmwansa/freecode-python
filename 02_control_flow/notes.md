# Control Flow — FreeCodeCamp Notes

This document covers all the ways Python controls the execution of code: conditionals, loops, and loop control statements.

---

## 1. What is Control Flow?
- Control flow determines the order in which statements are executed
- By default, Python executes code line-by-line from top to bottom
- Control flow structures allow you to make decisions and repeat actions
- Main types: conditionals (if/elif/else) and loops (for/while)

---

## 2. Comparison Operators
Before learning conditionals, understand comparison operators that produce boolean values:

| Operator | Meaning                | Example |
|----------|------------------------|---------|
| `==`     | Equal to               | `5 == 5` → True   |
| `!=`     | Not equal to           | `5 != 3` → True   |
| `<`      | Less than              | `3 < 5` → True    |
| `>`      | Greater than           | `5 > 3` → True    |
| `<=`     | Less than or equal     | `5 <= 5` → True   |
| `>=`     | Greater than or equal  | `5 >= 3` → True   |

Examples:

```python
age = 20
print(age >= 18)  # True
print(age == 20)  # True
print(age != 25)  # True
```

---

## 3. Logical Operators
Combine multiple conditions:

| Operator | Meaning | Example |
|----------|---------|---------|
| `and` | Both conditions true | `5 > 3 and 10 > 5` → True |
| `or` | At least one true | `5 > 10 or 5 > 3` → True |
| `not` | Reverse boolean | `not False` → True |

Examples:

```python
age = 20
has_license = True

can_drive = age >= 18 and has_license
print(can_drive)  # True

is_weekend = False
is_holiday = True

can_relax = is_weekend or is_holiday
print(can_relax)  # True

is_busy = not is_holiday
print(is_busy)  # False
```

---

## 4. Conditional Statements (if/elif/else)

### if statement
Execute code only if a condition is true:

```python
age = 20
if age >= 18:
    print("You are an adult")
```

### if...else statement
Choose between two code blocks:

```python
age = 15
if age >= 18:
    print("You can vote")
else:
    print("You are too young to vote")
```

### if...elif...else statement
Choose among multiple code blocks:

```python
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")
```

### Nested if statements
Conditionals within conditionals:

```python
age = 25
has_license = True

if age >= 18:
    if has_license:
        print("You can drive")
    else:
        print("You need a license")
else:
    print("You are too young to drive")
```

---

## 5. for Loops
Iterate over a sequence (list, string, range, etc.):

### Basic for loop with range()
```python
for i in range(5):  # 0, 1, 2, 3, 4
    print(i)

# range(start, stop, step)
for i in range(1, 10, 2):  # 1, 3, 5, 7, 9
    print(i)
```

### for loop with list
```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

### for loop with string
```python
text = "hello"
for char in text:
    print(char)  # h, e, l, l, o
```

### for loop with enumerate()
Get both index and value:

```python
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
```

### Nested for loops
```python
for i in range(3):
    for j in range(2):
        print(f"({i}, {j})")
```

---

## 6. while Loops
Repeat code while a condition is true:

### Basic while loop
```python
count = 0
while count < 5:
    print(count)
    count += 1  # Important: modify the condition variable
```

### while loop with user input
```python
user_input = ""
while user_input != "quit":
    user_input = input("Enter 'quit' to exit: ")
```

### Infinite loop (use with caution!)
```python
while True:
    user_input = input("Enter a number (or 'exit' to quit): ")
    if user_input == "exit":
        break
```

---

## 7. Loop Control Statements

### break
Exit the loop immediately:

```python
for i in range(10):
    if i == 5:
        break  # Exit loop when i equals 5
    print(i)  # Prints: 0, 1, 2, 3, 4
```

### continue
Skip the current iteration and continue to the next:

```python
for i in range(5):
    if i == 2:
        continue  # Skip when i equals 2
    print(i)  # Prints: 0, 1, 3, 4
```

### else with loops
Code in else block runs if loop completes without break:

```python
for i in range(5):
    if i == 10:
        break
else:
    print("Loop completed without break")  # This prints

# vs
for i in range(5):
    if i == 3:
        break
else:
    print("Loop completed")  # This does NOT print
```

---

## 8. pass Statement
Placeholder when syntax requires a statement but you don't need code:

```python
if age >= 18:
    pass  # Do nothing for now (write code later)
else:
    print("Too young")
```

---

## 9. Ternary Operator (Conditional Expression)
Shorthand for simple if/else:

```python
age = 20
status = "adult" if age >= 18 else "minor"
print(status)  # Output: adult

# General form: value_if_true if condition else value_if_false
```

---

## 10. Common Patterns and Best Practices

### 1. Guard clauses
```python
def process_user(user):
    if user is None:
        return  # Exit early if condition not met
    # Continue with main logic
```

### 2. Avoid deep nesting
```python
# Bad: deeply nested
if condition1:
    if condition2:
        if condition3:
            # action

# Better: combine conditions
if condition1 and condition2 and condition3:
    # action
```

### 3. Use meaningful variable names
```python
# Bad
if x > 18 and y:
    pass

# Good
age = 20
has_license = True
if age >= 18 and has_license:
    print("Can drive")
```

### 4. Avoid infinite loops
```python
# Make sure you modify the loop condition
count = 0
while count < 10:
    print(count)
    count += 1  # Essential!
```

---

## 11. Quick Summary Table

| Structure | Purpose | Example |
|-----------|---------|---------|
| if | Execute if true | `if x > 5:` |
| elif | Execute if previous false and this true | `elif x == 5:` |
| else | Execute if all previous false | `else:` |
| for | Loop over sequence | `for i in range(5):` |
| while | Loop while condition true | `while count < 5:` |
| break | Exit loop | `break` |
| continue | Skip iteration | `continue` |
| pass | Do nothing (placeholder) | `pass` |

---

## 12. Exercises

1. Write a program that checks if a number is positive, negative, or zero
2. Create a multiplication table for numbers 1-10 using nested loops
3. Ask user for password repeatedly until correct (while loop)
4. Find the sum of all numbers from 1 to 100 (for loop)
5. Print numbers 1-20, but skip multiples of 3
6. Create a simple guessing game using conditionals and loops
7. Count down from 10 to 1 using a loop

---

## 13. Teaching Tips
- Always show the importance of proper indentation in Python
- Use flowcharts to visualize conditional logic
- Demonstrate break and continue with practical examples
- Show how to trace through loop iterations step-by-step
- Warn about infinite loops and how to avoid them

---

Happy practicing — control flow is essential for any program! 🐍
