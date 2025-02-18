import speech_recognition as sr
import pyttsx3
import os
import webbrowser

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Capture audio input from the user."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        try:
            audio = recognizer.listen(source, timeout=5)
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't understand that.")
        except sr.RequestError:
            speak("Network error. Please check your connection.")
        except sr.WaitTimeoutError:
            speak("No input detected.")
        return ""

def open_application(app_name):
    """Open specified applications."""
    if "chrome" in app_name:
        speak("Opening Google Chrome.")
        os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
    elif "youtube" in app_name:
        speak("Opening YouTube.")
        webbrowser.open("https://www.youtube.com")
    elif "vscode" in app_name or "visual studio code" in app_name:
        speak("Opening Visual Studio Code.")
        os.startfile("C:\\Users\\YourUsername\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
    elif "codeblocks" in app_name:
        speak("Opening CodeBlocks.")
        os.startfile("C:\\Program Files\\CodeBlocks\\codeblocks.exe")
    elif "notepad" in app_name:
        speak("Opening Notepad.")
        os.startfile("notepad.exe")
    elif "this pc" in app_name or "my computer" in app_name:
        speak("Opening This PC.")
        os.startfile("explorer.exe")
    else:
        speak(f"Sorry, I couldn't find the application {app_name}.")

def main():
    """Main function to control the assistant."""
    speak("Hello, naan Hiru. naan evvaru ungalukku uthava vendum?")
    while True:
        command = listen()
        if "hye hiru" in command or "hi hiru" in command:
            speak("hi sir,have a good day! ")
        elif "exit" in command or "quit" in command:
            speak("Goodbye!")
            break
        elif "open" in command:
            speak("What do you want to open?")
            app = listen()
            open_application(app)
        else:
            speak("I didn't understand that. Please try again.")

if __name__ == "__main__":
    main()