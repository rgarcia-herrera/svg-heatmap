# -*- coding: utf-8 -*-

import svgwrite
from svgwrite import cm, mm

from math import sin, cos, atan2, degrees, radians, tan, sqrt



class Cell:
    def __init__( self, insert=(0, 0), size=(10,10), text=None, **kwargs):
        self.insert = insert
        self.size   = size
        self.dwg    = svgwrite.Drawing()
        self.text   = text
        self.attrs  = kwargs

    def draw( self ):
        self.dwg.add( self.dwg.rect( insert = self.insert,
                                     size   = self.size,
                                     **self.attrs ))
        if self.text:
            insert = (self.insert[0]+20, self.insert[1]+20)
            self.dwg.add(self.dwg.text(self.text, insert=insert, font_size="4"))

        

    def getDwg(self):
        self.draw()
        return self.dwg

    
class Heatmap:

    def __init__( self, filename, keys, pairs):
        self.keys  = keys
        self.pairs = pairs
        self.dwg   = svgwrite.Drawing(filename=filename, debug=True)
           
    def save(self):
        self.dwg.save()

    def draw(self):
        # draw cells
        y = 0
        width = 100
        vlabels = []
        for i in range(len(self.keys)):
            vlabels.append(self.keys[i])
            hlabels = []
            x = 0
            for j in range(i):
                hlabels.append(self.keys[j])
                c = Cell( insert=(x,y), size=(width, width),
                          text=str(self.pairs.get((self.keys[i],self.keys[j]), self.pairs.get( (self.keys[j],self.keys[i]))))+str((self.keys[i], self.keys[j])),
                          fill="white", stroke="black" )
                self.dwg.add( c.getDwg() )
                x += width
            y += width

        # draw labels
        y = 0
        width = 100
        for label in vlabels:
            self.dwg.add(
                self.dwg.text(label,
                              insert=insert,
                              font_size="4"))


            
        print vlabels,hlabels

