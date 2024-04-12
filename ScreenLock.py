import tkinter as tk
import sys
import os
import json

with open('config.json') as config_file:
    config = json.load(config_file)   

# Unlock Screen if password correct
def unlock(password_entry, root, error_label):
    password = password_entry.get()
    
    if password == config['password']:  
        root.destroy()
        sys.exit(0)
    else:
        error_label.config(text="Incorrect password. Please try again.")  
        password_entry.delete(0, tk.END)

# Shutdown System if password correct
def shutdown_windows(password_entry, error_label):
    password = password_entry.get()
    
    if password == config['password']:  
        os.system("shutdown /s /t 3")  
    else:
        error_label.config(text="Incorrect password. Please try again.")  
        password_entry.delete(0, tk.END)

# Initiate Lock Screen by generating a full screen, on top, black square with commands activated by password
def show_lock_screen():
    
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.configure(background='black') 
    root.wm_attributes("-topmost", True)
    
    label = tk.Label(root, text="Enter password to unlock", fg="white", bg="black", font=("Helvetica", 24))
    label.pack(pady=50)

    error_label = tk.Label(root, text="", fg="red", bg="black", font=("Helvetica", 12))
    error_label.pack(pady=10)

    password_entry = tk.Entry(root, show='*')
    password_entry.pack(pady=10)
  
    def unlock_and_destroy(event=None):
        unlock(password_entry, root, error_label)

    # Bind the Return key to call the unlock function
    password_entry.bind('<Return>', unlock_and_destroy)

    unlock_button = tk.Button(root, text="Unlock", command=lambda: unlock(password_entry, root, error_label))
    unlock_button.pack(pady=10)
    
    shutdown_button = tk.Button(root, text="ShutDown", command=lambda: shutdown_windows(password_entry, error_label))
    shutdown_button.pack(pady=10)
    
    root.mainloop()

