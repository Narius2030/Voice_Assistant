import speech_recognition as BDNhan59_sr
from gtts import gTTS
import os
import time
import playsound

BDNhan59_rec = BDNhan59_sr.Recognizer()
text = ''
dict_of_code = {
    'python': 'print',
    'csharp': 'Console.WriteLine'
}

def BDNhan59_read_out_loud(text, language):
    source = gTTS(text=text, lang = language)
    filename = input('Save as: ')
    source.save(filename)
    playsound.playsound(filename)

with BDNhan59_sr.Microphone() as source:
    #hiệu chỉnh mic để chuẩn bị nói
    print("Hieu chinh nhieu trươc khi noi !")
    BDNhan59_rec.adjust_for_ambient_noise(source, duration=1)
    #nhận lời nói của người dùng từ MIc mặc định lưu dữ liệu âm thanh vào audio_data print("Nói tiếng Việt đi, sau 5s sẽ in ra văn bản!") audio_data = r.record(Source, duration = 5)
    while True:
        check = input('Sẵn sàng chưa ? y/n ')
        lang = input('Chọn ngôn ngữ: vi (Tiếng Việt),  en (Tiếng Anh),  fr (Tiếng Pháp) ? ')
        if check=='y':
            print('Bắt đầu nói...')
            audio_data = BDNhan59_rec.record(source, duration=5)
            break
    #In ra văn bản text
    print("KẾT QUẢ NHẬN DIỆN ..................")
    #chuyển lời nói thành văn bản
    try:
        text = BDNhan59_rec.recognize_google(audio_data,language=lang)
    except:
        text = "Bạn nói gì nghe không rõ...!"
    #in kết quả ra nhận diện giọng nói
    print(f"Bạn đã nói là :	{text}")
    BDNhan59_read_out_loud(text, lang)
    #Tạo code
    for key in dict_of_code:
        if key in text.lower() :
            print(f'{dict_of_code[key]}("Hello world!")')
    
