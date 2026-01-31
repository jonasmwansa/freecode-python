# Strings — FreeCodeCamp Notes

This document covers core string concepts, idioms, and small examples useful for learning and teaching Python strings.

---

## 1. What is a string?
- A string is an ordered sequence of characters used to represent text.
- In Python, strings are instances of `str` and are immutable (cannot be changed in-place).

Examples:

```python
name = "Alice"
greeting = 'Hello, world!'
multiline = """Line one
Line two
Line three"""
```

---

## 2. Creating strings
- Single quotes: `'text'`
- Double quotes: `"text"`
- Triple quotes: `'''...'''` or `"""..."""` for multi-line strings
- Raw strings: prefix with `r` to avoid escape processing (useful for regex and Windows paths)

Examples:

```python
path = r"C:\Users\Alice\Documents"  # raw string: backslashes preserved
quote = 'He said "Hi" to her'         # mix quotes to avoid escaping
```

---

## 3. Common operations
- Concatenation: `+`
- Repetition: `*`
- Membership test: `in` / `not in`
- Length: `len(s)`
- Indexing: `s[0]`, `s[-1]`
- Slicing: `s[start:stop]`, `s[start:stop:step]`

Examples:

```python
s = "Python"
print(s + " Rocks")      # 'Python Rocks'
print(s * 2)              # 'PythonPython'
print('y' in s)           # True
print(len(s))             # 6
print(s[0], s[-1])        # 'P' 'n'
print(s[1:4])             # 'yth'
```

---

## 4. Immutability
- Strings are immutable. Operations that appear to modify a string return a new string.

```python
s = "cat"
new = s.replace('c', 'b')  # returns 'bat', original `s` unchanged
```

---

## 5. Useful string methods
- `s.upper()`, `s.lower()` — case conversion
- `s.strip()`, `s.rstrip()`, `s.lstrip()` — remove whitespace
- `s.split(sep)` — split into list
- `sep.join(list)` — join list into string
- `s.replace(old, new)` — replace substrings
- `s.find(sub)` / `s.rfind(sub)` — index or -1
- `s.startswith(prefix)` / `s.endswith(suffix)` — boolean checks
- `s.isdigit()`, `s.isalpha()`, `s.isalnum()` — character tests

Examples:

```python
text = "  Hello, Python!  "
print(text.strip())            # 'Hello, Python!'
print(text.upper())            # '  HELLO, PYTHON!  '
parts = text.split(',')        # ['  Hello', ' Python!  ']
joined = ' - '.join(parts)     # '  Hello -  Python!  '
print(text.replace('Python', 'World'))
```

---

## 6. Formatting strings
- f-strings (Python 3.6+): `f"{var} text {expr}"` — preferred for readability and performance
- `str.format()` — `{}`-based formatting
- `%` operator — old-style formatting

Examples:

```python
name = 'Alice'
age = 30
print(f"{name} is {age} years old")             # f-string
print("{} is {}".format(name, age))            # str.format
print("%s is %d" % (name, age))                # %-formatting
```

Formatting with precision and padding:

```python
value = 3.1415926
print(f"Pi: {value:.2f}")       # 'Pi: 3.14'
print(f"{value:08.2f}")         # zero-padded width 8
```

---

## 7. Encoding and bytes
- `str` is text (Unicode). To work with binary data, use `bytes` and encode/decode:

```python
s = "café"
b = s.encode('utf-8')    # bytes
print(b)
print(b.decode('utf-8')) # back to str
```

---

## 8. Common pitfalls and gotchas
- Mixing types in concatenation: `"age: " + 30` raises TypeError — cast with `str()`
- Floating-point formatting: `0.1 + 0.2` may give surprising results — format when printing
- Beware slicing indexes (off-by-one) and negative indices

---

## 9. Small exercises (practice)
1. Create a string containing your full name, then print initials (e.g., "J. D.").
2. Given `date = "2026-01-31"`, extract year, month, day as integers.
3. Split a comma-separated string of numbers and compute their sum.
4. Read a user input phrase and print it reversed.
5. Format a floating price to two decimal places with a leading dollar sign.

---

## 10. Teaching tips
- Encourage experimenting with indexing and slicing in REPL.
- Demonstrate immutability by showing that `replace()` returns a new string.
- Show real-world examples: parsing CSV lines, simple templating with f-strings, file path manipulation.

---

Happy practicing — strings are a fundamental, versatile tool in Python! 🐍
