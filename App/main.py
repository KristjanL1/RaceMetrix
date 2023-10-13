import tkinter as tk
from gui.laptime_gui import create_gui
from db.laptime_db import init_database

def main():
    root = tk.Tk()
    init_database()

    # Initialize the GUI
    create_gui(root)

    root.mainloop()

if __name__ == "__main__":
    main()




# import sqlite3 as sql

# conn = sql.connect("lap_times.db")
# cursor = conn.cursor()
# cursor.execute('''CREATE TABLE IF NOT EXISTS lap_times (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 track_name TEXT,
#                 lap_time REAL
#                 )''')
# conn.commit()



# # Text Field
# textbox = tk.Text(root, height=3, font=('Arial', 16))
# textbox.pack(padx=10)

# #Single field entry
# myEntry = tk.Entry(root)
# myEntry.pack()

# #Button
# button = tk.Button(root, text="BUTTON!")
# button.pack(padx=10, pady=10)

# #Grid layout frame
# buttonframe = tk.Frame(root)
# gridText = tk.Label(buttonframe, text="Button grid")
# buttonframe.columnconfigure(0, weight=1)
# buttonframe.columnconfigure(1, weight=1)
# buttonframe.columnconfigure(2, weight=1)

# btn1 = tk.Button(buttonframe, text="1")
# btn1.grid(row=0,column=0, sticky=tk.W+tk.E)

# btn2 = tk.Button(buttonframe, text="2")
# btn2.grid(row=0,column=1, sticky=tk.W+tk.E)

# btn3 = tk.Button(buttonframe, text="3")
# btn3.grid(row=0,column=2, sticky=tk.W+tk.E)

# btn4 = tk.Button(buttonframe, text="4")
# btn4.grid(row=1,column=0, sticky=tk.W+tk.E)

# btn5 = tk.Button(buttonframe, text="5")
# btn5.grid(row=1,column=1, sticky=tk.W+tk.E)

# btn6 = tk.Button(buttonframe, text="6")
# btn6.grid(row=1,column=2, sticky=tk.W+tk.E)

# buttonframe.pack(fill='x')

# #.place places button at coordinates
# placebtn = tk.Button(root, text="Yes")
# placebtn.place(x=200, y=200)

