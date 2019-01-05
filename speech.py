import speech_recognition as sr
r=sr.Recognizer()
fn=open("myspeech.text","w+")
while(1):
    with sr.Microphone() as source:
        a=r.listen(source)
    try:
        print(r.recognize_google(a))
        with open("myspeech.wav","wb") as f:
            f.write(a.get_wav_data())
        
        fn.write(r.recognize_google(a))
        fn.write("\n")
        fn=open("myspeech.text","a+")
    except Exception:
        print("something is wrong")
        break
    
