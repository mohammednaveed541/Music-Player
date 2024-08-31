import os
import tkinter as tk
from tkinter import filedialog, messagebox
import pygame

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Music Player")
        self.root.geometry("400x300")

        # Initialize Pygame mixer
        pygame.mixer.init()

        # Current song and playlist
        self.current_song = None
        self.playlist = []
        self.song_index = 0

        # Control buttons
        self.play_button = tk.Button(root, text="Play", command=self.play_music)
        self.play_button.pack(pady=10)

        self.stop_button = tk.Button(root, text="Stop", command=self.stop_music)
        self.stop_button.pack(pady=10)

        self.pause_button = tk.Button(root, text="Pause", command=self.pause_music)
        self.pause_button.pack(pady=10)

        self.resume_button = tk.Button(root, text="Resume", command=self.resume_music)
        self.resume_button.pack(pady=10)

        self.next_button = tk.Button(root, text="Next", command=self.next_song)
        self.next_button.pack(pady=10)

        self.previous_button = tk.Button(root, text="Previous", command=self.previous_song)
        self.previous_button.pack(pady=10)

        self.select_folder_button = tk.Button(root, text="Select Folder", command=self.select_folder)
        self.select_folder_button.pack(pady=10)

    def select_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.playlist = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith(('.mp3', '.wav', '.ogg'))]
            if self.playlist:
                self.current_song = self.playlist[0]
                self.song_index = 0
                messagebox.showinfo("Folder Selected", f"{len(self.playlist)} songs loaded from the folder.")
            else:
                messagebox.showerror("Error", "No music files found in the selected folder.")
    
    def play_music(self):
        if self.current_song:
            pygame.mixer.music.load(self.current_song)
            pygame.mixer.music.play()
            messagebox.showinfo("Now Playing", f"Playing: {os.path.basename(self.current_song)}")
        else:
            messagebox.showerror("Error", "No song selected. Please select a folder first.")

    def stop_music(self):
        pygame.mixer.music.stop()

    def pause_music(self):
        pygame.mixer.music.pause()

    def resume_music(self):
        pygame.mixer.music.unpause()

    def next_song(self):
        if self.playlist and self.song_index < len(self.playlist) - 1:
            self.song_index += 1
            self.current_song = self.playlist[self.song_index]
            self.play_music()
        else:
            messagebox.showinfo("End of Playlist", "No more songs in the playlist.")

    def previous_song(self):
        if self.playlist and self.song_index > 0:
            self.song_index -= 1
            self.current_song = self.playlist[self.song_index]
            self.play_music()
        else:
            messagebox.showinfo("Start of Playlist", "This is the first song in the playlist.")

if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayer(root)
    root.mainloop()
