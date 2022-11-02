import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia


listener = sr.Recognizer()
robot = pyttsx3.init()
voices = robot.getProperty('voices')
voices = robot.getProperty('voices')
robot.setProperty('voice', voices[1].id)


def speak(audio):
    robot.say(audio)
    robot.runAndWait()


def inputRequest():
    global request
    try:
        with sr.Microphone() as origin:
            # speak('Hello Teeaaruh, I am Eve. How may I help you?')
            print("Eve is listening...")
            speech = listener.listen(origin)
            request = listener.recognize_google(speech)
            request = request.lower()
            if "Eve" in request:  # if audio doesn't contain 'Eve' request will be ignored
                request = request.replace('Eve', " ")
                print(request)
    except:
        print("Try again.")
    return request


def playEve():
    request = inputRequest()
    print(request)
    if 'play' in request:
        song = request.replace('play', " ")
        speak("Playing" + song)
        pywhatkit.playonyt(song)
    elif 'time' in request:
        time = datetime.datetime.now().strftime('%I:%M%p')
        speak("Current time is: " + time)

    elif 'date' in request:
        date = datetime.datetime.now().strftime('%A %B %w %Y')
        speak("Today's date is: " + date)
    elif 'how are you' in request:
        speak("I am well Teeaaruh, how are you?")
    elif 'what is your name' in request:
        speak("I am Eve. How can I help you today?")
    elif 'who is' in request:
        human = request.replace('who is', " ")
        info = wikipedia.summary(human, 1)
        print(info)
        speak(info)
    else:
        speak("I didn't quite get that.")


playEve()
