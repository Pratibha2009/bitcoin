#!/usr/bin/python



from mininet.net import Mininet
import socket


class client :
    def __init__( self, serverhost = None, serverport='0', clientIP=None ):
      s = socket.socket( socket.AF_INET, socket.SOCK_STREAM)
      #now connect to the server on port serverport
      # - the normal http port
      print "I am in client file.."
      print serverhost
      print serverport
      s.connect((serverhost,serverport))
      
      print s.recv(1024)
      s.close()
