"""
Topic: 03_slicing
Source: freeCodeCamp Python

This file demonstrates string slicing and indexing in Python.
Strings are sequences, so they support indexing and slicing operations.
"""

# ============================================================================
# BASIC INDEXING
# ============================================================================

print("=== BASIC INDEXING ===\n")

text = "Python"

# Positive indexing (from left, 0-based)
print(f"Text: {text}")
print(f"text[0] = '{text[0]}'  (first character)")
print(f"text[1] = '{text[1]}'")
print(f"text[2] = '{text[2]}'")
print(f"text[5] = '{text[5]}'  (last character)")

# Negative indexing (from right)
print(f"\nNegative indexing:")
print(f"text[-1] = '{text[-1]}'  (last character)")
print(f"text[-2] = '{text[-2]}'  (second to last)")
print(f"text[-6] = '{text[-6]}'  (first character)")

# Index out of range raises error
try:
    print(text[10])
except IndexError as e:
    print(f"\ntext[10] raises IndexError: {e}")
print()


# ============================================================================
# BASIC SLICING: [start:stop]
# ============================================================================

print("=== BASIC SLICING [start:stop] ===\n")

text = "Hello, World!"
print(f"Text: {text}")

# From start to index 5 (not including 5)
print(f"text[0:5] = '{text[0:5]}'")

# From index 7 to 12
print(f"text[7:12] = '{text[7:12]}'")

# From beginning to index 5
print(f"text[:5] = '{text[:5]}'  (omit start)")

# From index 7 to end
print(f"text[7:] = '{text[7:]}'  (omit stop)")

# Entire string
print(f"text[:] = '{text[:]}'  (omit both)")

# Negative indices in slicing
print(f"text[-6:-1] = '{text[-6:-1]}'  (last 5 chars, excluding last)")
print()


# ============================================================================
# SLICING WITH STEP: [start:stop:step]
# ============================================================================

print("=== SLICING WITH STEP [start:stop:step] ===\n")

text = "Python Programming"
print(f"Text: {text}")

# Every 2nd character
print(f"text[::2] = '{text[::2]}'  (every 2nd char)")

# Every 3rd character
print(f"text[::3] = '{text[::3]}'  (every 3rd char)")

# Characters from index 0 to 6, every 2nd
print(f"text[0:6:2] = '{text[0:6:2]}'")

# Reverse string (step = -1)
print(f"text[::-1] = '{text[::-1]}'  (reversed)")

# Reverse from index 6 to 0
print(f"text[6:0:-1] = '{text[6:0:-1]}'  (partial reverse)")

# Every 2nd character in reverse
print(f"text[::-2] = '{text[::-2]}'  (reversed, every 2nd)")
print()


# ============================================================================
# PRACTICE EXAMPLE 1: EXTRACT PARTS OF A STRING
# ============================================================================

print("=== PRACTICE 1: STRING PARTS ===\n")

sentence = "The quick brown fox"
print(f"Original: {sentence}")

# First word
first_word = sentence[:3]
print(f"First word: '{first_word}'")

# Last word
last_word = sentence[-3:]
print(f"Last word: '{last_word}'")

# Middle part
middle = sentence[4:9]
print(f"Middle part: '{middle}'")

# First 3 words
first_three = sentence[:13]
print(f"First 3 words: '{first_three}'")
print()


# ============================================================================
# PRACTICE EXAMPLE 2: EMAIL PARSING
# ============================================================================

print("=== PRACTICE 2: EMAIL PARSING ===\n")

email = "john.doe@example.com"
print(f"Email: {email}")

# Extract username (before @)
at_index = email.find('@')
username = email[:at_index]
print(f"Username: {username}")

# Extract domain (after @)
domain = email[at_index + 1:]
print(f"Domain: {domain}")

# Extract extension (after last .)
dot_index = email.rfind('.')
extension = email[dot_index + 1:]
print(f"Extension: {extension}")
print()


# ============================================================================
# PRACTICE EXAMPLE 3: PHONE NUMBER FORMATTING
# ============================================================================

print("=== PRACTICE 3: PHONE NUMBER ===\n")

phone = "5551234567"
print(f"Raw: {phone}")

# Format as (555) 123-4567
formatted = f"({phone[:3]}) {phone[3:6]}-{phone[6:]}"
print(f"Formatted: {formatted}")

# Extract area code
area_code = phone[:3]
print(f"Area code: {area_code}")

# Extract exchange
exchange = phone[3:6]
print(f"Exchange: {exchange}")

# Extract line number
line_number = phone[6:]
print(f"Line number: {line_number}")
print()


# ============================================================================
# PRACTICE EXAMPLE 4: DATE PARSING
# ============================================================================

print("=== PRACTICE 4: DATE PARSING ===\n")

date = "2026-02-01"
print(f"Date: {date}")

# Extract year, month, day
year = date[:4]
month = date[5:7]
day = date[8:]
print(f"Year: {year}")
print(f"Month: {month}")
print(f"Day: {day}")

# Reverse date format
reversed_date = f"{day}/{month}/{year}"
print(f"Reversed format: {reversed_date}")

# Alternative format
alt_date = f"{day}-{month}-{year}"
print(f"Alternative format: {alt_date}")
print()


# ============================================================================
# PRACTICE EXAMPLE 5: DNA SEQUENCE OPERATIONS
# ============================================================================

print("=== PRACTICE 5: DNA SEQUENCE ===\n")

