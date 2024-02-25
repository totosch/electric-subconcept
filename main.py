from kivy.app import App
from ui import MainLayout

class TestApp(App):
    def build(self):
        return MainLayout()

if __name__ == '__main__':
    TestApp().run()
 