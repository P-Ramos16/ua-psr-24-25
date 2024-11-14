#!/usr/bin/env python
# --------------------------------------------------
# Miguel Riem Oliveira.
# PSR, September 2020.
# Adapted from https://stackabuse.com/basic-socket-programming-in-python/
# -------------------------------------------------
import socket
import time
import dog_lib
import json

dog = dog_lib.Dog()  # instantiate a new dog
dog = dog.initFromValues(name='Toby', age=7, color='brown')
dog.addBrother('Lassie')
dog.addBrother('Boby')
print('CLIENT: my dog has ' + str(dog))

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create TCP/IP socket
local_hostname = socket.gethostname()  # retrieve local hostname
local_fqdn = socket.getfqdn()  # get fully qualified hostname
ip_address = socket.gethostbyname(local_hostname)  # get the according IP address

server_address = (ip_address, 23456)  # bind the socket to the port 23456, and connect
sock.connect(server_address)
print ("connecting to %s (%s) with %s" % (local_hostname, local_fqdn, ip_address))

# define example data to be sent to the server
message = dog.toDict()

print ('Sending message: ' + str(message))
sock.sendall(bytes(json.dumps(message), "utf-8"))
time.sleep(2)  # wait for two seconds

sock.close()  # close connection