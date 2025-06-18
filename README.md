
# Fruit Basket Report

This project is a CLI-based Python program that analyzes a CSV file containing fruit data and produces a summary report.

---

## Features

- Accepts a fruit CSV file as input via command line
- Validates and cleans input data
- Computes:
  - Total number of fruits
  - Number of unique fruit types
  - Count of each fruit type (descending order)
  - Characteristics (color and shape) by fruit type
  - Identifies fruits that have been in the basket for more than 3 days
- Output is clear and formatted, e.g.:
  ```
  Have any fruit been in the basket for over 3 days
  4 oranges and 5 pineapples are over 3 days old
  ```

---

## Usage

```bash
python fruit_basket_solution.py <basket.csv>
```

**Example:**
```bash
python fruit_basket_solution.py test_data/valid_basic.csv
```

---

## Test Files (Located in `test_data/`)

| File                    | Purpose                              |
|-------------------------|--------------------------------------|
| `basket.csv`            | valid input coding challenge example |
| `missing_columns.csv`   | Tests missing column handling        |
| `malformed_values.csv`  | Tests non-numeric values             |
| `all_old_fruits.csv`    | All fruits aged over 3 days          |
| `empty_file.csv`        | Tests empty file edge case           |

---

## Requirements

- Python 3.6+
- pandas

Install dependencies with:

```bash
pip install pandas
```

---

## Project Structure

```
fruit_basket_project/
├── src/
│   └── fruit_basket_solution.py
├── test_data/
│   ├── valid_basic.csv
│   ├── missing_columns.csv
│   ├── malformed_values.csv
│   ├── all_old_fruits.csv
│   └── empty_file.csv
└── README.md
```
