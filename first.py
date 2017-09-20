import kivy
import time

from datetime import time
from kivy.app import App
from kivy.core.text import LabelBase
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.clock import Clock
from time import gmtime,strftime

Window.clearcolor = get_color_from_hex('#101216')

LabelBase.register(name="Roboto",
	fn_regular="Roboto-Thin.ttf",
	fn_bold="Roboto-Medium.ttf")

class ClockApp(App):

	def update_time(self, nap):
		self.root.ids.time.text = strftime('[b]%H[/b]:%M:%S')
	
	def on_start(self):
		Clock.schedule_interval(self.update_time, 1)
		
	pass

if __name__ == '__main__':
	ClockApp().run()
