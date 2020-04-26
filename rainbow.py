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
values["v"] = 2
values["Stat"] = True

class launch(Thread):
    def __init__(self, lettre):
        Thread.__init__(self)
        self.lettre = lettre
        self.square = [81,82,83,84,85,86,87,88,
                        71,72,73,74,75,76,77,78,
                        61,62,63,64,65,66,67,68,
                        51,52,53,54,55,56,57,58,
                        41,42,43,44,45,46,47,48,
                        31,32,33,34,35,36,37,38,
                        21,22,23,24,25,26,27,28,
                        11,12,13,14,15,16,17,18]

    def run(self):
        if self.lettre == "1":
            while values["Stat"]:
                self.checker()
        elif self.lettre == "2":
            while values["Stat"]:
                self.rainbow(values["v"])

    def colorSquare(self, R, G, B):
        for p in self.square:
            lp.LedCtrlRaw(p, R, G, B)
        if values["Stat"] == False:
            lp.Reset()

    def rainbow(self, gb):
        CR = gb
        CG = 0
        CB = gb
        plus = 1
        for nm in range(1, gb**3):
            if CR >= gb and CG < gb:
                CG += plus
                CB -= plus
            elif CG >= gb and CB < gb:
                CB += plus
                CR -= plus
            elif CB >= gb and CR < gb:
                CR += plus
                CG -= plus
            self.colorSquare(CR,CG,CB)

    def checker(self):
        but = lp.ButtonStateRaw()
        if but != []:
	        print("event: "+str(but))
        if but == [49, 127]:
            self.stop()
        if but == [19, 127]:
            values["v"] = int(values["v"])/2
            print(values["v"])
        if but == [29, 127]:
            values["v"] = int(values["v"])*2
            print(values["v"])

    def stop(self):
        values["Stat"] = False
        quit()

thread_1 = launch("1")
thread_2 = launch("2")

thread_1.start()
thread_2.start()
