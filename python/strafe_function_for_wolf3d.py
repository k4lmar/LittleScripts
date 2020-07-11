'''
Req.:
- Python 3.x
- pynput lib (
              install command in CMD:
              python -m pip install pynput
              )

This script allow you to strafe move in
Wolf3D with a single A or D keyboard button.
'''
import pynput
import time
class Strafe4W3d():
    def __init__(self):
        self.keyb=pynput.keyboard
        self.listener=self.keyb.Listener(on_press=self.on_press,
                                         on_release=self.on_release)
        self.btn=None
        self.holddown=False
    def on_press(self, key):
        try:
            if key.char in "ad" and self.holddown==False:
                self.holddown=True
                self.btn=key.char
        except:
            pass
    def on_release(self, key):
        try:
            if key.char in "ad":
                self.holddown=False
        except:
            pass
    def run(self):
        #keyboard listener start
        self.listener.start()
        print('Started.. A and D buttons activate ALT button.')
        while True:
            #ALT button is the default strafe key in Wolf3D
            if self.btn!=None and self.holddown==True:
                self.keyb.Controller().press(self.keyb.Key.alt)
            if self.holddown==False:
                self.keyb.Controller().release(self.keyb.Key.alt)
            time.sleep(10/1000)
Strafe4W3d().run()
