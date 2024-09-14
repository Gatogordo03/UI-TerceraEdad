from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window

from menu_screen import MenuScreen
from contact_screen import ContactScreen
from call_screen import CallScreen
from message_screen import MessageScreen
from social_screen import SocialScreen
from camera_screen import CameraScreen
from music_screen import MusicScreen

class MainMenuApp(App):
    def build(self):
        Window.size = (360, 640) # Resolución temporal para ver en mi lap

        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))         # Pantalla del menú principal
        sm.add_widget(ContactScreen(name='contacts'))  # Pantalla de contactos
        sm.add_widget(CallScreen(name='call'))         # Pantalla de llamadas
        sm.add_widget(MessageScreen(name='message'))   # Pantalla de mensajes
        sm.add_widget(SocialScreen(name='social'))     # Pantalla de red social
        sm.add_widget(CameraScreen(name='camera'))     # Pantalla de cámara
        sm.add_widget(MusicScreen(name='music'))       # Pantalla de música

        return sm

if __name__ == '__main__':
    MainMenuApp().run()
