import subprocess
import pyttsx3
import pyautogui
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
import smtplib
import ctypes
import time
from datetime import date
import requests
import shutil
import datetime
from clint.textui import progress
from ecapture import ecapture as ec
import wolframalpha
from twilio.rest import Client
from plyer import notification
import randfacts
from GoogleNews import GoogleNews
import os.path
from tkinter import *
import keyboard
from playsound import playsound

name_file = open("Assistant_name", "r")
name_assistant = name_file.read()

app = wolframalpha.Client("WRVYH2-6WRR9T6Y55")
account_sid = 'AC9f8c3e67160fb118469a15ec2bb541f3'

auth_token = 'a748912730c9770f94b288214f694161'

client = Client(account_sid, auth_token)


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
r = sr.Recognizer()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir !")
        print("Good Morning Sir !")

    elif hour >= 12 and hour < 16:
        speak("Good Afternoon Sir !")
        print("Good Afternoon Sir !")

    else:
        speak("Good Evening Sir !")
        print("Good Evening Sir !")

    speak("I am your Assistant")


def usrname():
    speak("What should i call you sir")
    uname = take_command()
    speak("Welcome Mister")
    speak(uname)
    columns = shutil.get_terminal_size().columns

    print("Welcome Mr.", uname)

    speak("How can i Help you" + uname)


def take_command():

    try:
        with sr.Microphone() as source:
            print("listening...")
            playsound(r"D:\Projects 2021-2222\Final-year_Project_II\pythonProject\assistant_on.wav")
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source, timeout=8, phrase_time_limit=8)
            
            playsound(r"D:\Projects 2021-2222\Final-year_Project_II\pythonProject\assistant_off.wav")
            
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')

            print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.")
        return "None"

    return query


# def send_email(to, content):
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.ehlo()
#     server.starttls()
#     server.login('dkokane0@gmail.com', '*************')
#     server.sendmail('dkokane0@gmail.com', to, content)
#     server.close()


