from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel

class ScreenRecorderApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        layout = MDBoxLayout(orientation='vertical', spacing=20, padding=40)

        self.status_label = MDLabel(
            text="📱 Screen Recorder Ready",
            halign="center",
            theme_text_color="Primary"
        )

        start_btn = MDRaisedButton(
            text="🎥 Start Recording",
            md_bg_color=(0, 0.6, 1, 1),
            on_release=self.start_recording
        )

        stop_btn = MDRaisedButton(
            text="🛑 Stop Recording",
            md_bg_color=(1, 0, 0, 1),
            on_release=self.stop_recording
        )

        layout.add_widget(self.status_label)
        layout.add_widget(start_btn)
        layout.add_widget(stop_btn)

        return layout

    def start_recording(self, *args):
        self.status_label.text = "🔴 Recording started..."
        # Android స్క్రీన్ రికార్డింగ్ ప్రారంభించే కోడ్ ఇక్కడ రాయాలి

    def stop_recording(self, *args):
        self.status_label.text = "✅ Recording stopped.\nSaved in /storage/emulated/0/Recordings/"
        # రికార్డింగ్ ఆపే కోడ్ ఇక్కడ రాయాలి

ScreenRecorderApp().run()