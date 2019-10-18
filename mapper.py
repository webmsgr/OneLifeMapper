import mitm
import multiprocessing
import zlib

class MapChunk: 
    def __init__(self,data=[[]],lx=0,ly=0):
        self.data = data
    def get(x,y):
        return self.data[y][x]
    def set(x,y,data):
        self.data[y][x] = data
    def setrow(y,data):
        self.data[y] = data
    def setcol(x,data):
        for n,data in enumerate(data):
            self.set(x,n,data)
    def __iter__(self):
        return iter(self.data)
  
def main():
    pass
def worker(): # takes packets from server, parses map chunks, converts to MapChunks and sends them to caller
    pass
def zlib_decompress(data):
    pass
def parser_worker(data): # parses map chunks
    pass 

# flow
# func name in []
# -> [worker]packet from mitm 
# -> [worker]check if map 
# -> [zlib_decompress]decompress 
# -> [worker]send over to parser 
# -> [parser_worker]parse 
# -> [worker]return
