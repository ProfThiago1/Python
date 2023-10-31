from kivy.app import App
from kivy.uix.image import Image, AsyncImage

class MainApp(App):
    def build(self):
        img =AsyncImage(source ='https://supermariorun.com/assets/img/stage/mario03.png', size_hint = (1,.5), pos_hint = {'center_x':.5, 'center_y':.5})
        return img

MainApp().run()