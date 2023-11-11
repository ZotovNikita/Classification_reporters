from vosk import KaldiRecognizer
import pyaudio

def vosk_voice_recignize(model):
    rec = KaldiRecognizer(model, 44100)
    p = pyaudio.PyAudio()
    stream = p.open(
        format=pyaudio.paInt16, 
        channels=1, 
        rate=44100, 
        input=True, 
        frames_per_buffer=44100
    )
    stream.start_stream()

    while True:
        data = stream.read(44100)
        if rec.AcceptWaveform(data):
            return rec.Result()

