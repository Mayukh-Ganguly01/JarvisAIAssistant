import speech_recognition as sr 
import webbrowser
import pyttsx3
import musicLibrary
from openai import OpenAI
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def aiProcess(command):
    client = OpenAI(
    api_key="API_KEY" ,
    )

    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a virtual assistant, skilled in explaining complex programming concepts with creative flair."},
        {"role": "user", "content": command}
    ]
    )

    return completion.choices[0].message.content

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open github" in c.lower():
        webbrowser.open("https://github.com")
    elif "open web development" in c.lower():
        webbrowser.open("https://learn.codehelp.in/t/u/activeCourses")
    elif "open chat" in c.lower():
        webbrowser.open("https://chatgpt.com/")
    elif c.lower().startswith("play"):
        parts = c.lower().split(" ")
        if len(parts) >= 1:    
            song = parts[1]
            link = musicLibrary.music[song]
            webbrowser.open(link)
        else:
            print("specify the song")
    else:
        # let openAI handle the request
        output = aiProcess(c)
        speak(output)
        
    
    print(c)

if __name__ == "__main__":
    speak("Initializing Your Virtual Assistant...")
    while True:
        # obtain Audio from microphone
        r = sr.Recognizer() 
        try:
            with sr.Microphone() as source:
                speak("Listening...")
                audio = r.listen(source)
            word = r.recognize_google(audio)
            print(word)
            if(word.lower() == "jarvis"):
                # speak("bol Gandu")
                # listen for command
                with sr.Microphone() as source:
                    speak("yes sir")
                    audio = r.listen(source, phrase_time_limit=2)
                    command = r.recognize_google(audio) 

                    processCommand(command)
        except sr.UnknownValueError:
            speak("Couldnot understand what are saying")
        except sr.RequestError as e:
            speak(f"Jarvis error {e}")