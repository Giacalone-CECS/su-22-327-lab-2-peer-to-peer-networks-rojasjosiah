# node.py

import time
import zmq
import nmap
import threading
import socket

#### SERVER ###

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
        s.send(bytes("FROM " + socket.gethostbyname(socket.gethostname()) + ": Time: " + time.asctime(), 'utf-8'))

threading.Thread(target=establish_publish).start()
#establish_publish()
#######

host = "server"  # can use DNS here (container name) or actual address
port = "65432"  # The port used by the server


def establish_subscribe(host, port):
	context = zmq.Context()			# establishes zmq context
	s = context.socket(zmq.SUB)     # creates subscriber socket
	p = "tcp://" + host + ":" + port
	s.connect(p)
	s.setsockopt(zmq.SUBSCRIBE, b"")		# looks for publishes starting with those bytes
	for i in range(5):		
		curr_time = s.recv()
		print(curr_time.decode())


nm = nmap.PortScanner()
nm.scan('172.48.0.0/24', '11111-65435')		# needs wide range for some reason (was bugging)

peers = []

for each_host in nm.all_hosts():
	if 'tcp' in nm[each_host].keys():
		open_ports = nm[each_host]['tcp'].keys()		# stores dict of the open ports

		if 65432 in open_ports:                 # uses int for dict vals

			peers.append((each_host, '65432'))


threads = []

for peer in peers:			# creates a thread for each publisher
	if not peer[0] == socket.gethostbyname(socket.gethostname()): # don't connect to yourself
		threads.append(threading.Thread(target=establish_subscribe, args=(peer[0], port,), daemon=True))
for t in threads:
	t.start()

for t in threads:
	t.join()




