from kivy.app import App
from kivy.uix.label import Label

class TranslatorApp(App):
    def build(self):
        return Label(text='Translator Academy')

if __name__ == '__main__':
    TranslatorApp().run()
