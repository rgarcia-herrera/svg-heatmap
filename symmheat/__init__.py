# -*- coding: utf-8 -*-

import svgwrite
from svgwrite import cm, mm

from math import sin, cos, atan2, degrees, radians, tan, sqrt



class Cell:
    def __init__( self, insert=(0, 0), size=(10,10), value=0, show_value=False, **kwargs):
        self.insert= insert
        self.size  = size
        self.dwg   = svgwrite.Drawing()
        self.attrs = kwargs

    def draw( self ):
        self.dwg.add( self.dwg.rect( insert = self.insert,
                                     size   = self.size,
                                     **self.attrs ))
        #if show_value:
        #    pass
        

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
        y = 0
        width = 10
        for i in self.keys:
            x = 0
            for j in self.keys:
                c = Cell( insert=(x,y), size=(width, width),
                          value=self.pairs.get((i,j)))
                self.dwg.add( c.getDwg() )
                x += width
            y += width
