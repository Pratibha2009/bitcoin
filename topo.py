#!/usr/bin/python

"""
This example shows how to create an empty Mininet object
(without a topology object) and add nodes to it manually.
"""

from mininet.net import Mininet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.log import setLogLevel, info
# from threading import Thread
import thread
import time
import simpleserver
import clientrequest

port=9001
peer={}

def emptyNet():

    "Create an empty network and add nodes to it."

    net = Mininet( controller=Controller )

    info( '*** Adding controller\n' )
    net.addController( 'c0' )
    
    info( '*** Adding switch\n' )
    s1 = net.addSwitch( 's1' )

    
    n=input('Enter no. of hosts ')
    info( '*** Adding hosts\n' )
    for h in range(n) :
      host = net.addHost( 'h%s'%(h+1))
      net.addLink(host,s1)

   

    info( '*** Starting network\n')
    net.start()
  
    for h in range(n):
	host=net.get('h%s'%(h+1))
        print host
        try :
          t=thread.start_new_thread(callthread,(host,2,h))
	except :
	   print "not able to start thread "
   
    inp=input("which server u want to connect to...?? ")
    server=net.get('h%s'%inp)
    print server
    #print (str(peer))
    
    inp2=input("tell me ur client id..")
    client=net.get('h%s'%inp2)
    print client
    clientrequest.client(server.IP(),(9000+inp),client.IP())  
    
    
    info( '*** Running CLI\n' )
    CLI( net )
    
    info( '*** Stopping network' )
    net.stop()
def callthread(name,delay,i):
      	print "Thread started......"  
        key=i+1
        peer.setdefault(key,[])
	peer[key]=(simpleserver.Server(port+i,name,name.IP()))
	#peer[key]=(name)
	time.sleep(delay)
        
if __name__ == '__main__':
    setLogLevel( 'info' )
    emptyNet()
