import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Say Something")
    audio = r.listen(source)

#try:
#    text = r.recognize_google(audio)
#    print(f"You said: '{text}'")
#except:
#    print("Translation Failed.")

##Create new .wav file with recording in it.
#with open("wavaudio.wav", "wb") as f:
#    f.write(audio.get_wav_data())
#
