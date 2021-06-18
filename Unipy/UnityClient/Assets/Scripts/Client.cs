using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using System;
using System.Net;
using System.Net.Sockets;
using System.Text;
using System.IO;


namespace Client
{
    public static class Access
    {
        public static Lemmatizer Lemmatize(string fileName, Lemmatizer lemmaMaker)
        {
            string sentence = ReadFile(fileName);
            lemmaMaker.text = sentence;
            string message = JsonUtility.ToJson(lemmaMaker);
            lemmaMaker = JsonUtility.FromJson<Lemmatizer>(ConnectAndExecute(message));
            return lemmaMaker;
        }
        private static string ConnectAndExecute(string message)
        {
            IPHostEntry host = Dns.GetHostEntry("54.167.118.0");
            IPEndPoint ipe = new IPEndPoint(host.AddressList[0], 9050);
            Socket s = new Socket(ipe.AddressFamily, SocketType.Stream, ProtocolType.Tcp);
            s.Connect(ipe);
            if (!s.Connected)
            {
                throw new Exception("Could not connect to server");
            }
            else
            {
                Debug.Log("Server connection successful");
            }
            s.Send(Encoding.ASCII.GetBytes(message));
            byte[] receivedMessage = new byte[4096];
            int receivedBytes = s.Receive(receivedMessage);
            string receivedString = Encoding.ASCII.GetString(receivedMessage, 0, receivedBytes);
            s.Shutdown(SocketShutdown.Both);
            s.Close();
            return receivedString;
        }

        //Read the text to send from a file and return it
        private static string ReadFile(string filename)
        {
            TextAsset asset = (TextAsset)Resources.Load(filename);
            string sentence = asset.ToString();
            return sentence;
        }
    }


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

}
