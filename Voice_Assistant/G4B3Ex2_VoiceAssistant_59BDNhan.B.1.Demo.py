import speech_recognition as BDNhan59_sr

BDNhan59_rec = BDNhan59_sr.Recognizer()   #Hàm nhận diện dòng nói
with BDNhan59_sr.Microphone() as source:
    print("Adjusting noise ")
    BDNhan59_rec.adjust_for_ambient_noise(source, duration=1)
    print("Nói bằng tiếng Việt đi bạn 5s sau sẽ in ra Text...")
    while True:
        check = input('Sẵn sàng chưa ? y/n ')
        lang = input('Chọn ngôn ngữ: vi (Tiếng Việt),  en (Tiếng Anh),  fr (Tiếng Pháp) ? ')
        if check=='y':
            print('Bắt đầu nói...')
            audio_data = BDNhan59_rec.record(source, duration=5)
            break;
    print("Ket qua nhan dien...")
    try:
        text = BDNhan59_rec.recognize_google(audio_data,language=lang)
    except:
        text = "bạn nói gì mình không hiểu!"
    print(f"Bạn đã nói là: {text}")