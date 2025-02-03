# rappresentazione di un suono complesso nel piano complesso!
'''
Questo concetto è usato per visualizzare onde sonore!
Se prendi il segnale di una chitarra, il punto finale rappresenta l'andamento complesso del suono nel piano reale-immaginario.
Un suono puro → traccerebbe una circonferenza (come un solo fasore).
Un suono con più armoniche → formerà curve intricate come quelle che vedi.
Un suono complesso (chitarra distorta) → genererebbe un grafico ancora più caotico, perché ci sono molte frequenze diverse in gioco.
'''
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parametri del segnale
T = 1  # Secondi (periodo base)
fs = 100  # Frequenza di campionamento (100 campioni al secondo)
t = np.linspace(0, T, fs, endpoint=False)  # Intervallo di tempo

# Frequenze e ampiezze delle sinusoidi
f1, f2, f3 = 1, 3, 5  # Frequenze
A1, A2, A3 = 3, 2, 1  # Ampiezze

# Creiamo la figura per l'animazione
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-4, 4)
ax.set_ylim(-4, 4)
ax.set_aspect('equal')
ax.set_xticks([])
ax.set_yticks([])
ax.set_title("Combinazione dei Fasori")

# Creiamo le linee per i fasori
lines = [ax.plot([], [], lw=2)[0] for _ in range(3)]  # Tre fasori
result_line, = ax.plot([], [], 'ro')  # Punto finale

# Inizializzazione delle linee
def init():
    for line in lines:
        line.set_data([], [])
    result_line.set_data([], [])
    return lines + [result_line]

# Funzione di aggiornamento per l'animazione
def update(frame):
    t = frame / fs  # Tempo attuale

    # Fasori rotanti
    angles = [2 * np.pi * f * t for f in [f1, f2, f3]]  # Angoli per le tre frequenze
    vectors = [A * np.exp(1j * angle) for A, angle in zip([A1, A2, A3], angles)]  # Vettori complessi

    # Calcoliamo le posizioni cumulative dei fasori
    positions = np.cumsum(vectors)  # Somma cumulativa dei vettori

    # Aggiorniamo le linee
    start = np.array([0, 0])
    for i, line in enumerate(lines):
        end = np.array([positions[i].real, positions[i].imag])
        line.set_data([start[0], end[0]], [start[1], end[1]])
        start = end

    # Punto finale della somma dei fasori
    result_line.set_data([start[0]], [start[1]]) 


    return lines + [result_line]

# Creiamo l'animazione
ani = animation.FuncAnimation(fig, update, frames=fs, init_func=init, blit=True, interval=30)

# Mostriamo l'animazione
plt.show()
