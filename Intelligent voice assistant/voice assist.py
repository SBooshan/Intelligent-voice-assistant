import speech_recognition as sr 
from GoogleNews import GoogleNews
import pyttsx3
import webbrowser
import subprocess
import pyttsx3 as tts
import pywhatkit
import sumy




speaker = tts.init()
googlenews = GoogleNews()
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
speaker.setProperty('rate',150)
recognizer=sr.Recognizer()


note = ["Listen raja songs" ," dance" ," trip to manali"]


def cmd():
    with sr.Microphone() as source:
        print("Clearing background noises...Please wait")
        recognizer.adjust_for_ambient_noise(source,duration=0.5)
        print('Ask me anything..')
        recordedaudio=recognizer.listen(source)
        print("Done recording..!")
    try:
        text=recognizer.recognize_google(recordedaudio,language='en_US')
        text=text.lower()
        print('Your message:',format(text))

    except sr.UnknownValueError:
        print("Sorry, I did not understand your speech.")
        
    if 'create note' in text or 'add note' in text:
            engine.say('What would you like to note down?')
            engine.runAndWait()
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source, duration=0.5)
                print("Listening for your note...")
                note_audio = recognizer.listen(source)
            try:
                note_text = recognizer.recognize_google(note_audio, language='en_US')
                note.append(note_text)
                engine.say('Note added.')
                engine.runAndWait()
                print(f"Note added: {note_text}")
            except sr.UnknownValueError:
                print("Sorry, I could not understand your note.")
            except Exception as e:
                print(f"An error occurred: {e}")
   
                

               

    if 'show the note' in text:
        for item in note:
            speaker.say(item)
            speaker.runAndWait()
           


    if 'headlines' in text:
        engine.say('Getting news for you ')
        engine.runAndWait()
        googlenews.get_news('Today news')
        googlenews.result()
        a=googlenews.gettext()
       
          # Convert the headline to speech
        engine.runAndWait()
        print(*a[1:5],sep=',')
       

    if 'tech' in text:
        engine.say('Getting news for you ')
        engine.runAndWait()
        googlenews.get_news('Tech')
        googlenews.result()
        a=googlenews.gettext()
        print(*a[1:5],sep=',')
       
     

    if 'politics' in text:
        engine.say('Getting news for you ')
        engine.runAndWait()
        googlenews.get_news('Politics')
        googlenews.result()
        a=googlenews.gettext()
        print(*a[1:5],sep=',')

    if 'sports' in text:
        engine.say('Getting news for you ')
        engine.runAndWait()
        googlenews.get_news('Sports')
        googlenews.result()
        a=googlenews.gettext()
        print(*a[1:5],sep=',')

    if 'cricket' in text:
        engine.say('Getting news for you ')
        engine.runAndWait()
        googlenews.get_news('cricket')
        googlenews.result()
        a=googlenews.gettext()
        print(*a[1:5],sep=',')
    
    if 'chrome' in text:
        engine.say('okay chrome is opening now')
        engine.runAndWait()
        program= "C:\Program Files\Google\Chrome\Application\chrome.exe"
        subprocess.Popen([program])

   
    
    if 'play' in text:
         engine.say(" the video you are searching for")
         engine.runAndWait()
         pywhatkit.playonyt(text)
         
    
    



cmd()