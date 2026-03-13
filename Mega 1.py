import webbrowser
import speech_recognition as sr
import pyttsx3
recognizer=sr.Recognizer()
engine = pyttsx3.init()
# For female Voice
#voices = engine.getProperty('voices')
#engine.setProperty('voice', voices[1].id)
def speak(text):
    engine.say(text)
    engine.runAndWait()
def open_websites(c):
    if "open google" in c.lower():
        speak("Opening Google")
        webbrowser.open_new("https://google.com")
    elif "open facebook" in c.lower():
        speak("Opening Facebook")
        webbrowser.open_new("https://facebook.com")
    elif "open youtube" in c.lower():
        speak("Opening Youtube")
        webbrowser.open_new("https://youtube.com")
    elif "open instagram" in c.lower():
        speak("Opening Instagram")
        webbrowser.open_new("https://instagram.com")
    elif "open linkedin" in c.lower():
        speak("Opening Linkedin")
        webbrowser.open_new("https://linkedin.com")
    elif "exit" in c or "stop" in c:
        speak("Goodbye")
        exit()
def main():
    speak("Hii I'm Jarvis.Initialising....")
    while True:
        try:
            with sr.Microphone() as source:
                print("Adjusting for background noise...")
                recognizer.adjust_for_ambient_noise(source, duration=1)
                print("Listening....")
                audio=recognizer.listen(source)
            command=recognizer.recognize_google(audio)
            print("You said:",command)
            open_websites(command)
        except sr.UnknownValueError:
            speak("Could not understand audio repeat it again")
        except sr.RequestError:
            speak("There is a network error wait for a while")
        except Exception as e:
            print("Error",(e))
if __name__=="__main__":
    main()