dna = "ATCGATCGATCG"
print(f"DNA: {dna}")

# First 4 nucleotides (codon)
first_codon = dna[:3]
print(f"First codon: {first_codon}")

# Last 4 nucleotides
last_codon = dna[-3:]
print(f"Last codon: {last_codon}")

# Every 3rd nucleotide (codons)
codons = dna[::3]
print(f"Codons (every 3rd): {codons}")

# Reverse complement would need replacement, but reverse:
reversed_dna = dna[::-1]
print(f"Reversed: {reversed_dna}")

# Middle section
middle_section = dna[3:9]
print(f"Middle section: {middle_section}")
print()


# ============================================================================
# PRACTICE EXAMPLE 6: URL PARSING
# ============================================================================

print("=== PRACTICE 6: URL PARSING ===\n")

url = "https://www.example.com/path/to/page"
print(f"URL: {url}")

# Extract protocol
protocol_end = url.find("://")
protocol = url[:protocol_end]
print(f"Protocol: {protocol}")

# Extract domain
domain_start = protocol_end + 3
domain_end = url.find("/", domain_start)
domain = url[domain_start:domain_end]
print(f"Domain: {domain}")

# Extract path
path = url[domain_end:]
print(f"Path: {path}")

# Get page name (last part of path)
page = url.split("/")[-1]
print(f"Page: {page}")
print()


# ============================================================================
# PRACTICE EXAMPLE 7: TEXT TRUNCATION
# ============================================================================

print("=== PRACTICE 7: TEXT TRUNCATION ===\n")

long_text = "The quick brown fox jumps over the lazy dog and continues to run"
max_length = 20

print(f"Original: {long_text}")
print(f"Length: {len(long_text)}")

# Truncate and add ellipsis
if len(long_text) > max_length:
    truncated = long_text[:max_length - 3] + "..."
    print(f"Truncated: {truncated}")
    print(f"Length: {len(truncated)}")

# Find last space within limit
text_to_truncate = long_text[:max_length]
last_space = text_to_truncate.rfind(" ")
if last_space != -1:
    smart_truncate = long_text[:last_space] + "..."
    print(f"Smart truncated: {smart_truncate}")
print()


# ============================================================================
# PRACTICE EXAMPLE 8: PALINDROME CHECK
# ============================================================================

print("=== PRACTICE 8: PALINDROME CHECK ===\n")

words = ["racecar", "hello", "noon", "python", "madam"]

for word in words:
    reversed_word = word[::-1]
    is_palindrome = word == reversed_word
    print(f"'{word}' reversed: '{reversed_word}' -> Palindrome: {is_palindrome}")
print()


# ============================================================================
# PRACTICE EXAMPLE 9: EVERY NTH CHARACTER
# ============================================================================

print("=== PRACTICE 9: EVERY NTH CHARACTER ===\n")

text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(f"Text: {text}")

# Every 2nd character
every_2nd = text[::2]
print(f"Every 2nd: {every_2nd}")

# Every 3rd character
every_3rd = text[::3]
print(f"Every 3rd: {every_3rd}")

# Every 5th character
every_5th = text[::5]
print(f"Every 5th: {every_5th}")

# Start from index 1, every 2nd
from_1_every_2 = text[1::2]
print(f"Start from 1, every 2nd: {from_1_every_2}")
print()


# ============================================================================
# PRACTICE EXAMPLE 10: STRING REVERSAL AND MANIPULATION
# ============================================================================

print("=== PRACTICE 10: STRING MANIPULATION ===\n")

text = "Hello"
print(f"Original: {text}")
print(f"Reversed: {text[::-1]}")
print(f"First half: {text[:len(text)//2]}")
print(f"Second half: {text[len(text)//2:]}")

# Swap first and last characters
swapped = text[-1] + text[1:-1] + text[0]
print(f"Swap first/last: {swapped}")

# Create acronym (every first letter)
phrase = "As Soon As Possible"
acronym = "".join([word[0] for word in phrase.split()])
print(f"\nPhrase: {phrase}")
print(f"Acronym: {acronym}")
print()


# ============================================================================
# SLICING EDGE CASES
# ============================================================================

print("=== EDGE CASES ===\n")

text = "Python"
print(f"Text: {text}")

# Slicing with out-of-range indices (doesn't raise error)
print(f"text[0:100] = '{text[0:100]}'  (stop beyond length)")
print(f"text[-100:3] = '{text[-100:3]}'  (start before beginning)")
print(f"text[100:200] = '{text[100:200]}'  (both out of range)")

# Empty slices
print(f"text[3:3] = '{text[3:3]}'  (same start and stop)")
print(f"text[5:2] = '{text[5:2]}'  (start > stop, normal order)")
print(f"text[5:2:-1] = '{text[5:2:-1]}'  (start > stop, reverse)")
print()


# ============================================================================
# QUICK CHALLENGES
# ============================================================================

print("=== CHALLENGES ===")
print("1) Given 'abcdefgh', extract 'bcd' (middle 3 chars starting from index 1).")
print("2) Reverse a word without using any built-in reverse function.")
print("3) Extract every vowel from a sentence using slicing and iteration.")
print("4) Given a sentence, get the first and last character without separate indexing.")
print("5) Create a function that returns the last N characters of any string.")
print("\nTry implementing these!\n")

print("=== END OF SLICING EXAMPLES ===")
