import mitm
import multiprocessing as mp
import zlib
import argparse


class Tile:
    def __init__(self,data="0 0 0 0 0"):
        self.data = data
        parsed = data.split(" ")
        self.x = parsed[0]
        self.y = parsed[1]
        self.biome = parsed[2]
        self.floor = parsed[3]
        self.contained = []
        on = parsed[4]
        out = []
        if "," in on:
            temp = []
            inside = on.split(",")
            container = inside.pop(0)
            for item in inside:
                if ";" in item:
                    temp2 = []
                    inside2 = item.split(";")
                    container2 = inside2.pop(0)
                    for item2 in inside2:
                        temp2.append(item2)
                    temp.append((container2,temp2))
                else: 
                    temp.append(item)
            out = (container,temp)
        else:
            out = (on,[])
        self.contained = out

def read_tutorial():
    tiles = {}
    lines = open("OneLifeData/tutorialMaps/tutorial1.txt").read().split("\n")
    for line in lines:
        if line.strip() == "":
            continue
        temp = Tile(line)
        if temp.x in tiles:
            tiles[temp.x][temp.y] = temp
        else:
            tiles[temp.x] = {}
            tiles[temp.x][temp.y] = temp
    return OHOLMap(tiles)


class OHOLMap:
    def __init__(self,data={}):
        self.data = data
    def settile(self,x,y,tile):
        if x in self.data:
            self.data[x][y] = tile
        else:
            self.data[x] = {}
            self.data[x][y] = tile
    def blanktile(self,x,y):
        return Tile("{0} {0} 0 0 0".format(x,y))
    def gettile(self,x,y):
        if x in self.data:
            if y in self.data[x]:
                return self.data[x][y]
        return self.blanktile(x,y)
        

class MapChunk: 
    def __init__(self,data=[[]],x=0,y=0):
        self.data = data
        self.x = x
        self.y = y
        self.ly = len(data)
        self.lx = len(data[0])
    def get(self,x,y):
        return self.data[y][x]
    def setitem(self,x,y,data):
        self.data[y][x] = data
    def setrow(self,y,data):
        self.data[y] = data
    def setcol(self,x,data):
        for n,data in enumerate(data):
            self.set(x,n,data)
    def __iter__(self):
        return iter(self.data)
  
def main():
    pass
def worker(): # takes packets from server, parses map chunks, converts to Tiles and sends them to caller
    pass
def zlib_decompress(data):
    return zlib.decompress(data)
def parser_worker(data): # parses map chunks
    pass 
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--server",help = "The address of the server in hostname:port format",default="server1.onehouronelife.com:8006")
    parser.add_argument("--port",help= "The port to host the server on",default="8007")
    parser.add_argument("-o",help="Where to output map chunks to")
    parser.add_argument("-i",help="Where to output a image of the map")
    parser.add_argument("--interactive",help="Allow for viewing of map in a pygame window",action="store_true")
    data = parser.parse_args()
# flow
# func name in []
# -> [worker]packet from mitm 
# -> [worker]check if map 
# -> [zlib_decompress]decompress 
# -> [worker]send over to parser 
# -> [parser_worker]parse 
# -> [worker]return
