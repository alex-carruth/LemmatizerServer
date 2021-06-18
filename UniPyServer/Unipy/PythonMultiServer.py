# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 10:51:57 2021

@author: acarr
"""
from socket import *
import os
import threading
import json
from ServerOps import server_main

def clientThread(sock):
    try:
        while True:
            #Get Json from client
            jsonr_packet = sock.recv(4096).decode()
            #Load json string into variable
            r_packet = json.loads(jsonr_packet)
            #Find lemmas
            jsons_packet = server_main.switch_function(r_packet)
            #Convert the packet into a json string
            s_packet = json.dumps(jsons_packet)
            #Send the packet
            sock.sendall(s_packet.encode())
    except:
        sock.close()

def main():
    #Create a socket stream in the internet domain
    sock = socket(AF_INET, SOCK_STREAM)
    try:
        #Bind the socket to the correct port
        sock.bind(("0.0.0.0", 9050))
    except:
        print("Port cannot be accessed")
    #Listen for connections on the socket
    while True:
        sock.listen()
        #Accept the connection and get the client and address
        c, addr = sock.accept()
        #Create a new thread that runs the clientThread code and sends the socket as an argument
        thread = threading.Thread(target=clientThread, args=(c,))
        #Start the new thread
        thread.start()
        print(thread)
    sock.close()

if __name__ == "__main__":
    main()