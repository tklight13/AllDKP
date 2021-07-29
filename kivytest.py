from kivy.app import App
from kivy.uix.widget import Widget


class BaseScreen(Widget):
    pass


class kivylog(App):
    def build(self):
        return BaseScreen()


if __name__ == '__main__':
    kivylog().run()