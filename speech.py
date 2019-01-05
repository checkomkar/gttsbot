import speech_recognition as sr
import os
import time
from subprocess import call
r=sr.Recognizer()
fn=open("myspeech.text","w+")
while(1):
    with sr.Microphone() as source:
        a=r.listen(source)
    try:
        print(r.recognize_google(a))        
        with open("myspeech.riff","wb") as f:
            f.write(a.get_wav_data())
        os.system("sox -S myspeech.riff output.wav rate -L -s 16000")
        time.sleep(1)
        os.system("sh auto.sh")
        fn.write(r.recognize_google(a))
        fn.write("\n")
        fn=open("myspeech.text","a+")
    except Exception:
        print("something is wrong")
        break
    
