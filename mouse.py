from tkinter import VERTICAL
import sys, math
from direct.showbase.ShowBase import ShowBase
from pandac.PandaModules import *
from direct.gui.DirectGui import *
loadPrcFile("conf.prc")

keyMap = {
    "red": False,
    "green": False,
    "pink": False,
    "yellow": False,
    "orange": False,
    "blue": False,
}
keyMap2= {
    "shift": True,
    "darkmood": False

}

def updateKeyMap(key):
    
    for i in keyMap:
        if i == key:
            if keyMap[i]:
                keyMap[i] = False
                continue

            keyMap[i] = True
            continue

        else:
            keyMap[i] = False
        


def updateKeyMap2(key):
        if keyMap2[key] == True:
            keyMap2[key] = False
        else:
            keyMap2[key] = True



class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.lens = OrthographicLens()
        self.lens.setFilmSize(10,10)
        self.camNode.setLens(self.lens)
        self.point = False
        self.setBackgroundColor(0.1,0.1,0.1,1)
        self.segs = LineSegs("lines")
        self.x = 0
        self.y = 0
        self.taskMgr.add(self.update, "update")
        self.accept("r", updateKeyMap, ["red"])


        self.accept("g", updateKeyMap, ["green"])

        self.accept("b", updateKeyMap, ["blue"])

        
        self.accept("p", updateKeyMap, ["pink"])

        self.accept("o", updateKeyMap, ["orange"])

        self.accept("y", updateKeyMap, ["yellow"])

        self.accept("d", updateKeyMap2, ["darkmood"])

        self.accept("shift", updateKeyMap2, ["shift"])

        self.colors = [[0.40,0.01,0.05,1], [1,1,1,1]]
        self.point2 = True
        self.font = self.loader.loadFont("Wbxkomik.ttf")





        self.slider = DirectSlider(range=(1, 10), value=1, pageSize=1, command=self.showValue, orientation=VERTICAL)
        self.value = int(self.slider["value"])

        self.slider.setScale(0.5)
        self.slider.setPos(1.6,0,0)

    # def mouseClick(self):
    #     if not self.point: 
    #          x = round(self.mouseWatcherNode.getMouseX(), 3)
    #          y = round(self.mouseWatcherNode.getMouseY(), 3)
    #          self.x = x
    #          self.y = y
    #          self.point = True
    #          return 
    #     if base.mouseWatcherNode.hasMouse():
    #         x = round(self.mouseWatcherNode.getMouseX(), 3)
    #         y = round(self.mouseWatcherNode.getMouseY(), 3)
    #         self.segs = LineSegs("lines")
    #         self.segs.setColor(0.1,0.1,0.1 ,1)
    #         self.segs.drawTo(self.x,self.y, self.y)
    #         self.segs.drawTo(x, y, y)
    #         self.x = x
    #         self.y = y
    #         self.segsnode = self.segs.create(False)
    #         render2d.attachNewNode(self.segsnode)

    #         print(x, y)
    #         md2= self.win.getPointer(0)

    #         print(md2.getX(), md2.getY())

            # get the mouse position
        self.genLabelText("[SHIFT]: to start/stop drawing", 1)
        self.genLabelText("[G]: green", 2)
        self.genLabelText("[B]: blue", 3)
        self.genLabelText("[P]: pink", 4)
        self.genLabelText("[O]: orange", 5)
        self.genLabelText("[Y]: yellow", 6)
        self.genLabelText("[R]: red", 7)
        self.genLabelText("[D]: dark/light mood", 8)

    def showValue(self):
        self.segs.setThickness(self.slider['value'])


    def genLabelText(self, text, i):
        if keyMap2["darkmood"]:
            fgcolor = (0.1,0.1,0.1,1)
        else:
            fgcolor = (1,1,1,1)
        return OnscreenText(text=text, parent=base.a2dTopLeft, scale=.05,
                        pos=(0.06, -.08 * i), fg=fgcolor,
                        shadow=(0, 0, 0, 1), align=TextNode.ALeft, font = self.font)

    def update(self, task):
        if not keyMap2["shift"]:
            self.point2 = False
            color = (1,1,1,1)
            self.setBackgroundColor(0.1,0.1,0.1,1)

            if keyMap2["darkmood"]:
                self.setBackgroundColor(0.949,0.898,0.874,1)

            if keyMap["red"]:
                color = (0.870, 0.05, 0.07, 1)
            elif keyMap["green"]:
                color = (0.207,0.611,0.356,1)
            elif keyMap["blue"]:
                color = (0.298,0.45,0.780,1)
            elif keyMap["pink"]:
                color = (0.878,0.345,0.737,1)
            elif keyMap["orange"]:
                color = (0.760,0.345,0.168,1)
            elif keyMap["yellow"]:
                color = (0.760,0.686,0.219,1)
            
            if self.mouseWatcherNode.hasMouse():
                if not self.point:
                    x = self.mouseWatcherNode.getMouseX()
                    y = self.mouseWatcherNode.getMouseY()
                    self.x = x
                    self.y = y
                    self.point = True
                    return task.cont
                x = self.mouseWatcherNode.getMouseX()
                y = self.mouseWatcherNode.getMouseY()
                self.segs.setColor(color)
                self.segs.drawTo(self.x,self.y, self.y)
                self.segs.drawTo(x, y, y)
                self.x = x
                self.y = y
                self.segsnode = self.segs.create(False)
                render2d.attachNewNode(self.segsnode)
                # print(x,y)

            return task.cont
        if not self.point2:
            if self.mouseWatcherNode.hasMouse():

                x = self.mouseWatcherNode.getMouseX()
                y = self.mouseWatcherNode.getMouseY()
                self.x = x
                self.y = y
                self.point = True
                return task.cont
        
        return task.cont

            
app = MyApp()
app.run()
