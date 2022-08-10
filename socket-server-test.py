# socket-server-test.py

import time
import zmq

HOST = "0.0.0.0"  
""" weird docker things. can't bind to traditional localhost address,
but using 0.0.0.0 works. And for whatever reason, you can't use 
DNS specifically for bind with zmq (even though you can with socket)
but you can with connect. """
PORT = "65432"  # Port to listen on 


def establish_publish():
    context = zmq.Context()
    s = context.socket(zmq.PUB)     # creates publisher socket
    p = "tcp://" + HOST + ":" + PORT
    s.bind(p)						# binds socket to specified port
    while True:						# sends messages every 5 seconds
        time.sleep(5)
        s.send(bytes("Time: " + time.asctime(), 'utf-8'))


establish_publish()
