using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using System;
using System.Net;
using System.Net.Sockets;
using System.Text;
using System.IO;
using Client;

public class LemmatizerClient : MonoBehaviour
{

    //Command attached to the Button to run the program
    public void Run()
    {
        Lemmatizer lemmaA = new Lemmatizer();
        lemmaA.function = "wordnet";
        lemmaA = Access.Lemmatize("lemmatize_text", lemmaA);
        //Display the received text on the Canvas
        Debug.Log(lemmaA);
        GameObject.Find("output").GetComponent<Text>().text = "\nmessage: " + lemmaA.lemmas[1];
    }
}
