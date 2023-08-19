from kivymd.app import MDApp
from main_window import MainWindows
# from kivy.config import Config
# Config.set('graphics', 'fullscreen', '0')
# Config.write()
from kivy.utils import platform
if platform != "android":
    ######### Размер телефона
    from kivy.core.window import Window

    Window.size = (300, 600)

class MainApp(MDApp):
    def build(self):
        return MainWindows()

if __name__ == '__main__':
    MainApp().run()