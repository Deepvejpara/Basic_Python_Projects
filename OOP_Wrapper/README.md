# 🧑‍💼 Python OOP Employee Management System 

A simple Object-Oriented Python project that demonstrates **inheritance, encapsulation, method overriding, and polymorphism** while managing employee data.

This project provides a console-based menu where users can:
- Create Employees
- Assign Departments (Manager role)
- Assign Programming Languages (Developer role)
- Display employee details based on role

---

## ✨ Features
- **OOP Structure** with classes: `Employee`, `Manager`, `Developer`
- **Private attributes** such as `__id` and `__salary`
- **Global list `emp`** to store all employee data
- **Role-based actions** using subclasses
- **Menu-driven interface** with Python's `match-case`
- **Method overriding** in display functions

---

## 🧠 Concepts Demonstrated
### ✔ Encapsulation
Private attributes:
```python
self.__id
self.__salary
```

### ✔ Inheritance
`Manager` and `Developer` inherit from `Employee`.

### ✔ Polymorphism
Both subclasses override the `display()` method.

### ✔ Method Overriding
Each role shows extra data:
- Manager → Department
- Developer → Programming Language

### ✔ Updating Dictionaries
Uses:
```python
employee.update({"dept": dept})
```

---

## 📌 Class Breakdown

### **1️⃣ Employee Class**
Handles:
- Creating employee
- Storing private ID & salary
- Adding entry to global `emp` list
- Displaying basic employee details

### **2️⃣ Manager Class (inherits Employee)**
Adds:
- Assign department to existing employee
- Overrides display to include department

### **3️⃣ Developer Class (inherits Employee)**
Adds:
- Assign programming language
- Overrides display to include language

---

## ▶️ How the Menu Works
The program starts with:
```
1. Create Employee
2. Assign Department
3. Update Programming Languages
4. Show Details
5. Exit
```
You choose an option and the appropriate class method executes.

---

## 🛠 How to Run
1. Install Python 3.10+ (for `match-case` syntax)
2. Save the file as **OOP_Wrapper.py**
3. Run the script:
```bash
python OOP_Wrapper.py
```

---

## 🚀 Future Improvements
- Add file storage (CSV or JSON)
- Add error handling for invalid input
- Add search functionality
- Add UI / GUI version in Tkinter or PyQt
- Remove `global emp` dependency

---

## 📜 License
This project is open-source and free to modify.


