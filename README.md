# Python Automation Projects

A collection of practical Python automation projects focused on data cleaning, file handling, and reducing repetitive manual work.

## Projects

### Day 1: Customer Data Cleaning

**Description:** Cleans customer records by removing incomplete records and duplicate email addresses.

**Concepts Used:**

* Python lists and loops
* Conditional statements
* Sets for duplicate detection
* List operations

**File:** `day1.py`

### Day 2: CSV Data Cleaning Automation

**Description:** Reads customer records from a CSV file, removes records with missing emails and duplicate email addresses, and generates a cleaned CSV file.

**Features:**

* Reads CSV files using Python's `csv` module
* Skips the CSV header row
* Removes records with missing email addresses
* Detects duplicate email addresses using a set
* Generates `cleaned_customers.csv`

**Files:**

* `day2.py` — automation script
* `customers.csv` — sample input data
* `cleaned_customers.csv` — cleaned output data

## Technologies Used

* Python
* CSV
* Git and GitHub

## How to Run

1. Install Python.
2. Clone or download this repository.
3. Open the project folder in VS Code.
4. Run the following commands:

```bash
python day1.py
python day2.py
```

The Day 2 script reads `customers.csv` and generates `cleaned_customers.csv`.

## Learning Goals

* Build practical Python automation skills
* Work with files and structured data
* Handle invalid and duplicate records
* Practice writing maintainable code
* Build a portfolio of real-world automation projects

## Author

Shruthi Challa

GitHub: https://github.com/Shruthi-Challa
