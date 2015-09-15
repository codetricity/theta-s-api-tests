from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from thetaPythonTest import startSession, takePicture

class takePictureBtn(Button):
    def on_press(self):
        print("Take Picture button pressed")
        sid = startSession()
        takePicture(sid)

class Ping(Widget):
     pass

class PingApp(App):
    def build(self):
        return Ping()

PingApp().run()
