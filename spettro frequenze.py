import numpy as np
import cv2
import matplotlib.pyplot as plt

def fourier_spectrum(image_path):
    # Carica l'immagine in scala di grigi
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    if img is None:
        print("Errore: Immagine non trovata.")
        return
    
    # Calcola la Trasformata di Fourier 2D
    f = np.fft.fft2(img)
    
    # Sposta le basse frequenze al centro
    fshift = np.fft.fftshift(f)
    
    # Calcola lo spettro di ampiezza (magnitude spectrum)
    magnitude_spectrum = 20 * np.log(np.abs(fshift) + 1)  # Evita log(0)

    # Visualizza l'immagine originale e lo spettro
    plt.figure(figsize=(10,5))
    
    # Immagine originale
    plt.subplot(1,2,1)
    plt.imshow(img, cmap='gray')
    plt.title('Immagine Originale')
    plt.axis('off')
    
    # Spettro di Fourier
    plt.subplot(1,2,2)
    plt.imshow(magnitude_spectrum, cmap='gray')
    plt.title('Spettro di Fourier')
    plt.axis('off')
    
    plt.show()

# ---- ESEMPIO D'USO ----
image_path = "immagine2.jpg"  # Sostituisci con il tuo file
fourier_spectrum(image_path)
