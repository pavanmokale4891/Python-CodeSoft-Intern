import tkinter as tk
from tkinter import messagebox
import time

class ToDoListApp:
    def __init__(self, window):
        self.window = window
        self.window.title("To Do List App")

        # Label
        self.label = tk.Label(self.window, text="Enter Task")
        self.label.grid(row=0, column=0)

        # Entry
        self.task_entry = tk.Entry(self.window)
        self.task_entry.grid(row=0, column=1)

        # Add Button
        self.add_button = tk.Button(self.window, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=2)

        # Task Listbox
        self.task_listbox = tk.Listbox(self.window)
        self.task_listbox.grid(row=1, column=0, columnspan=3)

        # Set time
        self.current_time = time.strftime("%H:%M:%S")
        self.timer = self.window.after(1000, self.tick)

    def tick(self):
        next_time = time.strftime("%H:%M:%S")
        if self.current_time != next_time:
            self.current_time = next_time
            if len(self.task_listbox.curselection()) > 0:
                self.notify_task()
        self.timer = self.window.after(1000, self.tick)

    def add_task(self):
        task = self.task_entry.get()
        if task != "":
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)

    def notify_task(self):
        messagebox.showinfo("Reminder", "It's time to work on the selected task.")

def main():
    window = tk.Tk()
    app = ToDoListApp(window)
    window.mainloop()

if __name__ == "__main__":
    main()