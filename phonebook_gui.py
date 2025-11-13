import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
import json
import os

FILE_NAME = "phonebook.json"

# -------------------- Load Data --------------------
def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return {}

phonebook = load_data()

# -------------------- Save Data --------------------
def save_data():
    with open(FILE_NAME, "w") as f:
        json.dump(phonebook, f)

# -------------------- Add Contact --------------------
def add_contact():
    name = name_entry.get().strip()
    number = number_entry.get().strip()

    if not name:
        messagebox.showerror("Error", "Name cannot be empty!")
        return
    if not number.isdigit():
        messagebox.showerror("Error", "Phone number must contain only digits!")
        return
    if name in phonebook:
        messagebox.showerror("Error", "Contact already exists!")
        return

    phonebook[name] = number
    save_data()
    refresh_list()
    clear_inputs()
    messagebox.showinfo("Success", "Contact added successfully!")

# -------------------- Update Contact --------------------
def update_contact():
    name = name_entry.get().strip()
    if name not in phonebook:
        messagebox.showerror("Error", "Contact not found!")
        return

    new_number = number_entry.get().strip()
    if not new_number.isdigit():
        messagebox.showerror("Error", "Invalid number!")
        return

    phonebook[name] = new_number
    save_data()
    refresh_list()
    clear_inputs()
    messagebox.showinfo("Success", "Contact updated!")

# -------------------- Delete Contact --------------------
def delete_contact():
    name = name_entry.get().strip()

    if name in phonebook:
        del phonebook[name]
        save_data()
        refresh_list()
        clear_inputs()
        messagebox.showinfo("Success", "Contact deleted!")
    else:
        messagebox.showerror("Error", "Contact not found!")

# -------------------- Search Contact --------------------
def search_contact():
    keyword = name_entry.get().strip().lower()

    result_list.delete(*result_list.get_children())

    for name, number in phonebook.items():
        if keyword in name.lower():  # partial match
            result_list.insert("", "end", values=(name, number))

# -------------------- List All Contacts --------------------
def refresh_list():
    result_list.delete(*result_list.get_children())

    for name in sorted(phonebook.keys()):
        result_list.insert("", "end", values=(name, phonebook[name]))

# -------------------- Clear Inputs --------------------
def clear_inputs():
    name_entry.delete(0, tk.END)
    number_entry.delete(0, tk.END)

# -------------------- GUI Setup --------------------

root = tk.Tk()
root.title("Phonebook Application")
root.geometry("500x480")
root.resizable(False, False)

# Title
title_label = tk.Label(root, text="Phonebook Application", font=("Arial", 18, "bold"))
title_label.pack(pady=10)

# Frame for inputs
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

tk.Label(input_frame, text="Name:", font=("Arial", 12)).grid(row=0, column=0, padx=5, pady=5)
name_entry = tk.Entry(input_frame, width=30, font=("Arial", 12))
name_entry.grid(row=0, column=1)

tk.Label(input_frame, text="Phone:", font=("Arial", 12)).grid(row=1, column=0, padx=5, pady=5)
number_entry = tk.Entry(input_frame, width=30, font=("Arial", 12))
number_entry.grid(row=1, column=1)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(button_frame, text="Add", width=12, command=add_contact).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Search", width=12, command=search_contact).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Update", width=12, command=update_contact).grid(row=0, column=2, padx=5)
tk.Button(button_frame, text="Delete", width=12, command=delete_contact).grid(row=0, column=3, padx=5)

tk.Button(root, text="Show All Contacts", width=20, command=refresh_list).pack(pady=10)

# Contact list (Table)
columns = ("Name", "Phone")
result_list = ttk.Treeview(root, columns=columns, show="headings", height=12)
result_list.heading("Name", text="Name")
result_list.heading("Phone", text="Phone")
result_list.pack(pady=10)

# Scrollbar
scrollbar = ttk.Scrollbar(root, orient="vertical", command=result_list.yview)
result_list.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side="right", fill="y")

refresh_list()

root.mainloop()
