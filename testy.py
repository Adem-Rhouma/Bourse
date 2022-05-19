
import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

Builder.load_file('whatever.kv')




class MyGridLayout(Widget):

    name = ObjectProperty(None)
    pizza = ObjectProperty(None)
    color = ObjectProperty(None)
    

        
        
        
    
    def press(self):
        name = self.name.text
        pizza = self.pizza.text
        color = self.color.text

        #self.add_widget(Label(text=f'Hello {name}, your favorite food is {pizza}, and your favorite color is {color}'))
        print(f'Hello {name}, your favorite food is {pizza}, and your favorite color is {color}')
        self.name.text = ""
        self.pizza.text = ""
        self.color.text= ""




class TestApp(App):
    def build(self):
        return MyGridLayout()


if __name__ == '__main__':
    TestApp().run()