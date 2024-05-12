from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.spinner import Spinner

class MyApp(App):
    def build(self):
        label = Label(text='Hello, world!')
        button = Button(text='Hello, world!',on_press=self.click)
        layout = BoxLayout(orientation='vertical',padding = 5,spacing = 5)
        layout2 = BoxLayout()
        spinner = Spinner(text='Hello')
        check = CheckBox(   )
        layout.add_widget(check)
        layout.add_widget(button)
        layout.add_widget(label)
        layout2.add_widget(spinner)
        layout2.add_widget(layout)
        return layout2
    def click(self,a):
        print('o')

app = MyApp()
app.run()