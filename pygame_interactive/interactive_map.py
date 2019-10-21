import pygame
import math
tilesize = 128 # pixels per tile

def tiletosurface(tile):
    pass

def maptosurface(sx,sy,ex,ey,oholmap):
    pass

def main(windowsize,tilepipe,OHOLMap):
    wt = math.floor(windowsize/tilesize)
    cx,cy,first = 0,0,True
    if OHOLMap.data != {}:
       for x in OHOLMap.data:
           for y in OHOLMap.data[x]:
                if not first:
                    break
                cx,cy = x,y
                first = False
    pass
