from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.uix.popup import Popup

class MainScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'

        # Crear la pantalla de inicio
        self.init_screen()

    def init_screen(self):
        # Agregar el nombre de la aplicación
        app_name_label = Label(
            text="Bienestar ++",
            font_size='32sp',  # Tamaño de fuente grande
            size_hint=(1, 0.3),  # Ocupa el 30% de la altura
            halign='center',
            valign='middle'
        )
        app_name_label.bind(size=app_name_label.setter('text_size'))  # Centrar el texto
        self.add_widget(app_name_label)

        # Agregar botón "Ver Contactos"
        contacts_button = Button(
            text="Ver Contactos",
            size_hint=(1, 0.2)
        )
        contacts_button.bind(on_press=self.show_contact_list)
        self.add_widget(contacts_button)

        # Agregar botón "Ver Horario de Pastillas"
        pill_schedule_button = Button(
            text="Ver Horario de Pastillas",
            size_hint=(1, 0.2)
        )
        pill_schedule_button.bind(on_press=self.show_pill_schedule)
        self.add_widget(pill_schedule_button)

    def show_contact_list(self, instance):
        # Mostrar la lista de contactos en un Popup
        contact_list_screen = ContactListScreen()
        popup = Popup(
            title="Contactos Cercanos",
            content=contact_list_screen,
            size_hint=(0.8, 0.8)
        )
        contact_list_screen.popup = popup  # Referencia al Popup para cerrarlo
        popup.open()

    def show_pill_schedule(self, instance):
        # Mostrar el horario de pastillas en un Popup
        pill_schedule_screen = PillScheduleScreen()
        popup = Popup(
            title="Horario de Tomar Pastillas",
            content=pill_schedule_screen,
            size_hint=(0.8, 0.6)
        )
        pill_schedule_screen.popup = popup  # Referencia al Popup para cerrarlo
        popup.open()

class ContactListScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'

        # Crear GridLayout para la lista de contactos
        grid = GridLayout(cols=1, padding=10, spacing=10, size_hint=(1, 1))

        # Lista de contactos con detalles
        contacts = [
            ("Esposa", "Sofia", "55 4394 88##"),
            ("Hijo", "Ricardo", "56 1122 334#"),
            ("Hermano", "Fabian", "55 4433 88##"),
            ("Cardiologo", "Ernesto Fernandez", "N/A")
        ]

        for contact_type, name, phone in contacts:
            contact_label = Label(
                text=f"{contact_type}: {name}\nTeléfono: {phone}",
                font_size='18sp',
                size_hint_y=None,
                height=80
            )
            grid.add_widget(contact_label)

        self.add_widget(grid)

        # Agregar botón de regresar
        back_button = Button(
            text="Regresar",
            size_hint=(1, 0.2)
        )
        back_button.bind(on_press=self.close_popup)
        self.add_widget(back_button)

    def close_popup(self, instance):
        # Cerrar el Popup
        self.popup.dismiss()

class PillScheduleScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'

        # Horario de pastillas
        pill_schedule_label = Label(
            text="Horario de Tomar Pastillas:\n9:00 AM\n4:00 PM",
            font_size='18sp',
            size_hint=(1, 1)
        )
        self.add_widget(pill_schedule_label)

        # Agregar botón de regresar
        back_button = Button(
            text="Regresar",
            size_hint=(1, 0.2)
        )
        back_button.bind(on_press=self.close_popup)
        self.add_widget(back_button)

    def close_popup(self, instance):
        # Cerrar el Popup
        self.popup.dismiss()

class MainMenuApp(App):
    def build(self):
        Window.size = (360, 640)  # Tamaño de la ventana
        return MainScreen()

if __name__ == '__main__':
    MainMenuApp().run()
