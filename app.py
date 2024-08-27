from flask import Flask, request, jsonify, render_template
import speech_recognition as sr
import pyttsx3
import webbrowser
import requests
from gtts import gTTS
import pygame
import os
import datetime
import logging
import threading
from openai import OpenAI
import musicLibrary
import pyautogui
from PIL import ImageGrab

app = Flask(__name__)

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "23ed1e5930b641edb7e58c659168fcfb"
openai_api_key = "sk-proj-TgHsC5TA8kOceYBGJicmT3BlbkFJPB1H7pPI7HGASVNpKg9W"

# Setup logging
logging.basicConfig(level=logging.DEBUG)

def speak(text):
    def play_audio():
        try:
            if isinstance(text, str):
                tts = gTTS(text)
                tts.save('temp.mp3')
                pygame.mixer.init()
                pygame.mixer.music.load('temp.mp3')
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick(10)
                pygame.mixer.music.unload()
                os.remove("temp.mp3")
            else:
                logging.error("Text to be spoken is not a string")
        except Exception as e:
            logging.error(f"Error in speak function: {e}")
    
    threading.Thread(target=play_audio).start()

def ai_process(command):
    client = OpenAI(api_key=openai_api_key)
    completion = client.chat_completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a virtual assistant named Nova skilled in general tasks like Alexa and Google Cloud. Give short responses please"},
            {"role": "user", "content": command}
        ]
    )
    return completion.choices[0].message.content

def get_current_time():
    return datetime.datetime.now().strftime("%I:%M:%S")

def get_current_date():
    now = datetime.datetime.now()
    return f"{now.day}/{now.month}/{now.year}"

def wishme():
    hour = datetime.datetime.now().hour
    greeting = "Good Night Sir, See You Tomorrow" if hour < 4 or hour >= 20 else (
        "Good Evening Sir!" if hour >= 16 else (
            "Good Afternoon Sir!" if hour >= 12 else "Good Morning Sir!!"
        )
    )
    speak("Welcome back sir!")
    speak(greeting)
    # speak("Nova at your service sir, please tell me how may I help you.")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_command', methods=['POST'])
def process_command():
    data = request.json
    command = data.get('command')
    if command:
        response = handle_command(command)
        return jsonify({'response': response})
    return jsonify({'response': 'Invalid command'})

def handle_command(command):
    command = command.lower()
    

    
    if "open" in command.lower():
        sites = {
            "google": "https://google.com",
            "gmail": "https://gmail.com",
            "facebook": "https://facebook.com",
            "youtube": "https://youtube.com",
            "linkedin": "https://linkedin.com",
            "bearys": "https://bitmangalore.edu.in/",
            "BIT": "https://bitmangalore.edu.in/",
            "instagram":"https://instagram.com",
        }
        for site in sites:
            if site in command.lower():
                 
                webbrowser.open(sites[site])
                speak( f"Opening {site.capitalize()}")
                return f"Opening {site.capitalize()}"
    # if "Hey Nova" in command or "Nova" in command:
        
    #     return "Nova at your service sir, please tell me how may I help you."    
    if "search" in command.lower():
        query = command.split("search ")[1]
        webbrowser.open(f"https://www.google.com/search?q={query}")
        return f"Searching for {query} on Google"
    if "youtube search" in command.lower():
        query = command.split("search ")[1]
        webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
        return f"Searching for {query} on youtube"
    if "close" in command.lower():
        
        pyautogui.hotkey('ctrl', 'w')
        return "Tab closed"
    if "screenshot" in command.lower():
        screenshot = ImageGrab.grab()
        screenshot.save("screenshot.png")
        
        return "Screenshot taken and saved."
    if "time" in command.lower():
        current_time = get_current_time()
        
        return f"The current time is {current_time}"
    
    if "date" in command.lower():
        current_date = get_current_date()
        speak (f"The current date is {current_date}")
        return f"The current date is {current_date}"
    
    if "who are you" in command.lower():
        response = "I'm Nova, a virtual assistant created by Muhammad Hisham."
        
        return response
    
    if "how are you" in command.lower():
        response = "I'm fine sir, What about you?"
        speak(response)
        return response
    
    if "play" in command.lower():
        song = command.split("play ")[1]
        song_url = musicLibrary.music.get(song)
        if song_url:
            webbrowser.open(song_url)
            return f"Playing {song}"
        return f"Song {song} not found in the library"
    
    if "news" in command.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            data = r.json()
            articles = data.get('articles', [])
            for article in articles:
                speak(article['title'])
                return article['title']
    
    if "hello" in command.lower() or "nova" in command.lower():
        return "Hello, I am Nova. How can I assist you today?"
    output = ai_process(command)
    speak(output)
    return output

if __name__ == "__main__":
    app.run(debug=True)


# newsapi = "23ed1e5930b641edb7e58c659168fcfb"