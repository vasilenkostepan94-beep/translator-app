from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import urllib.request
import urllib.parse
import json
import ssl

class TranslatorAcademyApp(App):
    def build(self):
        self.cards = [
            ("Hello / Hi", "Привет / Здравствуйте"),
            ("Good morning", "Доброе утро"),
            ("How are you?", "Как дела?"),
            ("Thank you", "Большое спасибо")
        ]
        self.card_index = 0

        root = BoxLayout(orientation='vertical', padding=15, spacing=10)

        root.add_widget(Label(text="TRANSLATOR & ACADEMY", font_size=20, size_hint_y=None, height=40))

        self.input_text = TextInput(text='', hint_text='Введите текст для перевода', size_hint_y=None, height=45)
        root.add_widget(self.input_text)

        self.result_label = Label(text='Результат перевода...', font_size=16, size_hint_y=None, height=60)
        root.add_widget(self.result_label)

        trans_btn = Button(text='ПЕРЕВЕСТИ', size_hint_y=None, height=50, background_color=(0.14, 0.39, 0.92, 1))
        trans_btn.bind(on_press=self.translate)
        root.add_widget(trans_btn)

        root.add_widget(Label(text="Флеш-карточки", font_size=18, size_hint_y=None, height=30))
        
        self.card_label = Label(text=self.cards[0][0], font_size=20, size_hint_y=None, height=70)
        root.add_widget(self.card_label)

        next_btn = Button(text='Следующая карточка', size_hint_y=None, height=50, background_color=(0.02, 0.58, 0.41, 1))
        next_btn.bind(on_press=self.next_card)
        root.add_widget(next_btn)

        return root

    def translate(self, instance):
        text = self.input_text.text.strip()
        if not text:
            self.result_label.text = "Введите текст!"
            return
        try:
            url = f"https://api.mymemory.translated.net/get?q={urllib.parse.quote(text)}&langpair=ru|en"
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            ctx = ssl.create_default_context()
            ctx.check_hostname = False
            ctx.verify_mode = ssl.CERT_NONE
            with urllib.request.urlopen(req, context=ctx, timeout=5) as resp:
                data = json.loads(resp.read().decode('utf-8'))
                res = data.get("responseData", {}).get("translatedText", "Ошибка")
                self.result_label.text = res
        except Exception as e:
            self.result_label.text = "Ошибка сети"

    def next_card(self, instance):
        self.card_index = (self.card_index + 1) % len(self.cards)
        self.card_label.text = self.cards[self.card_index][0]

if __name__ == '__main__':
    TranslatorAcademyApp().run()
