from vosk import Model , KaldiRecognizer
import pyaudio
import json 

#cargar el modelo en carpeta
model = Model("vosk-model-small-es-0.42/")
#cargar reconocedor con 16 khZ
rec = KaldiRecognizer(model, 16000)

#Creación de instancia pyaudio 
p = pyaudio.PyAudio()


#Apertura de stream de antrada 
#formato pant16 = audio de 16 bits (vosk)
#chanels = 1 es audio mono
#rate de 16000 son lor 16kHz
#input = entrada de microfono
#frames del buffer = tamano del buffer

stream = p.open(format = pyaudio.paInt16, channels = 1, rate = 16000, input=True, frames_per_buffer=8000)

#inicio de stream
stream.star_stream()

print("Escuchando\n")

#entrada a bucle infinito para escuchar audio, captura de frames, exception evita errores de lento procesamiento
try:
    while True:
        data = stream.read(4000, exception_on_overflow=False)
        if rec.AcceptWaveform(data): #verifica si se reconoce una frase completa
            result = json.loads(rec.Result()) #transcripción a JSON
            print(" Texto\n:", result.get("text", "")) #impresion de texto
except KeyboardInterrupt:
    print("\n Detenido por el usuario.")#detener el bucle con ctrl + c

#Terminar todo, limpiar y crerrar
finally:
    stream.stop_stream()
    stream.close()
    p.terminate()










