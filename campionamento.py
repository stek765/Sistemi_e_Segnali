import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq, fftshift

# Parametri del segnale
fs_original = 1000  # Frequenza di campionamento originale (Hz)
T = 1  # Durata del segnale in secondi
N = fs_original * T  # Numero di campioni
t = np.linspace(0, T, N, endpoint=False)  # Asse temporale

# Segnale continuo originale: somma di due sinusoidi
f1, f2 = 50, 120  # Frequenze delle sinusoidi (Hz)
signal = np.sin(2 * np.pi * f1 * t) + 0.5 * np.sin(2 * np.pi * f2 * t)

# Campionamento con una frequenza più bassa
fs_sampled = 300  # Frequenza di campionamento ridotta (Hz)
T_sampled = 1/fs_sampled
N_sampled = int(T * fs_sampled)
t_sampled = np.linspace(0, T, N_sampled, endpoint=False)
signal_sampled = np.sin(2 * np.pi * f1 * t_sampled) + 0.5 * np.sin(2 * np.pi * f2 * t_sampled)

# FFT originale
freqs_original = fftfreq(N, 1/fs_original)
fft_original = np.abs(fft(signal))

# FFT campionata
fft_sampled = np.abs(fft(signal_sampled))
freqs_sampled = fftfreq(N_sampled, 1/fs_sampled)

# Usiamo fftshift per vedere l'intero spettro
fft_sampled_shifted = fftshift(fft_sampled)
freqs_sampled_shifted = fftshift(freqs_sampled)

# Plot del segnale nel tempo
plt.figure(figsize=(12, 6))
plt.subplot(2, 2, 1)
plt.plot(t, signal, label="Segnale continuo")
plt.scatter(t_sampled, signal_sampled, color='red', label="Campioni")
plt.xlabel("Tempo (s)")
plt.ylabel("Ampiezza")
plt.title("Segnale originale e campionato")
plt.legend()

# Spettro prima del campionamento
plt.subplot(2, 2, 2)
plt.plot(freqs_original[:N//2], fft_original[:N//2])
plt.xlabel("Frequenza (Hz)")
plt.ylabel("Ampiezza")
plt.title("Spettro originale")

# Spettro dopo il campionamento con fftshift per mostrare le repliche
plt.subplot(2, 2, 3)
plt.plot(freqs_sampled_shifted, fft_sampled_shifted, color='red')
plt.xlabel("Frequenza (Hz)")
plt.ylabel("Ampiezza")
plt.title("Spettro dopo il campionamento (con repliche)")
plt.xlim(-fs_sampled, fs_sampled)  # Mostriamo tutto lo spettro

plt.tight_layout()
plt.show()
