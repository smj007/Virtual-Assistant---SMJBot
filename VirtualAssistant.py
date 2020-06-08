# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 22:31:20 2020

@author: saimi
"""
#Implementation of a Virtual Assistant 
#Importing WFA API
import wolframalpha
client = wolframalpha.Client("xo") #Any API Key is given

#Importing Wiki API
import wikipedia

#Using the GUI for ip and op
import PySimpleGUI as pySG
pySG.theme('TealMono') #Color (adjust as needed)
layout =[[pySG.Text('Shoot, what do you want?'), pySG.InputText()],[pySG.Button('Alright'), pySG.Button('Cancel')]]
window = pySG.Window('SMJBot', layout) #Defining the contents of the window

import pyttsx3
engine = pyttsx3.init() #text to speech library (use gTTS but it needs to be saved as an audio file)

while True:
    event, values = window.read()  #values stores the ip query
    if event in (None, 'Cancel'):    #exits
        break
    try:    #checks and finds both the results
        wiki_res = wikipedia.summary(values[0], sentences=2)
        wolfram_res = next(client.query(values[0]).results).text
        engine.say(wolfram_res)   #output audio
        pySG.PopupNonBlocking("Wolfram Result: "+wolfram_res,"Wikipedia Result: "+wiki_res)
    except wikipedia.exceptions.DisambiguationError: #fetch WFA result if Wiki error type 1
        wolfram_res = next(client.query(values[0]).results).text
        engine.say(wolfram_res)
        pySG.PopupNonBlocking(wolfram_res)
    except wikipedia.exceptions.PageError:   #fetch WFA result if Wiki error type 2 if page not found
        wolfram_res = next(client.query(values[0]).results).text
        engine.say(wolfram_res)
        pySG.PopupNonBlocking(wolfram_res)
    except:   #if WFA throws an error, fetch WIKI (Very rare)
        wiki_res = wikipedia.summary(values[0], sentences=2)
        engine.say(wiki_res)
        pySG.PopupNonBlocking(wiki_res)

    engine.runAndWait()

    print (values[0]) #prints the ip word we gave, as a sanity check on the app

window.close()