import os

def speak(text):
    command = f'powershell -Command "Add-Type -AssemblyName System.Speech; ' \
              f'(New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{text}\');"'
    os.system(command)

if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.1. created by Anagha")
    while True:
        x = input("Enter what you want to speak: ")
        if x.lower() == 'q':
            speak("Okay, bye bye friend!")
            break
        speak(x)

        
    