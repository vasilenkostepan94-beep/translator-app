from kivy.app import App
from kivy.uix.label import Label

class TranslatorAcademyApp(App):
    def build(self):
        return Label(text='Translator Academy')

if __name__ == '__main__':
    TranslatorAcademyApp().run()
