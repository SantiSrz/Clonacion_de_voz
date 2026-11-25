import sounddevice as sd
from scipy.io.wavfile import write
import os

os.makedirs("data", exist_ok=True)
fs = 44100  # Frecuencia de muestreo estándar

def grabar_audio(nombre_archivo, segundos=6):
    print(f"\n--- Preparando: {nombre_archivo} ({segundos}s) ---")
    input("Pulsa ENTER y empieza a hablar...")
    print("Grabando...")
    audio = sd.rec(int(segundos * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    ruta = os.path.join("data", nombre_archivo)
    write(ruta, fs, audio)
    print(f"Guardado en {ruta}")

# 1. Tu voz clara (con pausa marcada de ~1s en medio)
grabar_audio("A1_clara.wav", 6)

# 2. Tu voz con segunda condición (misma frase, lejos del micro o con ruido de fondo)
grabar_audio("A1_ruido.wav", 6)

# 3. Tu voz diciendo otra frase totalmente distinta
grabar_audio("A2_otra_frase.wav", 6)

# 4. Otra persona (p. ej. en casa) diciendo exactamente la misma frase que A1
grabar_audio("B1_otra_persona.wav", 6)