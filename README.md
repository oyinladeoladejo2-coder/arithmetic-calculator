# arithmetic-calculator
#A simple Python program that performs basic arithmetic calculations.

A simple desktop calculator built with Python's built-in `tkinter` library. It supports basic arithmetic, keyboard input, and a clean button-based interface.

## Features

- Basic operations: addition, subtraction, multiplication, division
- Clear (`C`) and backspace (`⌫`) buttons
- Decimal point support
- Keyboard support — type numbers/operators, press `Enter` to evaluate, `Backspace` to delete, `Esc` to clear
- Error handling for invalid expressions (e.g. dividing by zero)

## Requirements

- Python 3.x
- `tkinter` (included with most standard Python installations)

## How to Run

\`\`\`bash
python calculator.py
\`\`\`

> Make sure the file is named `calculator.py` (or update the command above to match your filename).

## Usage

- Click the number and operator buttons to build an expression, then press `=` to evaluate.
- Or use your keyboard:
  - `0-9`, `.`, `+`, `-`, `*`, `/` — enter numbers and operators
  - `Enter` — evaluate the expression
  - `Backspace` — delete the last character
  - `Esc` — clear the display

## How It Works

The calculator keeps the current expression as a string and uses Python's `eval()` to compute the result when `=` is pressed. Invalid expressions are caught and displayed as `Error`.

## Possible Improvements

- Replace `eval()` with a safer expression parser
- Add support for parentheses and scientific functions (sqrt, powers, etc.)
- Add unit tests
- Package as a standalone executable

## License

Feel free to use and modify this project for learning purposes.
