from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.metrics import dp


class Calculator(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)

        # ===== DISPLAY =====
        self.display = TextInput(
            readonly=True,
            font_size="26sp",
            size_hint=(1, 0.25),
            halign="right",
            multiline=False,
            padding=[dp(12), dp(12)]
        )
        self.add_widget(self.display)

        # ===== BUTTON GRID =====
        grid = GridLayout(
            cols=4,
            spacing=dp(6),
            padding=dp(6),
            size_hint=(1, 0.75)
        )

        buttons = [
            "AC", "(", ")", "DEL",
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "=", "+"
        ]

        for text in buttons:
            btn = Button(
                text=text,
                font_size="18sp",
                size_hint=(1, 1)
            )
            btn.bind(on_press=self.on_press)
            grid.add_widget(btn)

        self.add_widget(grid)

    def on_press(self, instance):
        t = instance.text

        if t == "AC":
            self.display.text = ""
        elif t == "DEL":
            self.display.text = self.display.text[:-1]
        elif t == "=":
            try:
                self.display.text = str(eval(self.display.text))
            except:
                self.display.text = "Error"
        else:
            self.display.text += t


class CalculatorApp(App):
    def build(self):
        return Calculator()


if __name__ == "__main__":
    CalculatorApp().run()
