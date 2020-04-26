#from threading import Thread
import launchpad_py as launchpad
import random
import sys
import time

lp = launchpad.LaunchpadMk2()
lp.Open(0,"Mk2")
lp.Reset()
lp.ButtonFlush()

#rond haut   :   104-111
#rond droite :   89-79-69-59-49-39-29-19
#ligne 1     :   81-88
#ligne 2     :   71-78
#ligne 3     :   61-68
#ligne 4     :   51-58
#ligne 5     :   41-48
#ligne 6     :   31-38
#ligne 7     :   21-28
#ligne 8     :   11-18

square = [81,82,83,84,85,86,87,88,
        71,72,73,74,75,76,77,78,
        61,62,63,64,65,66,67,68,
        51,52,53,54,55,56,57,58,
        41,42,43,44,45,46,47,48,
        31,32,33,34,35,36,37,38,
        21,22,23,24,25,26,27,28,
        11,12,13,14,15,16,17,18]


def colorSquare(R, G, B):
    for p in square:
        lp.LedCtrlRaw(p, R, G, B)

def rainbow(gb):
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
        time.sleep(0.01)
        colorSquare(CR,CG,CB)

while 1:
    but = lp.ButtonStateRaw()
    if but == [29, 127]:
        break
    if but != []:
	    print("event: "+str(but))
    rainbow(4)

lp.Reset()
lp.Close()
