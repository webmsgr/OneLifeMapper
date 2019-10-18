import mitm
import multiprocessing as mp
import zlib
import argparse



class MapChunk: 
    def __init__(self,data=[[]],x=0,y=0):
        self.data = data
        self.x = x
        self.y = y
        self.ly = len(data)
        self.lx = len(data[0])
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
    return zlib.decompress(data)
def parser_worker(data): # parses map chunks
    pass 
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("server",help = "The address of the server in hostname:port formst",default="server1.onehouronelife.com:8006")
    parser.add_argument("host_port",help= "The port to host the server on",default="8007")
    parser.add_argument("-o",help="Where to output map chunks to")
    parser.add_argument("-i",help="Where to output a image of the map")
    data = parser.parse_args()
# flow
# func name in []
# -> [worker]packet from mitm 
# -> [worker]check if map 
# -> [zlib_decompress]decompress 
# -> [worker]send over to parser 
# -> [parser_worker]parse 
# -> [worker]return
