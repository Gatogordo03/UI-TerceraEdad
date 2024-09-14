from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen

class SocialScreen(Screen):
    def __init__(self, **kwargs):
        super(SocialScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')

        back_button = Button(text="Atrás", size_hint=(0.1, 0.1))
        back_button.bind(on_press=self.go_back)

        content_label = Label(text="Pantalla de Red Social", font_size='20sp')
        layout.add_widget(back_button)
        layout.add_widget(content_label)
        self.add_widget(layout)
    
    def go_back(self, instance):
        self.manager.current = 'menu'