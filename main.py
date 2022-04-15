import speech_recognition as sr
filename = "1650051437540.wav"
ID = 'id'
key = 'key'
with open(ID, 'r') as guil:
    global client_id
    almostGuild = guil.read()
    client_id = almostGuild
with open(key, 'r') as toke:
    global client_key
    almostToken = toke.read()
    client_key = almostToken
# initialize the recognizer
r = sr.Recognizer()
# open the file
with sr.AudioFile(filename) as source:
    # listen for the data (load audio to memory)
    audio_data = r.record(source)
    # recognize (convert from speech to text)
    text = r.recognize_houndify(audio_data, client_id, client_key)
    print(text)
