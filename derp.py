from kivy.uix.label import Label
from kivy.app import App
from kivy.uix.behaviors import DragBehavior
from kivy.lang import Builder
from kivy.graphics import *
with self.canvas:
    # Add a red color
    Color(1., 0, 0)

    # Add a rectangle
    Rectangle(pos=(10, 10), size=(500, 500))

# You could also put the following in your kv file...
kv = '''
<DragLabel>:
    # Define the properties for the DragLabel
    drag_rectangle: self.x, self.y, self.width, self.height
    drag_timeout: 10000000
    drag_distance: 0

FloatLayout:
    # Define the root widget
    DragLabel:
        size_hint: 0.25, 0.2
        text: 'Drag me'
'''


class DragLabel(DragBehavior, Label):
    pass


class TestApp(App):
    def build(self):
	with self.canvas:
	 # Add a red color
         Color(1., 0, 0)
    # Add a rectangle
         Rectangle(pos=(10, 10), size=(500, 500))

        return Builder.load_string(kv)

TestApp().run()
