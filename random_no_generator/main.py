import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import random
#kivy.require(version)


class Myroot(BoxLayout):

    def __init__(self):
        super(Myroot,self).__init__()

    def generate_number(self):
        self.random_variable.text = str(random.randint(0, 1000))
class Neutron(App):
    
    def build(self):
        return Myroot()

ner = Neutron()
ner.run()
