import tkinter as tk

root = tk.Tk()

root.geometry("800x500")
root.title("RaceMetrix 0.1 widget testing")

# PAGE LABEL
label = tk.Label(root, text="Welcome to RaceMetrix!", font=('Arial', 18))
label.pack(padx=20, pady=20)

# Text Field
textbox = tk.Text(root, height=3, font=('Arial', 16))
textbox.pack(padx=10)

#Single field entry
myEntry = tk.Entry(root)
myEntry.pack()

#Button
button = tk.Button(root, text="BUTTON!")
button.pack(padx=10, pady=10)

#Grid layout frame
buttonframe = tk.Frame(root)
gridText = tk.Label(buttonframe, text="Button grid")
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)

btn1 = tk.Button(buttonframe, text="1")
btn1.grid(row=0,column=0, sticky=tk.W+tk.E)

btn2 = tk.Button(buttonframe, text="2")
btn2.grid(row=0,column=1, sticky=tk.W+tk.E)

btn3 = tk.Button(buttonframe, text="3")
btn3.grid(row=0,column=2, sticky=tk.W+tk.E)

btn4 = tk.Button(buttonframe, text="4")
btn4.grid(row=1,column=0, sticky=tk.W+tk.E)

btn5 = tk.Button(buttonframe, text="5")
btn5.grid(row=1,column=1, sticky=tk.W+tk.E)

btn6 = tk.Button(buttonframe, text="6")
btn6.grid(row=1,column=2, sticky=tk.W+tk.E)

buttonframe.pack(fill='x')

#Place btn
placebtn = tk.Button(root, text="Yes")
placebtn.place(x=200, y=200)

root.mainloop()

