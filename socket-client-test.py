# socket-client-test.py

import time
import zmq

HOST = "server"  # can use DNS here (container name) or actual address
PORT = "65432"  # The port used by the server


def establish_subscribe():
    context = zmq.Context()			# establishes zmq context
    s = context.socket(zmq.SUB)     # creates subscriber socket
    p = "tcp://" + HOST + ":" + PORT
    s.connect(p)
    s.setsockopt(zmq.SUBSCRIBE, b"T")		# looks for publishes starting with those bytes
    for i in range(5):		
        curr_time = s.recv()
        print(curr_time.decode())


establish_subscribe()
