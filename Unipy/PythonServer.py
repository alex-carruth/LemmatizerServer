from socket import *
import threading
import os
import json
from ServerOps import server_main

#Processes the client. Only runs one client at once
def clientThread(sock):
    try:
        while True:
            #Get Json from client
            jsonr_packet = sock.recv(4096).decode()
            #Load json string into variable
            r_packet = json.loads(jsonr_packet)
            #Find lemmas
            jsons_packet = server_main.run_wordnet(r_packet)
            #Convert the packet into a json string
            s_packet = json.dumps(jsons_packet)
            #Send the packet
            sock.sendall(s_packet.encode())
    except:
        sock.close()
        os._exit(1)


def main():
    #Create a socket stream in the internet domain
    sock = socket(AF_INET, SOCK_STREAM)
    try:
        #Bind the socket to the correct port
        sock.bind(("0.0.0.0", 7734))
    except:
        print("Port cannot be accessed")
        os._exit(1)
    try:
        while True:
            #Listen for connections on the socket
            sock.listen(5)
            #Accept the connection and get the client and address
            c, addr = sock.accept()
            #Create a new thread that runs the clientThread code and sends the socket as an argument
            thread = threading.Thread(target=clientThread, args=(c,))
            #Start the new thread
            thread.start()
    except:
        sock.close()
        os._exit(1)

if __name__ == "__main__":
    main()
