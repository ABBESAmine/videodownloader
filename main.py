from kivy.lang import Builder
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.core.clipboard import Clipboard
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
import yt_dlp

# Logique de téléchargement pour chaque plateforme
def download_video(url, save_path="video.mp4"):
    try:
        ydl_opts = {
            'format': 'best',
            'outtmpl': save_path,
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        return f"Vidéo téléchargée dans {save_path}"
    except Exception as e:
        return f"Erreur : {e}"

class VideoDownloaderApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        return Builder.load_file("main.kv")

    def paste_from_clipboard(self, text_input):
        """Fonction pour coller le texte du presse-papier dans le champ de texte"""
        text_input.text = Clipboard.paste()

    def download_from_platform(self, platform, url):
        """Fonction de téléchargement pour chaque onglet de plateforme"""
        if platform == "YouTube":
            message = download_video(url, save_path="youtube_video.mp4")
        elif platform == "Twitter":
            message = download_video(url, save_path="twitter_video.mp4")
        elif platform == "Twitch":
            message = download_video(url, save_path="twitch_video.mp4")
        elif platform == "Pinterest":
            message = download_video(url, save_path="pinterest_video.mp4")
        elif platform == "TikTok":
            message = download_video(url, save_path="tiktok_video.mp4")
        else:
            message = "Plateforme inconnue"
        self.root.ids.download_status.text = message

VideoDownloaderApp().run()
