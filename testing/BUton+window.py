import tkinter as tk

window = tk.Tk()

window.title("Label Example")

label = tk.Label(window, text="Hello")

label.pack()

window.mainloop()

def button_click():
    label.config(text="Button Clicked")

window = tk.Tk()

window.title("button exampleeee")

label = tk.Label(window, text="press the button")

label.pack()

button = tk.Button(window, text = "click me", command=button_click)
button.pack()
window.mainloop()