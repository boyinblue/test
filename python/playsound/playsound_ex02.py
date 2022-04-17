import playsound
import threading
import ctypes
import time

play_thread = None

def stop_mp3():
    global play_thread

    if not play_thread:
        return

    thread_id = None
    if hasattr(play_thread, '_thread_id'):
        thread_id = play_thead._thread_id
    else:
        for id, thread in threading._active.items():
            print("thread :", id, thread)
            if thread is play_thread:
                thread_id = id
                break

    print("Try to thread exit :", thread_id)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id,
                    ctypes.py_object(SystemExit))
    if res > 1:
        ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 0)
        print('Exception raise failure')

def play_mp3(filename):
    global play_thread

    stop_mp3()

    play_thread = threading.Thread(target=playsound.playsound, 
                    args=(filename,), daemon=True)
    play_thread.start()

def main():
    while True:
        cmd = input("cmd :")
        play_mp3("sample.mp3")

if __name__ == '__main__':
    main()
