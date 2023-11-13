
# Clock Application #

import tkinter as tk
import time

class ClockApplication: # Object constructor 
    def __init__(self, master):
        self.master = master # Master represents parent or main window
        master.title("Clock Application") # Title

        # Frame to contain the time_label with a border
        self.time_frame = tk.Frame(master, borderwidth=2, relief="solid")
        self.time_frame.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        # Main time label 
        self.time_label = tk.Label(self.time_frame, font=("Arial", 60), text="")
        self.time_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        # Labels for year, month, day, hour, minute and second
        self.year_label = tk.Label(master, font=("Arial", 14))
        self.year_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        
        self.month_label = tk.Label(master, font=("Arial", 14))
        self.month_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        
        self.day_label = tk.Label(master, font=("Arial", 14))
        self.day_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        
        self.hour_label = tk.Label(master, font=("Arial", 14))
        self.hour_label.grid(row=1, column=1, padx=10, pady=5, sticky="e")
        
        self.minute_label = tk.Label(master, font=("Arial", 14))
        self.minute_label.grid(row=2, column=1, padx=10, pady=5, sticky="e")
        
        self.second_label = tk.Label(master, font=("Arial", 14))
        self.second_label.grid(row=3, column=1, padx=10, pady=5, sticky="e")

        # Starting function time_update
        self.time_update()

    def time_update(self): # Function to update labels every second
        time_current = time.strftime("%Y-%m-%d %H:%M:%S")  # Time format
        
        self.time_label.configure(text=time_current)
        
        # Extracts year, month, day, hour, minute, and second using slicing from the current local time
        year, month, day, hour, minute, second = time.localtime()[:6]
        
        # Update year, month, day, hour, minute and second labels
        self.year_label.configure(text=f"Year: {year}")
        self.month_label.configure(text=f"Month: {month:02d}")
        self.day_label.configure(text=f"Day: {day:02d}")
        self.hour_label.configure(text=f"Hour: {hour:02d}")
        self.minute_label.configure(text=f"Minute: {minute:02d}")
        self.second_label.configure(text=f"Second: {second:02d}")
        
        # Schedule the time_update function to run again after 1000 milliseconds (1 second)
        self.master.after(1000, self.time_update)

# Window Settings 

window = tk.Tk()

# Configuration of grid rows 
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)

window.resizable(False, False)
clock = ClockApplication(window)

# Main Application Loop

window.mainloop()
