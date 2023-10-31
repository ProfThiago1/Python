from kivy.app import App
from kivy.uix.label import Label

class MainApp(App):
    def build(self):
        label = Label(text="Um primeiro teste.", size_hint=(.5,.5), pos_hint={'center_x':.5, 'center_y':.5})
        return label

MainApp().run()