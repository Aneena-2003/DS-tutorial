import tkinter as tk
from tkinter import ttk, messagebox

contacts = []

# ---- Functions ----

def add_contact():
    name = entry_name.get()
    phone = entry_phone.get()
    email = entry_email.get()
    address = entry_address.get()

    if name and phone:
        contacts.append({
            "name": name,
            "phone": phone,
            "email": email,
            "address": address
        })
        messagebox.showinfo("Success", f"Contact {name} added!")
        entry_name.delete(0, tk.END)
        entry_phone.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        entry_address.delete(0, tk.END)
        update_contact_list()
    else:
        messagebox.showwarning("Error", "Name and phone are required!")

def update_contact_list():
    listbox.delete(0, tk.END)
    for contact in contacts:
        listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")

def search_contact():
    keyword = entry_search.get()
    result.delete(1.0, tk.END)
    for contact in contacts:
        if contact["name"] == keyword or contact["phone"] == keyword:
            info = f"Name: {contact['name']}\nPhone: {contact['phone']}\nEmail: {contact['email']}\nAddress: {contact['address']}"
            result.insert(tk.END, info)
            return
    result.insert(tk.END, "Contact not found.")

def update_contact():
    keyword = entry_search.get()
    for contact in contacts:
        if contact["name"] == keyword:
            contact["name"] = entry_new_name.get() or contact["name"]
            contact["phone"] = entry_new_phone.get() or contact["phone"]
            contact["email"] = entry_new_email.get() or contact["email"]
            contact["address"] = entry_new_address.get() or contact["address"]
            messagebox.showinfo("Updated", "Contact updated!")
            update_contact_list()
            return
    messagebox.showinfo("Not Found", "Contact not found!")

def delete_contact():
    keyword = entry_search.get()
    for i, contact in enumerate(contacts):
        if contact["name"] == keyword:
            confirm = messagebox.askyesno("Confirm", f"Delete {contact['name']}?")
            if confirm:
                contacts.pop(i)
                messagebox.showinfo("Deleted", "Contact deleted!")
                update_contact_list()
                return
    messagebox.showinfo("Not Found", "Contact not found!")

# ---- Window ----

root = tk.Tk()
root.title("Contact Book with Tabs")
root.geometry("500x500")

notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand=True)

# ---- Tab 1: Add Contact ----
tab1 = tk.Frame(notebook, bg="#e6f7ff")
notebook.add(tab1, text="Add Contact")

tk.Label(tab1, text="Name:", bg="#e6f7ff").pack(pady=5)
entry_name = tk.Entry(tab1, width=40)
entry_name.pack()

tk.Label(tab1, text="Phone:", bg="#e6f7ff").pack(pady=5)
entry_phone = tk.Entry(tab1, width=40)
entry_phone.pack()

tk.Label(tab1, text="Email:", bg="#e6f7ff").pack(pady=5)
entry_email = tk.Entry(tab1, width=40)
entry_email.pack()

tk.Label(tab1, text="Address:", bg="#e6f7ff").pack(pady=5)
entry_address = tk.Entry(tab1, width=40)
entry_address.pack()

btn_save = tk.Button(tab1, text="Add Contact", bg="#4CAF50", fg="white", command=add_contact)
btn_save.pack(pady=10)

# ---- Tab 2: View Contacts ----
tab2 = tk.Frame(notebook, bg="#f0f8ff")
notebook.add(tab2, text="View Contacts")

listbox = tk.Listbox(tab2, width=50, height=20)
listbox.pack(padx=10, pady=10)

# ---- Tab 3: Search/Update/Delete ----
tab3 = tk.Frame(notebook, bg="#fff0f5")
notebook.add(tab3, text="Search / Update / Delete")

tk.Label(tab3, text="Search by Name or Phone:", bg="#fff0f5").pack(pady=5)
entry_search = tk.Entry(tab3, width=40)
entry_search.pack()

btn_search = tk.Button(tab3, text="Search", bg="#2196F3", fg="white", command=search_contact)
btn_search.pack(pady=5)

result = tk.Text(tab3, width=50, height=5)
result.pack(pady=5)

tk.Label(tab3, text="New Name:", bg="#fff0f5").pack(pady=2)
entry_new_name = tk.Entry(tab3, width=40)
entry_new_name.pack()

tk.Label(tab3, text="New Phone:", bg="#fff0f5").pack(pady=2)
entry_new_phone = tk.Entry(tab3, width=40)
entry_new_phone.pack()

tk.Label(tab3, text="New Email:", bg="#fff0f5").pack(pady=2)
entry_new_email = tk.Entry(tab3, width=40)
entry_new_email.pack()

tk.Label(tab3, text="New Address:", bg="#fff0f5").pack(pady=2)
entry_new_address = tk.Entry(tab3, width=40)
entry_new_address.pack()

btn_update = tk.Button(tab3, text="Update Contact", bg="#FFC107", command=update_contact)
btn_update.pack(pady=5)

btn_delete = tk.Button(tab3, text="Delete Contact", bg="#F44336", fg="white", command=delete_contact)
btn_delete.pack(pady=5)

update_contact_list()

root.mainloop()
