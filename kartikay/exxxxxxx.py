import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import time

# Simulate transferring music (You will replace this with actual API calls)
def transfer_music():
    spotify_playlist = spotify_entry.get()
    amazon_playlist = amazon_entry.get()

    if spotify_playlist and amazon_playlist:
        # Reset progress bar
        progress_bar['value'] = 0
        progress_label.config(text="Starting transfer...")

        # Simulate track transfer
        root.update_idletasks()
        for i in range(1, 101):
            time.sleep(0.05)  # Simulate time taken to transfer each track
            progress_bar['value'] = i  # Update progress
            progress_label.config(text=f"Transferring {i}%")
            root.update_idletasks()  # Update the GUI

        # After finishing
        progress_label.config(text="Transfer Complete!")
        messagebox.showinfo("Transfer Complete", "Music transfer from Spotify to Amazon Music completed successfully!")
    else:
        messagebox.showwarning("Input Error", "Please enter both Spotify and Amazon Music playlist details.")

# Setting up the Tkinter window
root = tk.Tk()
root.title("Music Transfer Tool")

# Spotify Label and Entry
spotify_label = tk.Label(root, text="Spotify Playlist URL/ID:")
spotify_label.pack(pady=10)

spotify_entry = tk.Entry(root, width=50)
spotify_entry.pack(pady=5)

# Amazon Music Label and Entry
amazon_label = tk.Label(root, text="Amazon Music Playlist Name/ID:")
amazon_label.pack(pady=10)

amazon_entry = tk.Entry(root, width=50)
amazon_entry.pack(pady=5)

# Transfer Button
transfer_button = tk.Button(root, text="Transfer Music", command=transfer_music)
transfer_button.pack(pady=20)

# Progress bar
progress_bar = ttk.Progressbar(root, orient="horizontal", length=300, mode='determinate')
progress_bar.pack(pady=10)

# Label to show progress percentage
progress_label = tk.Label(root, text="")
progress_label.pack()

# Running the main loop 
root.mainloop()
