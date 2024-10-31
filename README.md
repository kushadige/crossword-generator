# Crossword Puzzle Generator

Generates all possible crossword puzzles from a given list of words. It uses backtracking algorithm and generator functions to generate possible puzzles.

---

## Examples

### Terminal Renderer

<img width="1193" alt="image" src="https://github.com/user-attachments/assets/144fbb90-c17e-46bc-983d-8b2c46d4e202">

### Pygame Renderer

<img width="912" alt="image" src="https://github.com/user-attachments/assets/3785593d-7ea9-4167-9bab-46a0eaf3832e">

---

## Installation

```bash
git clone https://github.com/kushadige/crossword-generator.git
```

```bash
cd crossword-generator
```

### Virtual Environment Setup

#### Create

```bash
python3 -m venv venv
```

#### Activate

```bash
- MacOS/Linux

source venv/bin/activate
```

```bash
- Windows

venv\Scripts\activate
```

#### Install Dependencies

```bash
pip3 install -r requirements.txt
```

---

## Usage

### 1. Use default CLI

Run the application without any arguments to use the default CLI. It will prompt you to enter the words manually.

```bash
python3 main.py
```

### 2. Provide file input

You can provide a file containing the list of words using the `-f` flag.

```bash
python3 main.py -f data/wordlist.txt -r pygame
```

### 3. Specify renderer type

You can specify the rendering type using the `-r` flag. The available options are `pygame` or `terminal`. (default: `terminal`)

```bash
python3 main.py -f data/wordlist.txt -r pygame
```

---

## Author

[oguzhankuslar](https://github.com/kushadige)
