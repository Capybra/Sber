import os
import sys
import time
from threading import Thread
import webview
from desktop_app import start_webviewt

def start_webview():
    window = webview.create_window('Staff', 'http://localhost:8000/staff/login/', fullscreen=True)
    webview.start()

def start_django():
    if sys.platform in ['win32', 'win64']:
        os.system("python manage.py runserver {}:{}".format('127.0.0.1', '8000'))
    else:
        os.system("python3 manage.py runserver {}:{}".format('127.0.0.1', '8000'))

if __name__ == '__main__':
    Thread(target=start_django).start()
    # Ждем некоторое время для запуска сервера Django
    time.sleep(3)
    start_webview()
    time.sleep(1)
    start_webviewt()