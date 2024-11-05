import tkinter as tk
from tkinter import ttk, messagebox
import yt_dlp

def download_youtube_video(url, save_path="youtube_video.mp4"):
    try:
        ydl_opts = {
            'format': 'best',
            'outtmpl': save_path,
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        messagebox.showinfo("Succès", f"Vidéo YouTube téléchargée dans {save_path}")
    except Exception as e:
        messagebox.showerror("Erreur", f"Impossible de télécharger la vidéo YouTube : {e}")

def download_twitter_video(url, save_path="twitter_video.mp4"):
    try:
        ydl_opts = {
            'format': 'best',
            'outtmpl': save_path,
            'cookiefile': 'twitter_cookies.txt',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        messagebox.showinfo("Succès", f"Vidéo Twitter téléchargée dans {save_path}")
    except Exception as e:
        messagebox.showerror("Erreur", f"Impossible de télécharger la vidéo Twitter : {e}")

def download_twitch_video(url, save_path="twitch_video.mp4"):
    try:
        ydl_opts = {
            'format': 'best',
            'outtmpl': save_path,
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        messagebox.showinfo("Succès", f"Vidéo Twitch téléchargée dans {save_path}")
    except Exception as e:
        messagebox.showerror("Erreur", f"Impossible de télécharger la vidéo Twitch : {e}")

def download_pinterest_video(url, save_path="pinterest_video.mp4"):
    try:
        ydl_opts = {
            'format': 'best',
            'outtmpl': save_path,
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        messagebox.showinfo("Succès", f"Vidéo Pinterest téléchargée dans {save_path}")
    except Exception as e:
        messagebox.showerror("Erreur", f"Impossible de télécharger la vidéo Pinterest : {e}")

def download_tiktok_video(url, save_path="tiktok_video.mp4"):
    try:
        ydl_opts = {
            'format': 'best',
            'outtmpl': save_path,
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        messagebox.showinfo("Succès", f"Vidéo TikTok téléchargée dans {save_path}")
    except Exception as e:
        messagebox.showerror("Erreur", f"Impossible de télécharger la vidéo TikTok : {e}")

def paste_from_clipboard(entry):
    entry.delete(0, tk.END)
    entry.insert(0, root.clipboard_get())

# Interface Tkinter
root = tk.Tk()
root.title("Téléchargeur de Vidéo")

# Création du notebook pour les onglets
notebook = ttk.Notebook(root)
notebook.pack(pady=10, expand=True)

# Onglet pour YouTube
youtube_tab = ttk.Frame(notebook)
notebook.add(youtube_tab, text="YouTube")

youtube_entry = tk.Entry(youtube_tab, width=50)
youtube_entry.pack(pady=5)
youtube_paste_button = tk.Button(youtube_tab, text="Coller", command=lambda: paste_from_clipboard(youtube_entry))
youtube_paste_button.pack(pady=5)
youtube_download_button = tk.Button(youtube_tab, text="Télécharger", command=lambda: download_youtube_video(youtube_entry.get()))
youtube_download_button.pack(pady=5)

# Onglet pour Twitter
twitter_tab = ttk.Frame(notebook)
notebook.add(twitter_tab, text="Twitter")

twitter_entry = tk.Entry(twitter_tab, width=50)
twitter_entry.pack(pady=5)
twitter_paste_button = tk.Button(twitter_tab, text="Coller", command=lambda: paste_from_clipboard(twitter_entry))
twitter_paste_button.pack(pady=5)
twitter_download_button = tk.Button(twitter_tab, text="Télécharger", command=lambda: download_twitter_video(twitter_entry.get()))
twitter_download_button.pack(pady=5)

# Onglet pour Twitch
twitch_tab = ttk.Frame(notebook)
notebook.add(twitch_tab, text="Twitch")

twitch_entry = tk.Entry(twitch_tab, width=50)
twitch_entry.pack(pady=5)
twitch_paste_button = tk.Button(twitch_tab, text="Coller", command=lambda: paste_from_clipboard(twitch_entry))
twitch_paste_button.pack(pady=5)
twitch_download_button = tk.Button(twitch_tab, text="Télécharger", command=lambda: download_twitch_video(twitch_entry.get()))
twitch_download_button.pack(pady=5)

# Onglet pour Pinterest
pinterest_tab = ttk.Frame(notebook)
notebook.add(pinterest_tab, text="Pinterest")

pinterest_entry = tk.Entry(pinterest_tab, width=50)
pinterest_entry.pack(pady=5)
pinterest_paste_button = tk.Button(pinterest_tab, text="Coller", command=lambda: paste_from_clipboard(pinterest_entry))
pinterest_paste_button.pack(pady=5)
pinterest_download_button = tk.Button(pinterest_tab, text="Télécharger", command=lambda: download_pinterest_video(pinterest_entry.get()))
pinterest_download_button.pack(pady=5)

# Onglet pour TikTok
tiktok_tab = ttk.Frame(notebook)
notebook.add(tiktok_tab, text="TikTok")

tiktok_entry = tk.Entry(tiktok_tab, width=50)
tiktok_entry.pack(pady=5)
tiktok_paste_button = tk.Button(tiktok_tab, text="Coller", command=lambda: paste_from_clipboard(tiktok_entry))
tiktok_paste_button.pack(pady=5)
tiktok_download_button = tk.Button(tiktok_tab, text="Télécharger", command=lambda: download_tiktok_video(tiktok_entry.get()))
tiktok_download_button.pack(pady=5)

root.mainloop()
