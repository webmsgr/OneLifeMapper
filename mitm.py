# @todo add mitm proxy
import select
import socket
import multiprocessing
import threading

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

def main(): # receves parsed map data and does things
    pass

  
def task_manager(saddr,caddr,outpipe): # creates threads and the parsing pool and sends parsed map data back to the main thread
    pass

def server_worker(saddr,caddr,outpipe): # communicates with server/client
    pass

def map_worker(data): # parses map data
    pass

def Server(pipe,msocket): # copied from bot, communicates
    msocket.setblocking(0)
    while True:
        try:
            read,write,error  = select.select([msocket],[msocket],[msocket],60)
            if msocket in read:
                buf = msocket.recv(2048)
                pipe.send(buf)
            if pipe.poll() and msocket in write:
                msocket.send(pipe.recv())
             if msocket in error:
                break
        except:
            break
