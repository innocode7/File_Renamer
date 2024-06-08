import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

def rename_files_in_directory(directory, old_text, new_text):
    try:
        # List all files in the specified directory
        files = os.listdir(directory)

        for filename in files:
            # Check if the file name contains the old text
            if old_text in filename:
                # Create the new file name by replacing the old text with the new text
                new_filename = filename.replace(old_text, new_text)

                # Create full paths for the old and new file names
                old_file = os.path.join(directory, filename)
                new_file = os.path.join(directory, new_filename)

                # Rename the file
                os.rename(old_file, new_file)
                print(f'Renamed: {filename} -> {new_filename}')

        messagebox.showinfo("Success", "All files have been renamed successfully.")
    except Exception as e:
        messagebox.showerror("Error", f'An error occurred: {e}')

def select_directory():
    directory = filedialog.askdirectory()
    if directory:
        entry_directory.delete(0, tk.END)
        entry_directory.insert(0, directory)

def start_renaming():
    directory = entry_directory.get()
    old_text = entry_old_text.get()
    new_text = entry_new_text.get()
    if directory and old_text and new_text:
        rename_files_in_directory(directory, old_text, new_text)
    else:
        messagebox.showwarning("Input Error", "Please fill in all fields.")

def quit_application():
    root.quit()
    root.destroy()

def on_enter(e):
    e.widget['background'] = '#d9d9d9'

def on_leave(e):
    e.widget['background'] = 'SystemButtonFace'

# Create the main window
root = tk.Tk()
root.title("File Renamer")

# Create and place the directory selection widgets
label_directory = tk.Label(root, text="Directory:")
label_directory.grid(row=0, column=0, padx=10, pady=10)
entry_directory = tk.Entry(root, width=50)
entry_directory.grid(row=0, column=1, padx=10, pady=10)
button_browse = tk.Button(root, text="Browse", command=select_directory)
button_browse.grid(row=0, column=2, padx=10, pady=10)

# Create and place the old text widgets
label_old_text = tk.Label(root, text="Old Text:")
label_old_text.grid(row=1, column=0, padx=10, pady=10)
entry_old_text = tk.Entry(root, width=50)
entry_old_text.grid(row=1, column=1, padx=10, pady=10)

# Create and place the new text widgets
label_new_text = tk.Label(root, text="New Text:")
label_new_text.grid(row=2, column=0, padx=10, pady=10)
entry_new_text = tk.Entry(root, width=50)
entry_new_text.grid(row=2, column=1, padx=10, pady=10)

# Create a frame for the buttons
button_frame = tk.Frame(root)
button_frame.grid(row=3, column=0, columnspan=3, pady=20)

# Create and place the rename button
button_rename = tk.Button(button_frame, text="Rename Files", command=start_renaming)
button_rename.grid(row=0, column=0, padx=(0, 100), pady=10)
button_rename.bind("<Enter>", on_enter)
button_rename.bind("<Leave>", on_leave)

# Create and place the quit button
button_quit = tk.Button(button_frame, text="Quit", command=quit_application)
button_quit.grid(row=0, column=2, padx=(100, 0), pady=10)
button_quit.bind("<Enter>", on_enter)
button_quit.bind("<Leave>", on_leave)

# Run the main event loop
root.mainloop()