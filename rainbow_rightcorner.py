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
values["v"] = 0
values["sous"] = 1

class launch():
    def __init__(self):
        self.line01 = [88]
        self.line02 = [87,78]
        self.line03 = [86,77,68]
        self.line04 = [85,76,67,58]
        self.line05 = [84,75,66,57,48]
        self.line06 = [83,74,65,56,47,38]
        self.line07 = [82,73,64,55,46,37,28]
        self.line08 = [81,72,63,54,45,36,27,18]
        self.line09 = [71,62,53,44,35,26,17]
        self.line10 = [61,52,43,34,25,16]
        self.line11 = [51,42,33,24,15]
        self.line12 = [41,32,23,14]
        self.line13 = [31,22,13]
        self.line14 = [21,12]
        self.line15 = [11]


    def colorSquare(self, R, G, B, n):
        if n == 1:
            for p in self.line01:
                lp.LedCtrlRaw(p, R, G, B)
        elif n == 2:
            for p in self.line02:
                lp.LedCtrlRaw(p, R, G, B)
        elif n == 3:
            for p in self.line03:
                lp.LedCtrlRaw(p, R, G, B)
        elif n == 4:
            for p in self.line04:
                lp.LedCtrlRaw(p, R, G, B)
        elif n == 5:
            for p in self.line05:
                lp.LedCtrlRaw(p, R, G, B)
        elif n == 6:
            for p in self.line06:
                lp.LedCtrlRaw(p, R, G, B)
        elif n == 7:
            for p in self.line07:
                lp.LedCtrlRaw(p, R, G, B)
        elif n == 8:
            for p in self.line08:
                lp.LedCtrlRaw(p, R, G, B)
        elif n == 9:
            for p in self.line09:
                lp.LedCtrlRaw(p, R, G, B)
        elif n == 10:
            for p in self.line10:
                lp.LedCtrlRaw(p, R, G, B)
        elif n == 11:
            for p in self.line11:
                lp.LedCtrlRaw(p, R, G, B)
        elif n == 12:
            for p in self.line12:
                lp.LedCtrlRaw(p, R, G, B)
        elif n == 13:
            for p in self.line13:
                lp.LedCtrlRaw(p, R, G, B)
        elif n == 14:
            for p in self.line14:
                lp.LedCtrlRaw(p, R, G, B)
        elif n == 15:
            for p in self.line15:
                lp.LedCtrlRaw(p, R, G, B)

    def rainbow(self, gb):
        CR = gb
        CG = 0
        CB = gb
        plus = 1
        for nm in range(1, gb*3):
            if CR >= gb and CG < gb:
                CG += plus
                CB -= plus
            elif CG >= gb and CB < gb:
                CB += plus
                CR -= plus
            elif CB >= gb and CR < gb:
                CR += plus
                CG -= plus

            if values["v"] == 16:
                values["v"] = 1
            self.colorSquare(CR,CG,CB,values["v"])
            values["v"] += 1
            time.sleep(0.025)

a = launch()

while 1:
    a.rainbow(33) #ou 3