# @todo add mitm proxy
import select
import socket
import multiprocessing as mp
import threading


def main(saddr,cport,outpipe): # receves packets and sends them to the caller
    wk,data = mp.Pipe()
    sname,sport = saddr.split(":")
    server_worker_thread = threading.Thread(target=server_worker,args=(sname,sport,cport,wk))
    server_worker_thread.start()
    while server_worker_thread.is_alive():
        if data.poll():
            outpipe.send(data.recv())

def server_worker(sname,sport,cport,outpipe): # communicates with server/client
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
