import os
import threading
from socket import *
import json

#Connects to the server, sends the client Json packet, and returns the Json packet received from the server
def mainServer(client_packet):
    #Create a socket stream in the internet domain
    sock = socket(AF_INET, SOCK_STREAM)
    try:
        #Connect to static IP for the server on the allowed port (7734)
        sock.connect(("54.167.118.0", 7734))
    except:
        #If connection does not work, exit program
        print("Could not connect to server")
        os._exit(1)
    #Send Json
    sock.sendall(client_packet.encode())
    #Receive server Json
    server_packet = sock.recv(4096).decode()
    #Close the socket
    sock.close()
    #Return the server Json
    return server_packet
    #os._exit(1)

#Reads text from file and returns it as a string
def convertSentence(filename):
    sentence = ""
    i = 0
    with open(filename, "r") as a_file:
        for line in a_file:
            stripped_line = line.split()
            for word in stripped_line:
                if(i > 0):
                    sentence = sentence + " " + word
                else:
                    sentence = word
                    i += 1
    return sentence

def main():
    #Get the text to lemmatize
    sentence = convertSentence("lemmatize_text.txt")
    #Create Json
    lemmatize = {}
    #Choose function
    lemmatize["function"] = "wordnet"
    #Add text field to Json
    lemmatize["text"] = sentence;
    #Convert json to string
    client_packet = json.dumps(lemmatize)
    #Run mainServer function and get back string returned from the server
    server_packet = mainServer(client_packet)
    #Convert the string back into a Json
    test = json.loads(server_packet)
    
if __name__ == "__main__":
    main()