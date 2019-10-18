# @todo add mitm proxy
import select
import socket
import multiprocessing
import threading



def main(): # receves parsed map data and does things
    pass

  
def task_manager(): # creates threads and the parsing pool and sends parsed map data back to the main thread
    pass

def server_worker(): # communicates with server/client
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
