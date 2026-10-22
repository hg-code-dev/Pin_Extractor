# PIN Extractor

A Python project completed as part of my FreeCodeCamp Python learning journey.

## Overview

This program extracts a secret PIN code from one or more poems. It works by analysing the structure of each poem and creating a code based on the lengths of selected words from each line.

For every line in a poem:

- Line 1 uses the first word.
- Line 2 uses the second word.
- Line 3 uses the third word.
- And so on.

The length of each selected word is added to create a secret code.

If a line does not contain a word at the required position, the program adds `0` instead.

## Example

### Input

```python
poem = """Stars and the moon
shine in the sky
white and
until the end of the night"""
```

### Output

```python
['5202']
```

### Explanation

| Line | Selected Word | Length |
|------|--------------|---------|
| Stars and the moon | Stars | 5 |
| shine in the sky | in | 2 |
| white and | No 3rd word | 0 |
| until the end of the night | of | 2 |

Resulting PIN: `5202`

## Features

- Processes multiple poems at once.
- Uses loops and conditional logic.
- Handles missing words gracefully by inserting `0`.
- Returns a list of secret codes.

## Skills Practised

- Python functions
- Lists
- String manipulation
- Nested loops
- Conditional statements
- The `enumerate()` function
- Working with multiline strings

## How to Run

1. Clone this repository:

```bash
git clone https://github.com/your-username/pin-extractor.git
```

2. Navigate to the project folder:

```bash
cd pin-extractor
```

3. Run the script:

```bash
python main.py
```

## Sample Output

```python
['5202', '5336', '511010']
```

## Learning Journey

This project was completed while studying Python through FreeCodeCamp. It helped reinforce concepts such as iteration, string processing, indexing, and problem-solving through code.
