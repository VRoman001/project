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
from kivy.clock import Clock
from kivy.uix.floatlayout import FloatLayout

class Timer(App):
    def build(self):
        self.button1 = Button(text='start',on_press=self.start,font_size=30,size_hint=(0.9,0.8),pos_hint={'center_x': 0.5,'center_y': 0.5})
        self.button2 = Button(text='stop',on_press=self.pause,font_size=30,size_hint=(0.9,0.8),pos_hint={'center_x': 0.5,'center_y': 0.5})
        self.button3 = Button(text='reset',on_press=self.reset,font_size=30,size_hint=(0.9,0.8),pos_hint={'center_x': 0.5,'center_y': 0.5})
        self.text = Label(text='00:00:00',color='green',font_size=30)
        self.layout = BoxLayout(orientation='vertical',padding = (20,20))

        self.layout.add_widget(self.text)
        self.layout.add_widget(self.button1)
        self.layout.add_widget(self.button2)
        self.layout.add_widget(self.button3)
    
        self.total_seconds = 0
        self.running = False

        return self.layout
    
    def update_time(self,instance):
        
        self.total_seconds += 1
        hour, ostaca = divmod(self.total_seconds, 3600)
        minute, second = divmod(ostaca, 60)
        self.text.text = f'{hour:02}:{minute:02}:{second:02}'
    
    def start(self,instance):
        self.text.color = (0,1,0,1)
        if not self.running:
            self.running = True
            Clock.schedule_interval(self.update_time, 1)

    def pause(self,instance):
        self.text.color = (1,0,0,1)
        if self.running:
            self.running = False
            Clock.unschedule(self.update_time)
          

    def reset(self,instance):
        self.pause(instance)
        self.total_seconds = 0
        self.text.text = '00:00:00'
app = Timer()
app.run()