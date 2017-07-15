from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.image import Image

class GUI(App):
    def build(self):
        wimg = Image(source='../Tests/test_cases/testImage.jpg', allow_stretch=True)
        return wimg
GUI().run()
