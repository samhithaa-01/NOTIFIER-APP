from tkinter import *
from plyer import notification
from tkinter import messagebox
from PIL import Image, ImageTk
import time

# Initialize the Tkinter window
root = Tk()
root.title('Reminder Notifier')
root.geometry("500x300")

# Load an image to display in the app
reminder_img = Image.open("notify-label.png")
reminder_tkimage = ImageTk.PhotoImage(reminder_img)

# Function to get the details entered by the user and trigger the notification
def set_reminder():
    reminder_title = title_entry.get()
    reminder_message = message_entry.get()
    reminder_time = time_entry.get()

    if reminder_title == "" or reminder_message == "" or reminder_time == "":
        messagebox.showerror("Error", "All fields are required!")
    else:
        try:
            # Convert the time input to seconds (minutes -> seconds)
            reminder_seconds = float(reminder_time) * 60
            messagebox.showinfo("Reminder Set", f"Your reminder will trigger in {reminder_time} minutes.")
            
            # Close the Tkinter window and wait for the specified time
            root.destroy()
            time.sleep(reminder_seconds)

            # Trigger the notification after the delay
            notification.notify(
                title=reminder_title,
                message=reminder_message,
                app_name="Reminder Notifier",
                app_icon="ico.ico",  # Replace with actual icon file path if needed
                toast=True,
                timeout=10
            )
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid time in minutes!")

# Add image to the Tkinter window
image_label = Label(root, image=reminder_tkimage).grid()

# Label for Reminder Title
title_label = Label(root, text="Reminder Title", font=("poppins", 10))
title_label.place(x=12, y=70)

# Entry field for Reminder Title
title_entry = Entry(root, width="25", font=("poppins", 13))
title_entry.place(x=150, y=70)

# Label for Reminder Message
message_label = Label(root, text="Reminder Message", font=("poppins", 10))
message_label.place(x=12, y=120)

# Entry field for Reminder Message
message_entry = Entry(root, width="40", font=("poppins", 13))
message_entry.place(x=150, y=120)

# Label for Reminder Time
time_label = Label(root, text="Time (minutes)", font=("poppins", 10))
time_label.place(x=12, y=175)

# Entry field for Reminder Time
time_entry = Entry(root, width="5", font=("poppins", 13))
time_entry.place(x=150, y=175)

# Label for 'minutes' beside the time field
time_unit_label = Label(root, text="min", font=("poppins", 10))
time_unit_label.place(x=210, y=180)

# Button to set the notification
set_button = Button(root, text="SET REMINDER", font=("poppins", 10, "bold"), fg="#ffffff", bg="#34A853", width=20, 
                    command=set_reminder)
set_button.place(x=170, y=230)

# Prevent window resizing
root.resizable(0,0)

# Start the Tkinter event loop
root.mainloop()
