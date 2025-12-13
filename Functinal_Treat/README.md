# 🧮 Functional Treat — Data Analyzer & Transformer (Python)

A menu-driven Python program that demonstrates **functional programming concepts** and **basic data analysis** on a 1D numeric dataset.

This project is designed for learning and practicing:
- Functions
- Recursion
- Lambda functions
- Built-in functions
- Returning multiple values

---

## ✨ Features
- Input and store 1D numeric data
- Display summary using **built-in functions**
- Calculate factorial using **recursion**
- Filter data using **lambda & filter()**
- Sort data (ascending / descending)
- Calculate statistics without built-in functions
- Interactive menu-based interface

---

## 🧠 Concepts Demonstrated
- **Functional Programming** in Python
- **Recursion** (`factorial()`)
- **Lambda Functions** (`filter()`)
- **Built-in Functions** (`sum`, `min`, `max`, `len`)
- **User-defined Functions**
- **Returning multiple values from a function**
- **List manipulation**

---

## ▶️ Program Menu
```
1. Input Data
2. Display Data Summary (Built-in Functions)
3. Calculate Factorial (Recursion)
4. Filter Data by Threshold (Lambda Function)
5. Sort Data
6. Display Dataset Statistics (Return Multiple Values)
7. Exit Program
```

---

## 📌 Function Overview

### 🔹 Create()
- Accepts space-separated integers
- Stores them in a global list

### 🔹 Summary()
Displays:
- Total elements
- Minimum & Maximum values
- Sum & Average (using built-in functions)

### 🔹 factorial(n)
- Recursive function
- Calculates factorial of a number

### 🔹 lambda_filter(n)
- Uses `lambda` with `filter()`
- Returns values greater than threshold

### 🔹 sorting()
- Sorts data in ascending or descending order

### 🔹 stat()
- Calculates sum, mean, max, min **without built-in functions**
- Returns multiple values

---

## 🛠 How to Run
1. Make sure Python **3.10+** is installed
2. Save the file as **Functional_Treat.py**
3. Run the program:

```bash
python Functional_Treat.py
```

---

## ⚠️ Notes
- Input must contain only integers
- Dataset must be entered before other operations
- Program uses a global list for simplicity

---

## 🚀 Future Improvements
- Add input validation
- Support floating-point numbers
- Add file input/output
- Remove global variables
- Convert to modular structure

---

## 📜 License
Free to use for educational and learning purposes.

---

⭐ If you find this helpful, consider giving the repository a ⭐ on GitHub!