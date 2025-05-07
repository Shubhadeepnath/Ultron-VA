import speech_recognition as sr
import webbrowser
import pyttsx3
import requests
from dotenv import load_dotenv
import os

load_dotenv()


recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()



# def get_weather(city):
#     api_key ="50a0b7fedbc6ed1783655588d3de94a0"  # replace with your actual API key

    
#     base_url = "http://api.openweathermap.org/data/2.5/weather?"

#     complete_url = f"{base_url}appid={api_key}&q={city}&units=metric"

#     response = requests.get(complete_url)
#     data = response.json()

#     if data["cod"] != "404":
#         main = data["main"]
#         weather_desc = data["weather"][0]["description"]
#         temp = main["temp"]
#         humidity = main["humidity"]
#         result = f"Currently in {city}, it's {temp}°C with {weather_desc} and {humidity}% humidity."
#         return result 
#     else:
#         return "City not found. Please try again."

def get_weather(city):
    api_key = os.getenv("OPENWEATHER_API_KEY")
    # print(f"API Key: {api_key}") 
    if not api_key:
        print("API key not found. Make sure it's in the .env file.")
        return

    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}appid={api_key}&q={city}&units=metric"

    response = requests.get(complete_url)
    data = response.json()
    # print(f"API response: {data}")

    if data["cod"] != "404":
         main = data["main"]
         weather_desc = data["weather"][0]["description"]
         temp = main["temp"]
         humidity = main["humidity"]
         result = f"Currently in {city}, it's {temp}°C with {weather_desc} and {humidity}% humidity."
         return result 
    else:
         return "City not found. Please try again."


def processCommand(c):
   if "open google" in c.lower():
       webbrowser.open("https://google.com")
   elif "open linkedin" in c.lower():
       webbrowser.open("https://linkedin.com")
   elif "open facebook" in c.lower():
       webbrowser.open("https://facebook.com")
   elif "open youtube" in c.lower():
       webbrowser.open("https://youtube.com")
   elif "open amazon" in c.lower():
       webbrowser.open("https://amazon.com")
   elif "open github" in c.lower():
       webbrowser.open("https://github.com")

   elif "weather" in command:
        speak("Which city?")
        try:
            with sr.Microphone() as source:
                audio = recognizer.listen(source, timeout=4, phrase_time_limit=3)
                city = recognizer.recognize_google(audio)
                # print(f"You said: {city}") 
                weather = get_weather(city)
               
                speak(weather)
        except:
            speak("Sorry, I couldn't catch the city name.")
   
    
if __name__ == "__main__":
    speak("Initializing Ultron....")
    while True:
        #Listen for the wake word Ultron
        #obtain audio from microphone
     r = sr.Recognizer()
     
        

# recognize speech using Google
     print("recognizing...")
     try:
         with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source, timeout=2, phrase_time_limit=1) #otherwise it takes muchmore time to listen so we added a timeout of 2s.
         word = r.recognize_google(audio)
         if(word.lower() == "ultron"):
             speak("Hey Human")
             #listen for command
             with sr.Microphone() as source:
                print("Ultron Activated...")
                audio = r.listen(source)
                command=r.recognize_google(audio)
                
                processCommand(command)
             
         
     
     except Exception as e:
       print("Error; {0}".format(e))






