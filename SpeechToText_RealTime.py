# pip install SpeechRecognition
# pip install pyaudio
# pip install keyboard

import speech_recognition as sr
import pyaudio
import threading
import keyboard

sr.Microphone.list_microphone_names()

mic = sr.Microphone(1)

recog = sr.Recognizer()
is_recording = False


def listen_and_recognize():
    global is_recording
    with mic as source:
        print('เริ่มพูดได้เลย')
        while is_recording:
            audio = recog.listen(source)
            voice_data = recog.recognize_google(audio, language='th')
            print(voice_data)


def start_listening():
    global is_recording
    while True:
        if keyboard.is_pressed('R'):
            print("กำลังบันทึกเสียง...")
            is_recording = True
            threading.Thread(target=listen_and_recognize).start()
            while keyboard.is_pressed('R'):
                pass  # รอให้ปล่อยปุ่ม R
            print("หยุดการบันทึกเสียง")
            is_recording = False
            # break  # หยุดลูปเมื่อปล่อยปุ่ม R


# เริ่มการรับเสียงใน thread
threading.Thread(target=start_listening).start()
