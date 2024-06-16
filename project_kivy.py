from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.spinner import Spinner
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.videoplayer import VideoPlayer
from kivy.uix.video import Video

class B(Button):
    def __init__(self,screen,direction='rigth', goal='main',**kwargs):
        super().__init__(**kwargs)
        self.screen = screen
        self.direction = direction
        self.goal = goal
    def on_press(self):
        self.screen.manager.transition.direction = self.direction
        self.screen.manager.current = self.goal

class MyApp(App):
    def build(self):
        manager = ScreenManager()
        manager.add_widget(MainS(name='main'))
        manager.add_widget(Screen1(name='screen1'))
        return manager

class MainS(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        button = B(self,direction='left',goal='screen1',text='наступний екран')
        lanel = Label(text = '1 екран')
        layout = BoxLayout()
        layout.add_widget(button)
        layout.add_widget(lanel)    
        self.add_widget(layout)

class Screen1(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        button = B(self,direction='right',goal='main',text='наступний екран')
        lanel = Label(text = 'Фільм:Погані хлопці-Все або нічого.')
        lanel1 = Label(text = "ОФІЦІЙНИЙ ТРЕЙЛЕР ФІЛЬМУ | ПОГАНІ ХЛОПЦІ: ВСЕ АБО НІЧОГО | Прем'єра (в Україні): 06.06.2024")
        video = VideoPlayer(source = "trailer.mp4", state="pause", options={'allow_stretch': True})
        layout = BoxLayout(orientation="vertical")
        layout.add_widget(video)
        layout.add_widget(button)
        layout.add_widget(lanel)  
        self.add_widget(layout)




app = MyApp()
app.run()