import os
import pygame
import speech_recognition as sr
import pyautogui
import pywhatkit
from datetime import datetime
from functions.emailsender import *        
from gpt4_free import GPT
from PIL import Image


def speak(text):
    voice = "en-CA-ClaraNeural"

    command = f'edge-tts --voice "{voice}" --text "{text}" --write-media "output.mp3"'

    os.system(command)

    pygame.init()
    pygame.mixer.init()


    try:
        pygame.mixer.music.load("output.mp3")

        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    
    except Exception as e:
        print(e)
    
    finally:
        pygame.mixer.music.stop()
        pygame.mixer.quit()
    
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-us')
    
    except Exception as e:
        print(e)
        return "-"
    return query

sleep_mode = False

speak('Hello sir, I am Friday and How can i help you today?')
# click_on_chat_button()
while True:

    query = take_command().lower()
    print("\nYou: "+ query)

    with open("conv.txt", "a") as f:
        f.write("You: " + query + "\n")

    if 'open' in query:
        app_name = query.replace('open','')
        speak('opening' + app_name)
        pyautogui.press('super')
        pyautogui.typewrite(app_name)
        pyautogui.sleep(0.7)
        pyautogui.press('enter')
    
    elif 'play' in query:
        song_name = query.replace('play','')
        speak('Sure sir. Playing' + song_name + ' in youtube')
        pywhatkit.playonyt(song_name)        
    
    elif 'switch tab'in query:
        pyautogui.hotkey('ctrl','tab')

    elif 'close tab'in query:
        pyautogui.hotkey('ctrl','w')    

    elif 'close' in query:
        pyautogui.hotkey('alt','F4')
        speak('Done, sir')

    elif 'pause' in query:
        pyautogui.hotkey('space')

    elif 'take screenshot' in query:
        speak("Taking screenshot")
        pyautogui.screenshot("screenshot.png")
        image = Image.open('screenshot.png')
        image.show()
                

    elif 'time' in query:
        current_time = datetime.now().strftime("%H %M %p")   
        speak('Current time is ' + current_time)

    elif '-' in query:
        print('Speak again')  

    elif 'sleep' in query:
        speak('Going Offline. call me anytime if need anything')
        sleep_mode = True

    elif 'write an email' in query or 'compose an email' in query or 'send an email' in query:
        speak('Sure sir, Can you provide me name of user to whom you want to send an email below :')
        receiver = input('Enter receivers email address: ')
        speak('what should be subject of the email')
        subject = take_command()
        speak('what should be the content. Just provide me a prompt')
        email_prompt = take_command()
        content = GPT('write a mail for' + email_prompt)
        send_email(receiver, subject, content)
        speak(f'email sent successfully to {receiver}')

    else:
        res = GPT(query)
        speak(res)
        # speak('h')
        

    while sleep_mode:
        query = take_command().lower()
        print(query)
        if 'hello friday' in query:
            speak('System online. How can I help you ')
            sleep_mode = False
            