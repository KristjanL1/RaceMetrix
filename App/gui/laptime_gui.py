import tkinter as tk
from exec.laptime_handler import save_lap_time, display_lap_times

def create_gui(root):
    root.geometry("800x500")
    root.title("RaceMetrix 0.1 widget testing")

    # PAGE LABEL
    label = tk.Label(root, text="Welcome to RaceMetrix!", font=('Arial', 18))
    label.pack(padx=20, pady=20)

    # Entry Fields
    driver_name_label = tk.Label(root, text="Your Name:")
    driver_name_label.pack(padx=10, pady=5)
    driver_name_entry = tk.Entry(root)
    driver_name_entry.pack(padx=10, pady=5)

    track_name_label = tk.Label(root, text="Track Name:")
    track_name_label.pack(padx=10, pady=5)
    track_name_entry = tk.Entry(root)
    track_name_entry.pack(padx=10, pady=5)

    lap_time_label = tk.Label(root, text="Lap Time:")
    lap_time_label.pack(padx=10, pady=5)
    lap_time_entry = tk.Entry(root)
    lap_time_entry.pack(padx=10, pady=5)

    # Buttons
    save_button = tk.Button(root, text="Save Lap Time", command=lambda: [save_lap_time(track_name_entry.get(), lap_time_entry.get(), driver_name_entry.get()), update_lap_times_text(lap_times_text, display_lap_times())])
    save_button.pack(padx=10, pady=10)

    # display_button = tk.Button(root, text="Display Lap Times", command=lambda:update_lap_times_text(lap_times_text, display_lap_times()))
    # display_button.pack(padx=10, pady=10)

    # Lap Times Display
    lap_times_label = tk.Label(root, text="Lap Times:", font=('Arial', 14))
    lap_times_label.pack(padx=20, pady=10)

    lap_times_text = tk.Text(root, height=10, width=40)
    lap_times_text.pack(padx=10, pady=10)


def update_lap_times_text(text_widget, lap_times):
    text_widget.config(state=tk.NORMAL)  # Enable editing
    text_widget.delete(1.0, tk.END)  # Clear existing text
    text_widget.insert(tk.END, lap_times)  # Insert lap times
    text_widget.config(state=tk.DISABLED)  # Disable editing
    pass
