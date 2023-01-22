import tkinter as tk

window = tk.Tk()

label1 = tk.Label(window, text="Funny Test")
label2 = tk.Label(window, text="Namey")
label1.grid(row=0, column=0)
label2.grid(row=1, column=1)
window.mainloop()