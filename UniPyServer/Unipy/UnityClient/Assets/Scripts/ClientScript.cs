using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using System;
using System.Net;
using System.Net.Sockets;
using System.Text;
using System.IO;



public class ClientScript : MonoBehaviour
{
    //Create JSON object to be used by the lemmatizer
    public class Lemmatizer
    {
        //Holds the function to be used by the server
        public string function;
        //Holds the sent text
        public string text;
        //Holds the lemmas to be returned
        public string[] lemmas;
    }

    //Command attached to the Button to run the program
    public void Run()
    {
        string message = ConnectAndExecute();
        //Display the received text on the Canvas
        GameObject.Find("output").GetComponent<Text>().text += "\nmessage: " + message;
    }

    private static string ConnectAndExecute()
    {
        string sentence = ReadFile("lemmatize_text.txt");

        //IPHostEntry host = Dns.GetHostEntry(Dns.GetHostName());
        IPHostEntry host = Dns.GetHostEntry("54.167.118.0");
        IPEndPoint ipe = new IPEndPoint(host.AddressList[0], 7734);
        Socket s = new Socket(ipe.AddressFamily, SocketType.Stream, ProtocolType.Tcp);
        s.Connect(ipe);
        if (!s.Connected)
        {
            throw new Exception("could not connect to server");
        }
        Lemmatizer lemmaMaker = new Lemmatizer();
        lemmaMaker.text = sentence;
        Debug.Log(lemmaMaker.text);
        string message = JsonUtility.ToJson(lemmaMaker);
        Debug.Log(message);
        s.Send(Encoding.ASCII.GetBytes(message));

        byte[] receivedMessage = new byte[4096];
        int receivedBytes = s.Receive(receivedMessage);
        string receivedString = Encoding.ASCII.GetString(receivedMessage, 0, receivedBytes);
        Debug.Log(receivedString);
        lemmaMaker = JsonUtility.FromJson<Lemmatizer>(receivedString);
        Debug.Log(lemmaMaker);
        s.Shutdown(SocketShutdown.Both);
        s.Close();
        return receivedString;
    }

    //Read the text to send from a file and return it
    private static string ReadFile(string filename)
    {
        string sentence = File.ReadAllText("Assets/Texts/" + filename);
        return sentence;
    }
}
