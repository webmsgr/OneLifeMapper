import pygame
import math
import glob
import os
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
    print("Loading sprites")
    sprites = glob.glob("./OneLifeData/sprites/*.tga")
    loadedsprites = {}
    print("Found {} sprites, loading...".format(len(sprites)))
    for sprite in sprites:
        spriteid = os.path.basename(sprite).split(".")[0]
        loadedsprites[spriteid] = pygame.image.load(sprite)
        
    # do other loading things...
    tilepipe.send("READY")
    # main loop goes here
