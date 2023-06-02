
def Ex1():
    import tkinter as tk

    window = tk.Tk()

    window.title("Label Example")

    label = tk.Label(window, text="Hello")

    label.pack()

    window.mainloop()

def Ex2():
    import tkinter as tk
    def button_click():
        label.config(text="Button Clicked")

    window = tk.Tk()
    window.geometry('1280x720')
    window.title("button exampleeee")

    label = tk.Label(window, text="press the button")

    label.pack()

    button = tk.Button(window, text = "click me", command=button_click)

    button.pack()
    window.mainloop()

def Ex3():
    import time
    import tkinter as tk

    def center_window(width=300, height=200):
        # get screen width and height
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # calculate position x and y coordinates
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        root.geometry('%dx%d+%d+%d' % (width, height, x, y))

    root = tk.Tk()
    center_window(500, 400)
    time.sleep(5)
    root.mainloop()

def Ex4():
    import time
    import tkinter as tk


    import tkinter as tk
    def button_click():
        def t():
            label.config(text="s-au dus 4 sec")
        label.config(text="Button Clicked")
        #time.sleep(4)
        window.after(4000, t())


    window = tk.Tk()
    window.geometry('1280x720')
    window.title("button exampleeee")

    label = tk.Label(window, text="press the button")

    label.pack()

    button = tk.Button(window, text="click me", command=button_click)

    button.pack()
    window.mainloop()


Ex4()