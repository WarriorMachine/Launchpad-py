from threading import Thread
import launchpad_py as launchpad
import random
import sys
import time

lp = launchpad.LaunchpadMk2()
lp.Open(0,"Mk2")
lp.Reset()
lp.ButtonFlush()

values = dict()
values["indicator"] = 1

def base():
    lp.LedCtrlRaw(105, 16, 0, 1)
    lp.LedCtrlRaw(104, 0, 16, 6)
    lp.LedCtrlRaw(19, 2, 0, 3)

class launch():
    def __init__(self):
        self.indicator = [19,29,39,49,59,69,79,89]

    def colorBarMax(self, R, G, B, num):
        for p in self.indicator[0:num]:
            lp.LedCtrlRaw(p, R, G, B)

    def colorBarMin(self, R, G, B, num):
        num = 8-num
        for p in self.indicator[-num:]:
            lp.LedCtrlRaw(p, R, G, B)

a = launch()
base()

while 1:
    but = lp.ButtonStateRaw()
    if but != []:
        if but == [49, 127]:
            quit()
        if but == [105, 127]:
            if values["indicator"] == 1:
                lp.LedCtrlRaw(105, 64, 32, 0)
                time.sleep(0.25)
                lp.LedCtrlRaw(105, 16, 0, 1)
                time.sleep(0.25)
                lp.LedCtrlRaw(105, 64, 32, 0)
                time.sleep(0.25)
                lp.LedCtrlRaw(105, 16, 0, 1)
            else:
                values["indicator"] = int(values["indicator"])-1
                a.colorBarMin(0, 0, 0, values["indicator"])
        if but == [104, 127]:
            if values["indicator"] == 8:
                lp.LedCtrlRaw(104, 64, 32, 0)
                time.sleep(0.25)
                lp.LedCtrlRaw(104, 0, 16, 6)
                time.sleep(0.25)
                lp.LedCtrlRaw(104, 64, 32, 0)
                time.sleep(0.25)
                lp.LedCtrlRaw(104, 0, 16, 6)
            else:
                values["indicator"] = int(values["indicator"])+1
                a.colorBarMax(2, 0, 3, values["indicator"])

lp.Reset()
lp.Close()
