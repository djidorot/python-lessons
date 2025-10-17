import tkinter as tk

root = tk.Tk()


def myclick():
    myLabel = tk.Label(root, text="Look, I clicked a button!")
    myLabel.pack()


myButton = tk.Button(root, text="Click me!", command=myclick)
myButton.pack()

root.mainloop()