def process_audio():

    if __name__ == '__main__':

        clear = lambda: os.system('cls')

        # This Function will clean any
        # command before execution of this python file
        clear()
        wishme()
        usrname()
        while True:
            query = take_command().lower()

            if 'about' in query:
                person = query.replace('Who is the', '')
                info = wikipedia.summary(person, 1)
                print(info)
                speak(info)
                wishme()

            elif 'open youtube' in query:
                speak("Here you go to Youtube\n")
                webbrowser.open("youtube.com")

            elif 'open google' in query:
                speak("Here you go to Google\n")
                webbrowser.open("google.com")

            elif 'open stack overflow' in query:
                speak("Here you go to Stack Over flow.Happy coding")
                webbrowser.open("stackoverflow.com")

            elif 'play music' in query or "play song" in query:
                speak("Here you go with music")
                # music_dir = r"E:\Music"
                music_dir = r"D:\Projects 2021-2222\Final-year_Project_II\music"
                songs = os.listdir(music_dir)
                print(songs)
                random = os.startfile(os.path.join(music_dir, songs[1]))

            elif "what is the time" in query:
                strTime = datetime.datetime.now().strftime("%I:%M %p")
                speak(f"Sir, the time is {strTime}")

            elif "what is the date" in query:
                today = date.today()
                d1 = today.strftime("%d/%m/%y")
                print("Date is ", d1)
                speak("Date is" + d1)

            elif 'how are you' in query:
                speak("I am fine, Thank you")
                speak("How are you, Sir")

            elif 'fine' in query:
                speak("It's good to know that your fine")

            elif "what's your name" in query or "What is your name" in query:
                speak("My friends call me"+name_assistant)

            elif 'exit' in query:
                speak("Thanks for giving me your time")
                exit()

            elif "who made you" in query or " who created you" in query:
                speak("I have been created by Deepak sir")

            elif 'joke' in query:
                speak(pyjokes.get_joke())

            elif 'search' in query or 'play' in query:
                query = query.replace("search", "")
                query = query.replace("play", "")
                webbrowser.open(query)

            elif "who i am" in query:
                speak("If you talk then definitely you are human.")

            elif "why you came to world" in query or "to world" in query:
                speak("Thanks to Deepak. further It's a secret")

            elif 'is love' in query:
                speak("It is 7th sense that destroy all other senses")

            elif "who are you" in query:
                speak("I am your virtual assistant created by Deepak sir")

            elif 'reason for you' in query:
                speak("I was created as a Minor project by Mister Deepak sir ")

            elif 'change background' in query:
                ctypes.windll.user32.SystemParametersInfoW(20,
                                                           0,
                                                           "Location of wallpaper",
                                                           0)
                speak("Background changed successfully")

            elif 'lock window' in query:
                speak("locking the device")
                ctypes.windll.user32.LockWorkStation()

            elif 'shutdown system' in query:
                speak("Hold On a Sec ! Your system is on its way to shut down")
                os.system("shutdown /s /t 1")

            elif 'empty recycle bin' in query:
                winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
                speak("Recycle Bin Recycled")

            elif "where i am" in query:
                query = query.replace("where is", "")
                location = query
                speak("User asked to Locate")
                speak(location)
                webbrowser.open("https://www.google.nl / maps / place/" + location + "")

            elif "camera" in query or "take a photo" in query:
                ec.capture(0, " Camera ", "img.jpg")

            elif "restart" in query:
                subprocess.call(["shutdown", "/r"])

            elif "hibernate" in query or "sleep" in query:
                speak("Hibernating")
                subprocess.call("shutdown / h")

            elif "log off" in query or "sign out" in query:
                speak("Make sure all the application are closed before sign-out")
                time.sleep(5)
                subprocess.call(["shutdown", "/l"])

            elif "update assistant" in query:
                speak("After downloading file please replace this file with the downloaded one")
                url = '# url after uploading file'
                r = requests.get(url, stream=True)

                with open("Voice.py", "wb") as Pypdf:

                    total_length = int(r.headers.get('content-length'))

                    for ch in progress.bar(r.iter_content(chunk_size=2391975),
                                           expected_size=(total_length / 1024) + 1):
                        if ch:
                            Pypdf.write(ch)

            elif "Nova" in query:
                wishme()
                speak("Nova 1 point o in your service")

            elif "send email" in query:
                try:
                    speak("What should i say")
                    content = take_command()
                    to = 'dkokane0@gmail.com'
                    send_email(to, content)
                    speak("Email has been sent")
                except Exception as e:
                    print(e)
                    speak("Unable to send Email")

            elif "send message" in query:

                client.messages.create(

                    body='Hello Deepak',

                    from_='+12345678',

                    to="+9112345678")
                speak("Message sent successfully")

            elif "open wikipedia" in query:
                webbrowser.open("wikipedia.com")

            elif "Good Morning" in query:
                speak("A warm" + query)
                speak("How are you Mister")

            elif "will you be my gf" in query:
                speak("I'm not sure about, may be you should give me some time")

            elif "how are you" in query:
                speak("I'm fine, glad you me that")

            elif "i love you" in query:
                speak("It's hard to understand")

            elif "capture" in query or "my screen" in query or "screenshot" in query:
                speak("What should i Name that file")
                path = take_command()
                pathname = path + ".png"
                path1 = r"D:\Pen drive\\" + pathname
                kk = pyautogui.screenshot()
                kk.save(path1)
                os.startfile(r"D:\Pen drive")
                speak("Here is your Screenshot")

            elif "temperature" in query:
                res = app.query(query)
                print(next(res.results).text)
                speak(next(res.results).text)

            elif "calculate" in query:
                speak("What should i calculate")
                gh = take_command().lower()
                res = app.query(gh)
                print(next(res.results).text)
                speak("The ans is" + next(res.results).text)

            elif "what is" in query:
                res = app.query(query)
                print(next(res.results).text)
                speak(next(res.results).text)

            elif "how to" in query:
                res = app.query(query)
                print(next(res.results).text)
                speak(next(res.results).text)

            elif "water" in query:
                notification.notify(
                    title="Please Drink Water Now!!",
                    message="The National Academies of Sciences, "
                            "Engineering, and Medicine determined"
                            " that an adequate daily fluid intake is: "
                            "About 15.5 cups (3.7 liters) of fluids for men. About "
                            "11.5 cups (2.7 liters) of fluids a day for women.",
                    app_icon=r"D:\Projects 2021-2222\Final-year_Project_II\pythonProject\icon.ico",
                    timeout=12
                )
                time.sleep(60 * 60)

            elif "fact" in query or "facts" in query:
                x = randfacts.get_fact()
                print(x)
                speak("did you know that" + x)

            elif "news" in query:
                googlenews = GoogleNews(period='7d')
                googlenews.search('india')
                result = googlenews.result()
                for x in result:
                    print("_" * 50)
                    print("Title--", x['title'])
                    speak("Title--" + x['title'])
                    print("Date/Time--", x['date'])
                    speak("Date/Time--" + x['date'])
                    print("Description--", x['desc'])
                    speak("Description--" + x['desc'])
                    print("Link", x['link'])

            # elif "" in query:
            # Command go here
            # For adding more commands

            else:
                speak('Please say the Command again')


