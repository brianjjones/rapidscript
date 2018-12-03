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

class IfStatement(Widget):
    pass
#TODO  use ButtonBehavior with on_press/on_release if you need collision detection.
class Print(Widget):
    def on_touch_down(self, touch):
        #if self.collide_point(*touch.pos):
        if self.collide_point(touch.x, touch.y):
            print ("down")
            with self.canvas:
                Color(1, 0, 1)
                d = 30
                Print(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d*2))
        print ("fail")
        return super(Print, self).on_touch_down(touch)
           

class RapidScriptMain(Widget):
    box1 = ObjectProperty(None)
    box2 = ObjectProperty(None)
    btn1 = Button(text='Hello world 1',pos=(10,10), size=(30,30))
    #btn1.bind(state=makeRect)

    def init(self):
        self.prevId = None

    def on_press(self):
        print ("Master")
        with self.canvas:
            Color(1, 0, 0)
            d = 30
            if self.prevId is not None:
                self.prevId.width+=100
            #Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
            myid = Print(pos=(200, 200), size=(40, 40))
            self.prevId=myid
            


class RapidScriptApp(App):
    def build(self):
        rsMain = RapidScriptMain()
        rsMain.init()
        return rsMain

if __name__ == "__main__":
    RapidScriptApp().run()