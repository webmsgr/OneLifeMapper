# @todo add map program
import mitm
import multiprocessing

class MapChunk: 
    def __init__(self,data=[[]]):
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
