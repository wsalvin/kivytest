from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color,Ellipse,Line
from random import random
from kivy.uix.button import Button

class MyWidgetWidget(Widget):
    def on_touch_down(self, touch):
        color=(random(),random(),random())
        with self.canvas:
            Color(*color)
            touch.ud['Line']=Line(points=(touch.x,touch.y),width=5)
    def on_touch_move(self, touch):
        touch.ud['Line'].points=touch.ud['Line'].points+[touch.x,touch.y]


class MyPaintApp(App):
    def build(self):
        parent=Widget()
        self.painter=MyWidgetWidget()
        clearbtn=Button(text="Clear")
        clearbtn.bind(on_release=self.clear_canvas)
        parent.add_widget(self.painter)
        parent.add_widget(clearbtn)
        return parent
    def clear_canvas(self,obj):
        self.painter.canvas.clear()

if __name__=="__main__":
    MyPaintApp().run()

