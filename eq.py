import numpy as np
import pyaudio
import matplotlib.pyplot as plt
import scipy.signal as signal

# Parametri audio
FORMAT = pyaudio.paInt16  # Formato a 16 bit
CHANNELS = 1  # Audio mono
RATE = 44100  # Frequenza di campionamento (44.1 kHz, standard)
CHUNK = 1024  # Numero di campioni per blocco
# Usa numpy invece di scipy.signal
WINDOW = np.hanning(CHUNK)  # Finestra di Hann per ridurre il leakage



# Inizializza PyAudio
p = pyaudio.PyAudio()
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

# Crea la figura per il grafico
plt.ion()  # Modalità interattiva
fig, ax = plt.subplots()
frequencies = np.fft.rfftfreq(CHUNK, d=1/RATE)  # Frequenze positive
line, = ax.semilogx(frequencies, np.zeros(len(frequencies)))  # Grafico logaritmico

ax.set_xlim(20, RATE // 2)  # Limita tra 20 Hz e la metà della frequenza di campionamento
ax.set_ylim(0, 100)  # Imposta il range dell'ampiezza
ax.set_xlabel("Frequenza (Hz)")
ax.set_ylabel("Ampiezza")
ax.set_title("Equalizzatore in Tempo Reale")

print("🎤 Acquisizione audio in corso... Parla nel microfono!")

# Loop per aggiornare l'equalizzatore in tempo reale
try:
    while True:
        data = np.frombuffer(stream.read(CHUNK, exception_on_overflow=False), dtype=np.int16)
        fft_data = np.fft.rfft(data * WINDOW)  # Applica la FFT con finestra di Hann
        magnitude = np.abs(fft_data)  # Prende il modulo della FFT
        magnitude_db = 20 * np.log10(magnitude + 1e-6)  # Converti in dB evitando log(0)

        line.set_ydata(magnitude_db)  # Aggiorna il grafico
        plt.pause(0.01)  # Pausa breve per aggiornare la grafica

except KeyboardInterrupt:
    print("\n🎤 Interrotto dall'utente. Chiusura...")
    stream.stop_stream()
    stream.close()
    p.terminate()
