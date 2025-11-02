import tkinter as tk
from tkinter import filedialog
import pygame
from mutagen.mp3 import MP3
import os

# Initialize pygame mixer
pygame.mixer.init()

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("400x400")
        self.root.configure(bg="#1d1d1d")
        
        self.current_track_index = 0
        self.tracks = []
        self.is_playing = False

        # Track title label
        self.track_title = tk.Label(root, text="No track selected", bg="#1d1d1d", fg="#f0f0f0", font=("Arial", 14))
        self.track_title.pack(pady=20)

        # Progress and Volume sliders
        self.progress_slider = tk.Scale(root, from_=0, to=100, orient="horizontal", bg="#1d1d1d", fg="#1db954", length=300)
        self.progress_slider.pack(pady=10)

        self.volume_slider = tk.Scale(root, from_=0, to=1, resolution=0.01, orient="horizontal", bg="#1d1d1d", fg="#1db954", length=300)
        self.volume_slider.set(1)
        self.volume_slider.pack(pady=10)
        
        # Control buttons
        controls_frame = tk.Frame(root, bg="#1d1d1d")
        controls_frame.pack(pady=20)

        self.prev_button = tk.Button(controls_frame, text="⏮️", command=self.prev_track, font=("Arial", 20), bg="#1d1d1d", fg="#1db954")
        self.prev_button.grid(row=0, column=0, padx=10)

        self.play_pause_button = tk.Button(controls_frame, text="⏯️", command=self.toggle_play, font=("Arial", 20), bg="#1d1d1d", fg="#1db954")
        self.play_pause_button.grid(row=0, column=1, padx=10)

        self.next_button = tk.Button(controls_frame, text="⏭️", command=self.next_track, font=("Arial", 20), bg="#1d1d1d", fg="#1db954")
        self.next_button.grid(row=0, column=2, padx=10)

        # File selection button
        self.file_button = tk.Button(root, text="Select Music Files", command=self.load_tracks, font=("Arial", 12), bg="#1db954", fg="#ffffff")
        self.file_button.pack(pady=20)

        # Bind volume slider
        self.volume_slider.bind("<Motion>", self.set_volume)

        # Update the progress slider periodically
        self.update_progress()

    def load_tracks(self):
        files = filedialog.askopenfilenames(title="Select Music Files", filetypes=(("MP3 Files", "*.mp3"),))
        self.tracks = list(files)
        if self.tracks:
            self.load_track(self.current_track_index)

    def load_track(self, index):
        track = self.tracks[index]
        pygame.mixer.music.load(track)
        self.track_title.config(text=os.path.basename(track))
        self.play_track()

    def play_track(self):
        pygame.mixer.music.play()
        self.play_pause_button.config(text="⏸️")
        self.is_playing = True

    def pause_track(self):
        pygame.mixer.music.pause()
        self.play_pause_button.config(text="⏯️")
        self.is_playing = False

    def toggle_play(self):
        if self.is_playing:
            self.pause_track()
        else:
            pygame.mixer.music.unpause()
            self.play_pause_button.config(text="⏸️")
            self.is_playing = True

    def next_track(self):
        self.current_track_index = (self.current_track_index + 1) % len(self.tracks)
        self.load_track(self.current_track_index)

    def prev_track(self):
        self.current_track_index = (self.current_track_index - 1) % len(self.tracks)
        self.load_track(self.current_track_index)

    def set_volume(self, event=None):
        volume = self.volume_slider.get()
        pygame.mixer.music.set_volume(volume)

    def update_progress(self):
        if pygame.mixer.music.get_busy():
            track = MP3(self.tracks[self.current_track_index])
            length = track.info.length
            position = pygame.mixer.music.get_pos() / 1000
            self.progress_slider.set((position / length) * 100)
        self.root.after(1000, self.update_progress)

# Set up the Tkinter window
root = tk.Tk()
app = MusicPlayer(root)
root.mainloop()
