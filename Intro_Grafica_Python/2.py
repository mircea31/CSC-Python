# import tkinter as tk
#
# def insert_text():
#     input_text = entry.get()
#     text_widget.insert(tk.END, input_text + "\n")
#
# window = tk.Tk()
# window.title("insert text into text widget")
#

import tkinter   #sau cu as tk sau cu orice alt nume

def insert_text():
    input_text = entry.get()
    text_widget.delete('0', tkinter.END)
    text_widget.insert(tkinter.END, input_text + "\n")

window = tkinter.Tk()
window.title("insert text into text widget")

entry = tkinter.Entry(window)  # Create an Entry widget
entry.pack()

button = tkinter.Button(window, text="Insert", command=insert_text)  # Create a Button widget
def on_enter(e):
    button['background'] = 'green'

def on_leave(e):
    button['background'] = 'red'

button.bind("<Enter>", on_enter)
button.bind("<Leave>", on_leave)

button.pack()

text_widget = tkinter.Entry(window)  # Create a Text widget
text_widget.pack()

window.mainloop()
