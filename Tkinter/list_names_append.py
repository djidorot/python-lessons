import tkinter as tk

# Create an empty list
names = []


def add_name():
    name = entry.get().strip()
    if name.lower() == "done":
        result_label.config(text=f"Final list: {names}")
        entry.delete(0, tk.END)
        add_button.config(state="disabled")
        return
    if name:  # avoid adding empty names
        names.append(name)
        listbox.insert(tk.END, name)
        entry.delete(0, tk.END)


# Create main window
root = tk.Tk()
root.title("Name Collector")

# Input field
entry = tk.Entry(root, width=30)
entry.pack(pady=5)

# Add button
add_button = tk.Button(root, text="Add Name", command=add_name)
add_button.pack(pady=5)

# Listbox to show names
listbox = tk.Listbox(root, width=40, height=8)
listbox.pack(pady=5)

# Label to show result after "done"
result_label = tk.Label(root, text="")
result_label.pack(pady=5)

root.mainloop()
