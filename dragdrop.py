'''
Rapid Script
============

This is a drag and drop script creating app. It's purpose is to allow
quick bash script creation.  Its a work in progress, suggestions welcome.

'''
import kivy
kivy.require('1.4.2')
import time
import operator
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty
from kivy.vector import Vector
#import os
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.codeinput import CodeInput
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.graphics import Color, Ellipse
from kivy.graphics import Rectangle
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.button import Button
from kivy.uix.scatter import Scatter

class IfStatement(Widget):
    pass
#TODO  use ButtonBehavior with on_press/on_release if you need collision detection.
class Print(Widget):
    pass
           

class RapidScriptMain(Widget):

    # box1 = ObjectProperty(None)
    # box2 = ObjectProperty(None)
    #btn1 = Button(text='Hello world 1',pos=(10,10), size=(30,30))
    #btn1.bind(state=makeRect)

    def init(self):
        box1 = Print()
        scatter = Scatter(do_rotation=False, do_scale=False,
                          do_translation_y=False)
        scatter.add_widget(Print(pos=(10,10)))
        scatter.add_widget(IfStatement())
        self.prevId = None

    

class RapidScriptApp(App):
    def build(self):
        rsMain = RapidScriptMain()
        rsMain.init()
        return rsMain

if __name__ == "__main__":
    RapidScriptApp().run()