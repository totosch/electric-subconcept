from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.spinner import Spinner
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window
from calcs import MathLogic

class MainLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(MainLayout, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.spacing = 20  # Increase spacing between widgets
        self.padding = 40  # Increase padding around the layout
        self.bind(size=self.update_rect, pos=self.update_rect)
        self.create_widgets()
        self.math_logic = MathLogic()

    def create_widgets(self):
        with self.canvas.before:
            Color(21/255, 32/255, 43/255, 1)  # Set background color to RGB (21, 32, 43)
            self.rect = Rectangle(size=self.size, pos=self.pos)

        title = Label(text='Calculo de Nuevo Sub-Concepto Eléctrico', font_size='24sp', size_hint=(1, None), height=Window.height * 0.1)
        self.add_widget(title)

        consumo_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint=(1, None), height=Window.height * 0.1)
        consumo_label = Label(text='Consumo:', size_hint=(None, 1))
        self.consumo_input = TextInput(hint_text='Completar Umbral de Consumo (kWh)', halign='center')
        self.consumo_input.bind(size=self.update_padding, text=self.update_padding)
        consumo_layout.add_widget(consumo_label)
        consumo_layout.add_widget(self.consumo_input)
        self.add_widget(consumo_layout)

        nivel_ingreso_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint=(1, None), height=Window.height * 0.1)
        nivel_ingreso_label = Label(text='Nivel Ingreso:', size_hint=(None, 1))
        self.nivel_ingreso_spinner = Spinner(text='Selecciona Nivel de Ingresos', values=('Ingresos Altos: 1', 'Ingresos Medios: 2', 'Ingresos Bajos: 3'))
        nivel_ingreso_layout.add_widget(nivel_ingreso_label)
        nivel_ingreso_layout.add_widget(self.nivel_ingreso_spinner)
        self.add_widget(nivel_ingreso_layout)

        button = Button(text='Submit', size_hint=(1, None), height=Window.height * 0.1)
        button.bind(on_press=self.result)
        self.add_widget(button)

        self.result_label = Label(text='', size_hint=(1, None), height=Window.height * 0.1)
        self.add_widget(self.result_label)


    def update_rect(self, instance, value):
        self.rect.size = instance.size
        self.rect.pos = instance.pos

    def update_padding(self, instance, value):
        if value:
            padding_y = max((instance.height - instance.line_height) / 2, 0)
            instance.padding_y = padding_y

    def result(self, instance):
        consumo_text = self.consumo_input.text.strip()
        nivel_ingreso_text = self.nivel_ingreso_spinner.text.split(':')[-1].strip()

        if not consumo_text:
            self.result_label.text = 'Please input consumption.'
            return
        elif not nivel_ingreso_text:
            self.result_label.text = 'Please select income level.'
            return

        consumo_value = float(consumo_text)
        nivel_ingreso = int(nivel_ingreso_text)

        self.math_logic.set_consumo(consumo_value)
        self.math_logic.set_nivel_ingreso(nivel_ingreso)

        result = self.math_logic.calculate_result(nivel_ingreso, consumo_value)
        self.result_label.text = 'Nuevo valor: ' + str(result)