def change_name():
    name_info = name.get()

    file = open("Assistant_name", "w")

    file.write(name_info)

    file.close()

    settings_screen.destroy()

    screen.destroy()


def change_name_window():
    global settings_screen
    global name

    settings_screen = Toplevel(screen)
    settings_screen.title("Settings")
    settings_screen.geometry("300x300")
    settings_screen.iconbitmap('app_icon.ico')

    name = StringVar()

    current_label = Label(settings_screen, text="Current name: " + name_assistant)
    current_label.pack()

    enter_label = Label(settings_screen, text="Please enter your Virtual Assistant's name below")
    enter_label.pack(pady=10)

    name_label = Label(settings_screen, text="Name")
    name_label.pack(pady=10)

    name_entry = Entry(settings_screen, textvariable=name)
    name_entry.pack()

    change_name_button = Button(settings_screen, text="Ok", width=10, height=1, command=change_name)
    change_name_button.pack(pady=10)


def info():
    info_screen = Toplevel(screen)
    info_screen.title("Info")
    info_screen.iconbitmap('app_icon.ico')

    creator_label = Label(info_screen, text="Created by Deepak sir")
    creator_label.pack()

    age_label = Label(info_screen, text=" at the age of 22")
    age_label.pack()

    for_label = Label(info_screen, text="For the purpose of Degree project")
    for_label.pack()


keyboard.add_hotkey("F4", process_audio)


def wikipedia_screen(text):
    wikipedia_screen = Toplevel(screen)
    wikipedia_screen.title(text)
    wikipedia_screen.iconbitmap('app_icon.ico')

    message = Message(wikipedia_screen, text=text)
    message.pack()


def main_screen():
    global screen
    screen = Tk()
    screen.title(name_assistant)
    screen.geometry("500x450")
    screen.iconbitmap('app_icon.ico')

    name_label = Label(text=name_assistant, width=300, bg="black", fg="white", font=("Calibri", 13))
    name_label.pack()

    microphone_photo = PhotoImage(file="download.png")
    microphone_button = Button(image=microphone_photo, command=process_audio)
    microphone_button.pack(pady=10)

    settings_photo = PhotoImage(file="settings.png")
    settings_button = Button(image=settings_photo, command=change_name_window)
    settings_button.pack(pady=10)

    info_button = Button(text="About", command=info)
    info_button.pack(pady=10)

    screen.mainloop()


main_screen()
