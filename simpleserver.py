#!/usr/bin/python

# btpeer.py

import socket
import struct
import threading
import time
import traceback
 
class Server :
    def __init__( self, serverport='0', myid=None, serverhost = None ,backlog=1):
        
      	self.serverport = int(serverport)
	self.serverhost = (serverhost)
	print self.serverport
        print self.serverhost
        self.myid=myid
        print myid
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM )
	#s.setsockopt( socket.SOL_SOCKET, socket.SO_REUSEADDR, 1 )
        print "bind IP adrress "
        print serverhost
        print "with port "
        print serverport
        s.bind(('',self.serverport))
	
	print " creating a server socket..."
	s.listen( backlog )
	#s.setblocking(0)
	while 1:
          print "Server waiting........"
          clientsock, clientaddr = s.accept()
          print "got connection request from clientaddr",clientaddr
	  clientsock.send("Thankyou for connecting...")
          clientsock.close()
