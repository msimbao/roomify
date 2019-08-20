#====================================================

"""

By Mphatso Simbao

This is a simple Kivy App for playing a certain genre of 
music or playlist automatically depending on where the use is
in their house, e.g the music genre changes when moving from
the bedroom to the gym using machine learning

This was built using soundcloud-lib and whereami

"""

#====================================================

#Import Packages

#WebScraping Packages
import bs4
import requests


#Indoor Localization Packages
from whereami import learn
from whereami import get_pipeline
from whereami import predict, predict_proba, crossval, locations

#Threading and Time Packages
import time
import threading

#Sound Packages
import os
import playsound
from sclib import SoundcloudAPI, Track, Playlist

#Kivy Packages
import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.utils import platform
from kivy.config import Config
from kivy.core.window import Window
from kivy.uix.dropdown import DropDown
from kivy.core.text import LabelBase
from kivy.uix.screenmanager import ScreenManager, Screen

LabelBase.register(name="Fredoka",
fn_regular="fonts/FredokaOne-Regular.ttf"
)


LabelBase.register(name="Avenir",
fn_regular="fonts/AvenirLTStd-Medium.ttf"
)


if platform not in ('android','ios'):
    #Approximate dimensions of mobile phone.
    Config.set('graphics','resizable','0')
    Window.size = (300,420)



#====================================================

#Collect Mp3s from Soundcloud Website and set up sound player app

#====================================================



class MainWindow(Screen):
    pass

class SecondWindow(Screen):
    name = ObjectProperty(None)
    genre = ObjectProperty(None)
  
    api = SoundcloudAPI()
    playlist = api.resolve('https://soundcloud.com/playlist/sets/started-on-soundcloud')

    assert type(playlist) is Playlist

    # filename = f'./Roomify Songs/{track.artist} - {track.title}.mp3'

    # files = []
    # file_index = 0
    # for filename in os.listdir("./"):
    #     if filename.endswith(".mp3"):
    #         files.append(filename)

    def soundplayer(self):
        """ Simple function that takes a file directory and plays all mp3s in that file"""
        # files.sort() # do this if you want them in name order
        # playsound.playsound(self.files[self.file_index])
        # self.file_index = (self.file_index + 1) % len(self.files)
        # playsound.playsound(self.files[self.file_index])
    
    def btn(self):
        print("Name:",self.name.text,"Genre",self.genre.text)
        self.name.text = ""
        self.genre.text = ""
        learn(self.name.text)
        # threading.Thread(target=self.soundplayer).start()
        # threading.Thread(target=self.soundplayer).join()

class WindowManager(ScreenManager):
    pass

class CustomDropDown(DropDown):
    pass

#============================================

#Initiate Kivy App Class

#=========================================

kv = Builder.load_file("my.kv")

class MyApp(App):
    def build(self):
        return kv
  
if __name__ == "__main__":
    MyApp().run()