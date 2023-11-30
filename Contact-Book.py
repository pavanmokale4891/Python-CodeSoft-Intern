import tkinter as tk
from tkinter import messagebox

class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")

        # Creating Labels
        self.name_label = tk.Label(self.root, text="Name: ")
        self.number_label = tk.Label(self.root, text="Number: ")
        self.email_label = tk.Label(self.root, text="Email: ")

        # Creating TextBoxes
        self.name_text = tk.Entry(self.root)
        self.number_text = tk.Entry(self.root)
        self.email_text = tk.Entry(self.root)

        # Creating Buttons
        self.add_button = tk.Button(self.root, text="Add Contact", command=self.add_contact)
        self.view_button = tk.Button(self.root, text="View Contact", command=self.view_contact)
        self.search_button = tk.Button(self.root, text="Search Contact", command=self.search_contact)
        self.update_button = tk.Button(self.root, text="Update Contact", command=self.update_contact)
        self.delete_button = tk.Button(self.root, text="Delete Contact", command=self.delete_contact)

        # Creating ListBox
        self.contact_list = tk.Listbox(self.root)

        # Initializing
        self.contacts = {}

        # Placing Elements
        self.name_label.grid(row=0, column=0)
        self.name_text.grid(row=0, column=1)

        self.number_label.grid(row=1, column=0)
        self.number_text.grid(row=1, column=1)

        self.email_label.grid(row=2, column=0)
        self.email_text.grid(row=2, column=1)

        self.add_button.grid(row=3, column=0)
        self.view_button.grid(row=3, column=1)

        self.search_button.grid(row=4, column=0)
        self.update_button.grid(row=4, column=1)

        self.delete_button.grid(row=5, column=0)

        self.contact_list.grid(row=6, column=0, rowspan=6)

    def add_contact(self):
        name = self.name_text.get()
        number = self.number_text.get()
        email = self.email_text.get()

        if name not in self.contacts:
            self.contacts[name] = [number, email]
            self.contact_list.insert(tk.END, name)
            self.name_text.delete(0, tk.END)
            self.number_text.delete(0, tk.END)
            self.email_text.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Contact already exists")

    def view_contact(self):
        name = self.name_text.get()
        if name in self.contacts:
            messagebox.showinfo("Contact Details", "Name: " + name + "\nNumber: " + self.contacts[name][0] + "\nEmail: " + self.contacts[name][1])
        else:
            messagebox.showerror("Error", "Contact does not exist")

    def search_contact(self):
        name = self.name_text.get()
        if name in self.contacts:
            self.contact_list.delete(0, tk.END)
            self.contact_list.insert(tk.END, name)
        else:
            messagebox.showerror("Error", "Contact does not exist")

    def update_contact(self):
        name = self.name_text.get()
        number = self.number_text.get()
        email = self.email_text.get()

        if name in self.contacts:
            self.contacts[name] = [number, email]
            messagebox.showinfo("Updated", "Contact has been updated")
        else:
            messagebox.showerror("Error", "Contact does not exist")

    def delete_contact(self):
        name = self.name_text.get()
        if name in self.contacts:
            del self.contacts[name]
            self.contact_list.delete(0, tk.END)
            self.name_text.delete(0, tk.END)
            self.number_text.delete(0, tk.END)
            self.email_text.delete(0, tk.END)
            messagebox.showinfo("Deleted", "Contact has been deleted")
        else:
            messagebox.showerror("Error", "Contact does not exist")

root = tk.Tk()
contact_book = ContactBook(root)
root.mainloop()