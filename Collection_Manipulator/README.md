# 📘 Student Data Organizer 

A simple Python-based console application to manage and organize student information using lists, sets, and dictionaries.

This project demonstrates basic data collection, CRUD operations, subject handling, and menu-driven programming in Python.

---

## ✨ Features
- Add new students with ID, name, age, grade, birthdate, and subjects
- Display all students in a clean formatted way
- Update student details
- Delete students safely with confirmation
- Maintain a **set** of all unique subjects offered
- User-friendly text‑based menu system

---

## 🧠 Concepts Used
- **Lists** to store multiple student records
- **Dictionaries** to store individual student details
- **Sets** to store unique subjects
- **Loops** & **match-case** for menu navigation
- **Input validation (basic)**

---

## ▶️ How It Works
When the program starts, the user is presented with a menu:

```
1. Add Student
2. Display all Students
3. Update Student Information
4. Delete Student
5. Display Subjects Offered
6. Exit
```

### 📌 1. Add Student
- Enter ID (must be unique)
- Enter name, age, grade
- Enter birthdate (YYYY-MM-DD)
- Enter subjects (comma‑separated)
- Student is added to the list
- Subjects are added to a set

### 📌 2. Display All Students
Shows all registered students in a structured format.
Also displays:
- **Subjects offered** (from set)

### 📌 3. Update Student
Options:
- Update Name
- Update Name & Age
- Update Grade
- Add new Subject

### 📌 4. Delete Student
- Confirms before deletion
- Removes student by ID

### 📌 5. Display Subjects Offered
Shows all unique subjects from the `subjects` set.

### 📌 6. Exit
Gracefully exits the program.

---

## 📎 Code Breakdown
- `students = []` → list of dictionaries storing student entries
- `subjects = set()` → unique subject list
- `match choice:` → clean branch-based menu
- CRUD operations implemented using loops and dictionary updates

---

## 🛠 How to Run
1. Ensure Python 3.10+ is installed (for `match-case` syntax)
2. Save file as **Collection_manipulator.py**
3. Run using:

```
python Collection_manipulator.py
```

---

## 🚀 Future Improvements
- Add search function
- Add validation for wrong input types
- Store data permanently using JSON/CSV
- Add GUI version later

---

## 📜 License
This project is free to use and modify.

---


