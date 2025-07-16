# Fuertafit SOS Project

This project was developed as part of a technical test for **Fuertafit**.  
The goal is to implement a function called `can_form_message` that determines whether it is possible to form a message using only the characters available in a chest.

The function must ignore spaces, respect the quantity of each character, and allow any type of character (letters, symbols, numbers, accented letters, etc.).

The project includes:
- The main function (`can_form_message`)
- Unit tests covering basic and advanced cases
- A technical analysis of efficiency, design, and decisions made

## Requirements

This project was developed using:

- **Python 3.10 or higher**
- Visual Studio Code

No external libraries are required.

## Project Structure
```text
├── src/
│ └── check_message.py        # Main logic
├── tests/
│ └── test_check_message.py   # Unit tests
├── README.md                 # Project documentation
├── analysis.md               # Technical analysis
└── .gitignore                # Git exclusions
```
## Installation and Execution

Follow these steps to clone and run the project locally:

### 1. Clone the repository and navigate to the root directory:
```bash
git clone https://github.com/LorelayWilson/fuertafit_check_message
cd fuertafit_check_message
```
### 2. Run the function:
- Make sure you're in the project's root directory.
- Run the following command in the terminal:
```python
python src/check_message.py
```
> To use the function with custom inputs, you can either edit the `check_message.py` file directly or import the function from another script.

## Main Function Behavior

The function `can_form_message(message: str, chest: str) -> tuple[bool, str]` determines whether a message can be formed using only the characters available in a chest.

It returns a tuple:
- A `bool` indicating whether the message can be formed (`True` or `False`)
- An explanatory `str` with the reason (success or the missing characters)

The function includes internal optimizations to improve efficiency when handling very large inputs. Depending on the size of the `message` and `chest`, it dynamically chooses the most efficient strategy:

- If the chest is significantly larger than the message, it only counts relevant characters to avoid unnecessary processing.
- If the message is longer than the chest, it fails early when missing characters are detected.
- If both are of similar size, a balanced approach is used.

This ensures fast and scalable performance even in extreme cases (e.g., long messages or massive character pools).

The implementation is modular and internally structured into helper functions for character filtering, fast scanning, and comparison logic—improving readability and maintainability.

### Rules applied:
- Ignores spaces in both the message and the chest
- Case-insensitive (`a` and `A` are treated the same)
- Accented letters and symbols are not transformed: they are used as-is, and symbols are not ignored
- Respects character count (a letter cannot be used more times than it appears in the chest)
- If the message is empty, it is considered **valid** (no characters required)

### Example usage:
```python
can_form_message("SOS", "PELIGROSOS")
# Resultado: (True, "The message can be formed with the available characters.")

can_form_message("RESCUEA", "RSCU")
# Resultado: (False, "Missing characters: E(2), A(1)")

can_form_message("", "AA")
# Resultado: (True, "Empty message can always be formed.")
```


## Tests
The project includes a set of **unit tests** written using Python’s standard `unittest` module, located in:
```bash
tests/test_check_message.py
```

### What do the tests cover?


- Basic cases of possible and impossible messages
- Ignoring spaces in both the message and the chest
- Use of symbols, numbers, and Unicode characters (like ñ, é, etc.)
- Handling of repeated characters
- Edge cases: empty messages, empty chests, long inputs
- Verification of the explanatory message in the output

### How to run them

1. Make sure you are in the project's root directory.
2. Run the following command in the terminal:
```bash
  python -m unittest discover tests
```
This will automatically run all tests inside the  `tests/` folder.

> The tests are designed to run without requiring any external libraries.

## Author

**Lorelay Pricop Florescu**  
Graduate in Interactive Technologies and Project Manager with experience in .NET, Python, Angular, Azure DevOps, AI, and Agile methodologies.

🔗 [LinkedIn](https://www.linkedin.com/in/lorelaypricop)  
📧 Contact: lorelaypricop@gmail.com

# Notes
> Some ideas regarding validation, style, and structure were reviewed with the support of artificial intelligence (AI) tools, used to help accelerate documentation and validate edge case

