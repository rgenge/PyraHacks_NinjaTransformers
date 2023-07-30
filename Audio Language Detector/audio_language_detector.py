import sounddevice as sd
import speech_recognition as sr
import wavio
import soundfile as sf
from playsound import playsound
import os
from time import sleep
import numpy as np
import nltk
from textblob import TextBlob
from langdetect import detect

#Define function for recording voice
def record():
    keyPress = input("\nPress enter to record yourself speaking in any language.")
    if keyPress == '':
        seconds = 15
        print("Now recording. You have 15 seconds.")
        voice_recording = sd.rec(int(seconds * 44100), samplerate=44100, channels=1)
        sleep(8)
        print("\nRecording will stop in...")
        sleep(2)
        for i in range(5, 0, -1):
            print(i)
            sleep(1)
        sd.wait()
        print("Stopped Recording.")

        #Save voice recording as .wav file
        wavio.write("voicerecording.wav", voice_recording, 44100, sampwidth=2)

        #Play voice recording
        print("\nPlaying your recording...")
        cwd = os.getcwd()
        sound_file_path = cwd + "/voicerecording.wav"
        playsound(sound_file_path)
    else:
        quit()

#Allow user to record themselves and give option to recieve transcript or re-record
while True:
    record()
    keyPress2 = input("\nPress enter to record yourself again, enter 1 to get a transcript and emotional analysis of your recording, enter q to exit: ")
    if keyPress2 == "1":
        break
    if keyPress2 == "q":
        quit()
    os.remove("voicerecording.wav")

#Retrieve transcript of recording
print("\nRetrieving your transcript and analysis...\n")

#Listen to the .wav file containg voice recording
with sr.AudioFile("voicerecording.wav") as source:
    l_recording = sr.Recognizer().listen(source)

# Use Google recognizer for speech to text conversion
    try:
        transcript = sr.Recognizer().recognize_google(l_recording)
        print("\nTranscript:",transcript)
    except:#In case Google is unable to recognize
        print("Unable to retrieve transcript.")

#save transcript as .txt file
file = open("transcript.txt", "w")
file.write("%s" %transcript)
file.close()

#read transcript previously recorded
file = open("transcript.txt", "r")
text = file.read()
file.close()

languageOutput = (detect(text))
#Language Code outputed by langdetect
simplifiedNames = ["fr", "en", "es", "vi", "de"]

#1 = French, 2 = English, 3 = Spanish, 4 = Vietnamese, 5 = German.

if languageOutput == simplifiedNames[0]:
    print("French")
    os.remove("voicerecording.wav")
    os.remove("transcript.txt")
    exit()
elif languageOutput == simplifiedNames[1]:
    print("English")
    os.remove("voicerecording.wav")
    os.remove("transcript.txt")
    exit()
elif languageOutput == simplifiedNames[2]:
    print("Spanish")
    os.remove("voicerecording.wav")
    os.remove("transcript.txt")
    exit()
elif languageOutput == simplifiedNames[3]:
    print("Vietnamese")
    os.remove("voicerecording.wav")
    os.remove("transcript.txt")
    exit()
elif languageOutput == simplifiedNames[4]:
    print("German.")
    os.remove("voicerecording.wav")
    os.remove("transcript.txt")
    exit()
else:
    print("Cannot detect language, try again.")
    os.remove("voicerecording.wav")
    os.remove("transcript.txt")
    exit()