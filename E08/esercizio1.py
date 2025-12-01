import numpy as np
import pandas as pd
from scipy import constants, fft
from scipy import optimize
import matplotlib.pyplot as plt

# leggo i dati
dati1 = pd.read_csv('https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica-2025/refs/heads/main/dati/trasformate_fourier/data_sample1.csv')
dati2 = pd.read_csv('https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica-2025/refs/heads/main/dati/trasformate_fourier/data_sample2.csv')
dati3 = pd.read_csv('https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica-2025/refs/heads/main/dati/trasformate_fourier/data_sample3.csv')

# grafico segnali in ingresso
tempo1 = dati1['time']
tempo2 = dati2['time']
tempo3 = dati3['time']

ampiezza1 = dati1['meas']
ampiezza2 = dati2['meas']
ampiezza3 = dati3['meas']

plt.plot(tempo1, ampiezza1, color = 'blue', label='dati 1')
plt.plot(tempo2, ampiezza2, color = 'green', label='dati 2')
plt.plot(tempo3, ampiezza3, color = 'red', label='dati 3')
plt.xlabel('tempo (s)')
plt.ylabel('Ampiezza')
plt.legend(loc = 'upper right')
plt.grid(True)
plt.show()

# Grafico spettro di potenza (Coefficienti di Fourier al quadrato in funzione della frequenza)
# trasformate di fourier
fft_1 = fft.rfft(np.array(ampiezza1))
dt1 = tempo1.iloc[1] - tempo1.iloc[0]
freq_1 = fft.rfftfreq(len(ampiezza1), d = dt1)
pot_1 = np.abs(fft_1)**2

fft_2 = fft.rfft(np.array(ampiezza2))
dt2 = tempo2.iloc[1] - tempo2.iloc[0]
freq_2 = fft.rfftfreq(len(ampiezza2), d = dt2)
pot_2 = np.abs(fft_2)**2

fft_3 = fft.rfft(np.array(ampiezza3))
dt3 = tempo3.iloc[1] - tempo3.iloc[0]
freq_3 = fft.rfftfreq(len(ampiezza3), d = dt3)
pot_3 = np.abs(fft_3)**2

fig, ax = plt.subplots(1,3, figsize=(12,6))
ax[0].plot(freq_1, pot_1, color= 'blue')
ax[0].set_title('Spettro di potenza 1', fontsize=15, color='blue')
ax[0].set_xlabel('frequenza (Hz)')
ax[0].set_ylabel('Potenza')
ax[0].set_xscale('log')
ax[0].set_yscale('log')
ax[0].grid('True')

ax[1].plot(freq_2, pot_2, color= 'green')
ax[1].set_title('Spettro di potenza 2', fontsize=15, color='green')
ax[1].set_xlabel('frequenza (Hz)')
ax[1].set_ylabel('Potenza')
ax[1].set_xscale('log')
ax[1].set_yscale('log')
ax[1].grid('True')

ax[2].plot(freq_3, pot_3, color= 'red')
ax[2].set_title('Spettro di potenza 3', fontsize=15, color='red')
ax[2].set_xlabel('frequenza (Hz)')
ax[2].set_ylabel('Potenza')
ax[2].set_xscale('log')
ax[2].set_yscale('log')
ax[2].grid('True')
plt.show()

# fit con white, pink e red noise
def funzione_fit(f, A, beta):
    return A/(np.power(f,beta))

def linear_fit(log_f, A, beta):
    return np.log10(A) - beta * log_f

mask1 = freq_1 > 0
params1, params_covariance1 = optimize.curve_fit(funzione_fit, freq_1[mask1], pot_1[mask1], p0 = [5,0])
print('I parametri trovati sono: ', params1)

mask2 = freq_2 > 0
params2, params_covariance2 = optimize.curve_fit(funzione_fit, freq_2[mask2], pot_2[mask2], p0 = [5,0])
print('I parametri trovati sono: ', params2)

mask3 = freq_3 > 0
params3, params_covariance3 = optimize.curve_fit(linear_fit, np.log10(freq_3[mask3]), np.log10(pot_3[mask3]), p0 = [5,2])
print('I parametri trovati sono: ', params3)

fig, ax = plt.subplots(1,3, figsize=(12,6))
ax[0].plot(freq_1[mask1], pot_1[mask1], color= 'blue')
ax[0].plot(freq_1[mask1], funzione_fit(freq_1[mask1], params1[0],params1[1]), color='gold')
ax[0].set_title('Spettro di potenza 1', fontsize=15, color='blue')
ax[0].set_xlabel('frequenza (Hz)')
ax[0].set_ylabel('Potenza')
ax[0].set_xscale('log')
ax[0].set_yscale('log')
ax[0].grid('True')

ax[1].plot(freq_2[mask2], pot_2[mask2], color= 'green')
ax[1].plot(freq_2[mask2], funzione_fit(freq_2[mask2], params2[0],params2[1]), color='gold')
ax[1].set_title('Spettro di potenza 2', fontsize=15, color='green')
ax[1].set_xlabel('frequenza (Hz)')
ax[1].set_ylabel('Potenza')
ax[1].set_xscale('log')
ax[1].set_yscale('log')
ax[1].grid('True')

ax[2].plot(freq_3[mask3], pot_3[mask3], color= 'red')
ax[2].plot(freq_3[mask3], funzione_fit(freq_3[mask3], params3[0],params3[1]), color='gold')
ax[2].set_title('Spettro di potenza 3', fontsize=15, color='red')
ax[2].set_xlabel('frequenza (Hz)')
ax[2].set_ylabel('Potenza')
ax[2].set_xscale('log')
ax[2].set_yscale('log')
ax[2].grid('True')
plt.show()