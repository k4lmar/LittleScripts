'''
Req.:
- Python 3.x
- pynput lib (
              install command in CMD:
              python -m pip install pynput
              )

This script allow you to toggle walk/run
in games like (old dos) Doom 1 and 2, which do not
have always-run feature.
It starts a keyboard listener and
if I press left ALT it will change
left SHIFT press/release status.
Left SHIFT is default run key in Doom games.
'''
from pynput import keyboard
import time
class DoomRun():
    def __init__(self):
        self.kb=keyboard
        self.running=False

    #This func will be called, whenever a keyboard key is pressed.
    def onp(self, key):
        try:
            if key==self.kb.Key.alt_l:
                if self.running==False:
                    self.running=True
                    self.kb.Controller().press(self.kb.Key.shift_l)
                else:
                    self.running=False
                    self.kb.Controller().release(self.kb.Key.shift_l)
        except:
            pass
    def run(self):
        print('Started.\nLeft ALT is the run/walk (=left SHIFT press/release) toggle button')
        #Set and start a keyboard listener.
        self.l=self.kb.Listener(on_press=self.onp)
        self.l.start()
        while True:
            time.sleep(10/100)
dr=DoomRun()
dr.run()
