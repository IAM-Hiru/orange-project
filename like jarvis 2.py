import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import psutil
import signal
import requests

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

# Function to get the current location 
def get_location():
    try:
        # Using the free geolocation API
        url = "https://www.google.com/search?q=google+maps&oq=google&gs_lcrp=EgZjaHJvbWUqFQgCEAAYQxiDARiLAxixAxiABBiKBTIHCAAQABiPAjIhCAEQLhhDGIMBGMcBGIsDGKgDGLEDGNEDGNIDGIAEGIoFMhUIAhAAGEMYgwEYiwMYsQMYgAQYigUyFQgDEAAYFBiDARiHAhiLAxixAxiABDIGCAQQRRg8Mg0IBRAFGIsDGKYDGKgDMgYIBhBFGDwyBggHEEUYPNIBCDQ0NjZqMWo0qAIAsAIB&sourceid=chrome&ie=UTF-8"
        response = requests.get(url, timeout=10)  # Add a timeout to avoid hanging
        print("API Response:", response.json())  # Debugging: Log API response
        response.raise_for_status()  # Raise an error for bad status codes
        data = response.json()
        if data["status"] == "success":
            city = data.get("city", "Unknown city")
            region = data.get("regionName", "Unknown region")
            country = data.get("country", "Unknown country")
            return f"You are in {city}, {region}, {country}."
        else:
            return f"Error: {data.get('message', 'Unable to determine location')}"
    except requests.exceptions.RequestException as e:
        return f"Network error: {e}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"


# Function to close the browser
def close_browser():
    for proc in psutil.process_iter(attrs=['pid', 'name']):
        try:
            if 'chrome' in proc.info['name'].lower() or 'firefox' in proc.info['name'].lower() or 'edge' in proc.info['name'].lower():
                print(f"Closing {proc.info['name']} with PID {proc.info['pid']}")
                os.kill(proc.info['pid'], signal.SIGTERM)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

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

    elif 'close browser' in query:
        speak("Closing all open browsers")
        close_browser()

    elif 'time' in query:
        str_time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {str_time}")

    elif 'open notepad' in query:
        speak("Opening Notepad")
        os.system("notepad")

    elif 'hi jarvis' in query:
        speak("Hi sir, how are you?")   

    elif 'thank you jarvis' in query:
        speak("thank you sir")

    elif 'who are you' in query:
        speak("I am Jarvis, your virtual assistant")

    elif 'jarvis' in query:
        speak("Yes sir")

    elif 'i am going to ask you a question' in query:
        speak("Sure, sir.")          

    elif 'i am fine' in query:
        speak("I am also fine, sir.")    

    elif 'ok ok' in query:
        speak("Haa ok sir.") 

    elif 'current location' in query or 'where am i' in query:
        location = get_location()
        speak(location)

    elif 'exit' in query:
        speak("Goodbye! sir")
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
