from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
import time
from kivy.uix.image import Image

class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super(MenuScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')

        # Barra de estado de hora, señal y notificaciones
        status_bar = BoxLayout(orientation='horizontal', size_hint=(1, 0.1), padding=10, spacing=10)
        
        signal_icon = Label(text='Sig', size_hint=(0.1, 1), font_size='24sp')  # Señal
        notification_icon = Label(text='Camp', size_hint=(0.1, 1), font_size='24sp')  # Notificaciones
        self.time_label = Label(font_size='20sp', size_hint=(0.8, 1), halign='center', valign='middle')

        # Actualizar la hora
        Clock.schedule_interval(self.update_time, 1)
        status_bar.add_widget(signal_icon)
        status_bar.add_widget(self.time_label)
        status_bar.add_widget(notification_icon)

        # Iconos de las apps
        grid = GridLayout(cols=2, rows=3, padding=20, spacing=20, size_hint=(1, 0.9))
        
        # Lista de los iconos y las etiquetas
        icons = ['icons/contacts.svg', 'icons/call.svg', 'icons/message.svg', 'icons/social.svg', 'icons/camera.svg', 'icons/music.svg']
        labels = ['Contactos', 'Llamar', 'Mensaje', 'Red Social', 'Cámara', 'Música']
        screens = ['contacts', 'call', 'message', 'social', 'camera', 'music']

        for icon, label, screen_name in zip(icons, labels, screens):
            # Crear layout del botón
            button_layout = BoxLayout(orientation='vertical', padding=10)

            # Añadir ícono PNG
            png_icon = Image(source=icon, size_hint=(1, 1))
            button_layout.add_widget(png_icon)

            # Añadir etiqueta
            button_layout.add_widget(Label(text=label, font_size='18sp', halign='center', valign='middle', size_hint=(1, 0.2)))

            # Crear botón
            button = Button(size_hint=(1, 1))
            button.add_widget(button_layout)
            button.bind(on_press=lambda x, screen_name=screen_name: self.switch_screen(screen_name))

            # Añadir al grid
            grid.add_widget(button)

        layout.add_widget(status_bar)
        layout.add_widget(grid)
        self.add_widget(layout)

    def update_time(self, *args):
        self.time_label.text = time.strftime('%H:%M')

    def switch_screen(self, screen_name):
        self.manager.current = screen_name  # Cambia de pantalla
