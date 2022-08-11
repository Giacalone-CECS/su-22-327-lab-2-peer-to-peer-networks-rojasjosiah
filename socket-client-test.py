# socket-client-test.py

import time
import zmq
import nmap
import threading

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
	print("Host: " + each_host)							# prints Host: 172.48.0.2
	print(nm[each_host].all_protocols())					# prints ['tcp']
    
	if 'tcp' in nm[each_host].keys():
		open_ports = nm[each_host]['tcp'].keys()		# stores dict of the open ports
		print(open_ports)
		if 65432 in open_ports:                 # uses int for dict vals
			print(each_host + " has int port 65432")
			peers.append((each_host, '65432'))
	else:
		print(each_host + " doesn't have tcp")

threads = []
print(peers)


for peer in peers:			# creates a thread for each publisher
	threads.append(threading.Thread(target=establish_subscribe, args=(peer[0], port,), daemon=True))
print(threads)
for t in threads:
	t.start()

for t in threads:
	t.join()




