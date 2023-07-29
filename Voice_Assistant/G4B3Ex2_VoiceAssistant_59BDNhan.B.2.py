import time
import speech_recognition as sr
from gtts import gTTS
import os
from googletrans import Translator
import playsound
import pyttsx3 as psx3

BDNhan59_rec = sr.Recognizer()   #Hàm nhận diện dòng nói
BDNhan59_translator = Translator()
engine = psx3.init()

def BDNhan59_read_out_loud(mytext, language):
    source = gTTS(text=mytext, lang = language)
    filename = input('Save as: ')
    source.save(filename)
    playsound.playsound(filename)

with sr.Microphone() as source:
    print("Điều chỉnh giọng nói ")
    BDNhan59_rec.adjust_for_ambient_noise(source, duration=1)
    while True:
        check = input(('Sẵn sàng chưa ? y/n '))
        lang = input('Chọn ngôn ngữ:   vi (Tiếng Việt),  en (Tiếng Anh),  fr (Tiếng Pháp) ? ')
        trns_lang = input('Chọn ngôn ngữ dịch:   vi (Tiếng Việt),  en (Tiếng Anh),  fr (Tiếng Pháp) ? ')
        if check=='y':
            print('Bắt đầu nói...')
            audio_data = BDNhan59_rec.record(source, duration=5)
            break
    try:
        text = BDNhan59_rec.recognize_google(audio_data, language=lang)
    except:
        text = "bạn nói gì mình không hiểu!"
    trns_text = BDNhan59_translator.translate(text, dest=trns_lang)
    print(f"Bạn đã nói là: {trns_text.text}")
    BDNhan59_read_out_loud(trns_text.text, trns_lang)
