import playsound
import os
import tempfile

temp_file = None

def stop_mp3():
    global temp_file

    if not temp_file
        return

    os.remove(temp_file)

def play_mp3(filename):
    global temp_file

    fd, filename = tempfile.mkstemp()

    stop_mp3()

    

playsound.playsound("sample.mp3", block=False)
time.sleep(5)
