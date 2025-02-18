import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os

# Initialize the voice engine
engine = pyttsx3.init()

# Function to speak the text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to wish the user
def wish_me():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    
    speak("I am JARVIS, How can I assist you today?")

# Function to recognize the voice command
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
        return "None"
    except sr.RequestError:
        print("Sorry, there is an issue with the speech recognition service.")
        return "None"
    return query.lower()

# Function to handle tasks
def handle_query(query):
    if 'wikipedia' in query:
        speak("Searching Wikipedia...")
        query = query.replace("wikipedia", "")
        try:
            result = wikipedia.summary(query, sentences=2)
            speak(result)
        except wikipedia.exceptions.DisambiguationError as e:
            speak("There are multiple results for this query, please be more specific.")
        except wikipedia.exceptions.HTTPTimeoutError:
            speak("Wikipedia search timed out. Please try again later.")
    
    elif 'open youtube' in query:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif 'open google' in query:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")


    elif 'time' in query:
        str_time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {str_time}")

    elif 'open notepad' in query:
        speak("Opening Notepad")
        os.system("notepad")

    elif 'hi jarvis' in query :
        speak("hi sir, how are you")   

    elif 'i am fine and you' in query:
        speak("i am also fine sir")    

    elif 'ok ok' in query :
        speak("haa ok sir") 

    elif 'exit' in query or 'bye' in query:
        speak("Goodbye!")
        exit()

    else:
        speak("Sorry, I cannot perform that task at the moment.")

# Main function to run JARVIS
def run_jarvis():
    wish_me()
    while True:
        query = take_command()
        if query != "None":
            handle_query(query)

# Run the assistant
if __name__ == "__main__":
    run_jarvis()
