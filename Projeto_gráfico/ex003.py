import random

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

# Definindo as cores dos botões (em RGBA)

red = [1,0,0,1]
green = [0,1,0,1]
blue = [0,0,1,1]
purple = [1,0,1,1]

class HBoxLayout(App):
    def build(self):
        layout = BoxLayout(padding=10)
        cor = [red,blue,green,purple]

        i = 0 # contador
        for i in range(5):
            btn = Button(text = f'Este é o botão #{i+1}', font_size='17sp', background_color = random.choice(cor)) #selecionando a cor aleatoriamente
            layout.add_widget(btn) #adiciona um novo botão ao widget pai
        return layout

HBoxLayout().run()