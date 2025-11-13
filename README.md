
# Phonebook Application (Python + Tkinter)

A simple and user-friendly **Phonebook Application** built using **Python** and **Tkinter**, with features like adding, searching, updating, and deleting contacts. All contacts are saved automatically using a **JSON file**, making your phonebook persistent across sessions.

## 🚀 Features

### Add New Contact

Create a new contact by entering a name and phone number.

### Update Contact

Modify the phone number of an existing contact.

### Delete Contact

Remove any contact from the phonebook.

### Search Contact (Exact + Partial Search)

Search for a name or even a part of a name (e.g., typing “an” shows *Ananya*, *Rohan*, etc.).

### View All Contacts

Displays all contacts in a sorted table (A → Z).

### Auto Save & Load

Contacts are automatically saved in `phonebook.json` and loaded at start.

### Clean Tkinter GUI

User-friendly interface with text inputs, buttons, and a scrollable table using `ttk.Treeview`.

---

## 🛠 Technologies Used

* **Python 3**
* **Tkinter** (GUI)
* **JSON** (for storage)
* **ttk** (modern widgets)

---

## 📁 Project Structure

```
📦 Phonebook Application
 ┣ 📜 phonebook_gui.py
 ┣ 📜 phonebook.json
 ┗ 📜 README.md
```

---

## ▶️ How to Run the Project

### **1. Clone the Repository**

```bash
git clone https://github.com/palla-vii/Phonebook--Application-Python.git
cd phonebook-app
```

### **2. Run the Application**

Make sure Python is installed, then run:

```bash
python phonebook_gui.py
```

The Tkinter window will open instantly.

---

## 📸 GUI Preview

<img width="740" height="756" alt="image" src="https://github.com/user-attachments/assets/e379d56c-8b62-4b8e-8671-9ed2d2ca5e68" />

## 💾 Data Storage

All contacts are stored in:

```
phonebook.json
```

Example format:

```json
{
  "Riya": "9876543210",
  "Aman": "8765432109"
}
```

---

## ✨ Future Enhancements 

* Dark mode UI
* Adding contact categories (Work, Family, Friends)
* SQLite database integration
* Export contacts to CSV or Excel
* Search-as-you-type live filter
* Packaging the app as an EXE for Windows

---

## 🤝 Contributing

Pull requests are welcome!
For major changes, please open an issue to discuss what you’d like to improve.

---

## 📄 License

This project is open-source under the **MIT License**.

---

