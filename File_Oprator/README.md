# 📓 Journal File Operator

A simple **Python file-handling project** that works like a digital journal. Users can write daily entries, read them, search by keyword, and delete all entries using a menu-driven interface.

This project demonstrates **file I/O, classes, exception handling, and date-time usage** in Python.

---

## ✨ Features
- Add journal entries with **timestamp**
- Read all saved journal entries
- Search for a **specific keyword** inside entries
- Delete all journal entries safely
- Menu-driven console application
- Uses a text file (`journal.txt`) for storage

---

## 🧠 Concepts Used
- **File Handling** (`open`, `read`, `write`, `truncate`)
- **Object-Oriented Programming (OOP)**
- **Date & Time module** (`datetime`)
- **Exception Handling** (`try / except`)
- **String processing** (split, search)
- **While loop & match-case menu**

---

## 📂 File Structure
```
File_oprator.py
journal.txt   (auto-created when first entry is added)
```

---

## ▶️ How the Program Works
When the program starts, you see this menu:

```
1. Add Entry
2. Show all Entry
3. Find Specific Entry
4. Delete all Entries
5. Exit
```

### 📝 1. Add Entry
- User writes a journal entry
- Entry is saved to `journal.txt`
- Each entry is automatically tagged with:
  - Date
  - Time

### 📖 2. Show All Entries
- Displays all journal entries from the file
- Entries are shown in the order they were added

### 🔍 3. Find Specific Entry
- User enters a keyword
- Program searches through all entries
- Displays matching entry if found

### 🗑 4. Delete All Entries
- Asks for confirmation
- Clears all content from `journal.txt`

### 🚪 5. Exit
- Safely exits the application

---

## 🛠 How to Run
1. Make sure Python **3.10+** is installed
2. Save the file as **File_oprator.py**
3. Open terminal / command prompt
4. Run the program:

```bash
python File_oprator.py
```

---

## ⚠️ Notes
- The file `journal.txt` is created automatically
- Searching is **case-sensitive**
- Deleting entries is irreversible

---

## 🚀 Future Improvements
- Case-insensitive search
- Edit individual entries
- Store entries in JSON format
- Add password protection
- Add GUI version

---

## 📜 License
Free to use for learning and educational purposes.

---

⭐ If you like this project, consider adding a ⭐ on GitHub!