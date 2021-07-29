from kivy.app import App
from kivy.logger import COLORS
from kivy.uix.widget import Widget
import kivy.graphics



class BaseScreen(Widget):
    pass


class kivytest(App):
    def build(self):
        return BaseScreen()


if __name__ == '__main__':
    kivytest().run()