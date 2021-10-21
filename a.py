import pandas as pd     #pip install pandas
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr     #pip install SpeechRecognition

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query



sheet_id='1nFE-K6TH_qzybFgPFK-idvUUISaT0nZ6gnHHdIXklbo'

df= pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")
a=df.set_index('Organization name').T.to_dict('list')  #converting pandas dataframe to a python dictionary

print(type(a.values()))
print(a.keys())
query = takeCommand().lower()

for key,value in a.items():
    if key == query:
        print(key)
        speak(value)

   
