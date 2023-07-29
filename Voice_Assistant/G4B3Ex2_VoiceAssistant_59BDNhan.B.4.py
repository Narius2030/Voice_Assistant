import time
import speech_recognition as sr
from gtts import gTTS
import os
from googletrans import Translator
import playsound

BDNhan59_rec = sr.Recognizer()   #Hàm nhận diện dòng nói
BDNhan59_translator = Translator()

def BDNhan59_read_out_loud(mytext, language):
    source = gTTS(text=mytext, lang = language)
    filename = input('Save as: ')
    source.save(filename)
    playsound.playsound(filename)

with sr.Microphone() as source:
    print("Điều chỉnh giọng nói ")
    BDNhan59_rec.adjust_for_ambient_noise(source, duration=1)
    #Xử lý giọng nói
    lang = input('Chọn ngôn ngữ:   vi (Tiếng Việt),  en (Tiếng Anh),  fr (Tiếng Pháp) ? ')
    trns_lang = input('Chọn ngôn ngữ dịch:   vi (Tiếng Việt),  en (Tiếng Anh),  fr (Tiếng Pháp) ? ')
    if input('Bạn muốn nhập chữ hay nói "c" là chữ, "n" là nói ? ') == 'n':
        while True:        
            check = input(('Sẵn sàng chưa ? y/n '))
            if check == 'y':
                print('Bắt đầu nói...')
                audio_data = BDNhan59_rec.record(source, duration=5)
                break
        try:
            text = BDNhan59_rec.recognize_google(audio_data, language=lang)
        except:
            text = "bạn nói gì mình không hiểu!"
    else:
        text = input('Nhập: ')
    #Dịch văn bản
    trns_text = BDNhan59_translator.translate(text, dest=trns_lang)
    #Xuất text và file.mp3
    print(f"Bạn đã nói là: {text}\n Dịch sang {trns_lang}: {trns_text.text}")
    BDNhan59_read_out_loud(trns_text.text, trns_lang)
