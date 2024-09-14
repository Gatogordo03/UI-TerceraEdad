from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen

class ContactScreen(Screen):
    def __init__(self, **kwargs):
        super(ContactScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        
        # Botón "Atrás" en la parte superior
        back_button = Button(text="Atrás", size_hint=(0.1, 0.1))
        back_button.bind(on_press=self.go_back)
        layout.add_widget(back_button)

        # Título "Lista de Contactos" en la parte superior
        title_label = Label(text="Lista de Contactos", font_size='24sp', size_hint=(1, 0.1))
        layout.add_widget(title_label)
        
        # Mostrar la lista de contactos con botones "Llamar"
        self.show_contact_list(layout)

        self.add_widget(layout)

    def show_contact_list(self, layout):
        # Crear un layout vertical para apilar los contactos
        contact_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Lista de contactos
        contacts = ['Esposa', 'Hijo', 'Hermano', 'Doctor']
        
        for contact in contacts:
            # Layout horizontal para cada contacto y su botón
            contact_box = BoxLayout(orientation='horizontal', size_hint=(1, 0.1), padding=10, spacing=10)
            
            # Etiqueta con el nombre del contacto
            contact_label = Label(text=contact, font_size='18sp', size_hint=(0.7, 1))
            contact_box.add_widget(contact_label)
            
            # Botón de "Llamar" (clickeable pero sin acción por ahora)
            call_button = Button(text="Llamar", size_hint=(0.3, 1))
            contact_box.add_widget(call_button)
            
            # Añadir cada contacto al layout principal
            contact_layout.add_widget(contact_box)

        layout.add_widget(contact_layout)

    def go_back(self, instance):
        self.manager.current = 'menu'
