from threading import Thread
import launchpad_py as launchpad
import time

lp = launchpad.LaunchpadMk2()
lp.Open(0,"Mk2")
lp.Reset()
lp.ButtonFlush()

values = dict()
values["stat"] = True
values["indicator"] = 1
values["flush"] = 1

class launch(Thread):
    def __init__(self, arg):
        Thread.__init__(self)
        self.arg = arg
        self.square = [81,82,83,84,85,86,87,88,
                        71,72,73,74,75,76,77,78,
                        61,62,63,64,65,66,67,68,
                        51,52,53,54,55,56,57,58,
                        41,42,43,44,45,46,47,48,
                        31,32,33,34,35,36,37,38,
                        21,22,23,24,25,26,27,28,
                        11,12,13,14,15,16,17,18]
        self.indicator = [19,29,39,49,59,69,79,89]

    def base(self):
        lp.LedCtrlRaw(105, 16, 0, 1)
        lp.LedCtrlRaw(104, 0, 16, 6)
        self.colorBarMax(2, 0, 3, values["indicator"])

    def on(self):
        self.base()
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

    def colorSquare(self, R, G, B):
        for p in self.square:
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
            self.colorSquare(CR,CG,CB)

    def colorBarMax(self, R, G, B, num):
        for p in self.indicator[0:num]:
            lp.LedCtrlRaw(p, R, G, B)

    def colorBarMin(self, R, G, B, num):
        num = 8-num
        for p in self.indicator[-num:]:
            lp.LedCtrlRaw(p, R, G, B)

    def checker(self):
        but = lp.ButtonStateRaw()
        if but != []:
            if but == [49, 127]:
                quit()
            elif but == [105, 127]:
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
                    self.colorBarMin(0, 0, 0, values["indicator"])
            elif but == [104, 127]:
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
                    self.colorBarMax(2, 0, 3, values["indicator"])
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
