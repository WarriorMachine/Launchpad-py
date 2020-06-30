from threading import Thread
import launchpad_py as launchpad
import time

lp = launchpad.LaunchpadMk2()
lp.Open(0,"Mk2")
lp.Reset()
lp.ButtonFlush()

values = dict()
values["stat"] = True    #off/on
values["indicator"] = 8  #deep lvl color
values["flush"] = 1      #reset button memory
values["v"] = 0          #numb/checker of "lineXX"
values["%gradient"] = 1  #value gradient of your color
values["delay"] = 0.005  #refresh delay

class launch(Thread):
    def __init__(self, arg):
        Thread.__init__(self)
        self.arg = arg
        self.line00 = [111,89]
        self.line01 = [110,88,79]
        self.line02 = [109,87,78,69]
        self.line03 = [108,86,77,68,59]
        self.line04 = [107,85,76,67,58,49]
        self.line05 = [106,84,75,66,57,48,39]
        self.line06 = [105,83,74,65,56,47,38,29]
        self.line07 = [104,82,73,64,55,46,37,28,19]
        self.line08 = [81,72,63,54,45,36,27,18]
        self.line09 = [71,62,53,44,35,26,17]
        self.line10 = [61,52,43,34,25,16]
        self.line11 = [51,42,33,24,15]
        self.line12 = [41,32,23,14]
        self.line13 = [31,22,13]
        self.line14 = [21,12]
        self.line15 = [11]

    def on(self):
        while values["stat"]:
            self.rainbow(2*int(values["indicator"]))
        self.off()

    def off(self):
        lp.Reset()
        while not values["stat"]:
            pass
        self.on()

    def run(self):
        if self.arg == "rainbow":
            if values["stat"]:
                self.on()
        if self.arg == "loop":
            while 1:
                self.checker()

    def colorSquare(self, R, G, B, n):
        if n == 0:
            for p in self.line00:
                lp.LedCtrlRaw(p, R, G, B)
        elif n == 1:
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
        time.sleep(values["delay"])

    def rainbow(self, gb):
        CR = gb
        CG = 0
        CB = gb
        plus = values["%gradient"]
        self.masterTab = []
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
            self.masterTab.append([CR,CG,CB])
        for c in self.masterTab:
            count = 0
            if values["stat"]:
                for l in self.masterTab[0:16]:
                    self.colorSquare(l[0],l[1],l[2],count)
                    count += 1
            del self.masterTab[0]

    def checker(self):
        but = lp.ButtonStateRaw()
        if but != []:
            if but == [49, 127]:
                quit()
            elif but == [111, 127]:
                if values["stat"]:
                    values["stat"] = False
                else: 
                    values["stat"] = True
        else:
            values["flush"] = int(values["flush"])+1
            if values["flush"] == 100000:
                lp.ButtonFlush()
                values["flush"] = 1

thread_1 = launch("rainbow")
thread_2 = launch("loop")

thread_1.start()
thread_2.start()
