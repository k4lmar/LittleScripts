from pynput import keyboard
import time
class doomrun():
    def __init__(self):
        self.kb=keyboard
        self.running=False
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
        self.l=self.kb.Listener(on_press=self.onp)
        self.l.start()
        while True:
            time.sleep(10/100)
dr=doomrun()
dr.run()
