from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.clock import Clock

class GUI(Widget):
    pass

class ViewPort(Image):
    def build(self):
        return Image(source='../tests/test_cases/testImage.jpg')

class PixelApp(App):
    def build(self):
        return GUI()

if __name__ == '__main__':
    PixelApp().run()
