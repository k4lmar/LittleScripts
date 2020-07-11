'''
Req.:
- Python 3.x
- pynput lib (
              install command in CMD:
              python -m pip install pynput
              )
This script allow you to spamming a spell (a keyboard key)
in games like World of Warcraft. The spam cycle is around 1/100 sec.
It simulates press and release so if your spell cooldown is over,
the spell will be casted again.
This script is suited for Druid with ALT-1,2,3,4 formchange hotkeys.
'''

import pynput
import time

class btnsmash():
    def __init__(self):
        self.keyb=pynput.keyboard
        self.listener=self.keyb.Listener(on_press=self.on_press,
                                         on_release=self.on_release)
        self.btn=False
        self.btnkey=None
        self.alt_pressed=False
        self.mainswitch=True
        
    def on_press(self, key):
        try:
                                #exception keys, like move, backpack, spellbook...
            if (key.char not in "wasdbcmlpv"
                and key.char!=None):
                keychange=False
                #If I change spammable key, the listener must be stopped.
                if key.char!=self.btnkey:
                    self.listener.stop()
                    self.btnkey=key.char
                    keychange=True
                #Whenever i use formchange, pause spam.
                if (self.alt_pressed == True):
                    if (self.btnkey in '1234'):
                        self.btn=False
                    else: self.btn=True
                else: self.btn=True
                if keychange:
                    self.listener=self.keyb.Listener(on_press=self.on_press,
                                                     on_release=self.on_release)
                    self.listener.start()
        except:
            #Left CTRL is spam start/pause button
            if key == self.keyb.Key.ctrl_l:
                self.mainswitch=True
                if self.btn==False:
                    self.btn=True
                else: self.btn=False
            elif key == self.keyb.Key.alt_l:
                self.alt_pressed=True
            #Enter is a safety "off spam" key, if I want to use ingame chat
            elif key==self.keyb.Key.enter:
                if self.mainswitch==False:
                    pass
                else: self.mainswitch=False
                
    def on_release(self, key):
        try:
            if key.char=='0':
                pass
        except:
            if key == self.keyb.Key.alt_l:
                self.alt_pressed=False
                
    def run(self):
        self.listener.start()
        while True:
            if self.btnkey != None and self.btn==True and self.mainswitch==True:
                self.keyb.Controller().press(self.btnkey)
                self.keyb.Controller().release(self.btnkey)
            time.sleep(10/1000)
btn=btnsmash()
btn.run()
