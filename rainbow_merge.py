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
        self.square = [81,82,83,84,85,86,87,88,
                        71,72,73,74,75,76,77,78,
                        61,62,63,64,65,66,67,68,
                        51,52,53,54,55,56,57,58,
                        41,42,43,44,45,46,47,48,
                        31,32,33,34,35,36,37,38,
                        21,22,23,24,25,26,27,28,
                        11,12,13,14,15,16,17,18]


    def colorSquare(self, R, G, B, n):
        if n < 0:
            n = 8-n
        for p in self.square[8*n:8*(n+1)]:
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

            if values["v"] == 7:
                values["sous"] = -1
            elif values["v"] == -7:
                values["sous"] = 1
            self.colorSquare(CR,CG,CB,values["v"])
            values["v"] += values["sous"]
            time.sleep(0.01)

a = launch()

while 1:
    a.rainbow(16)