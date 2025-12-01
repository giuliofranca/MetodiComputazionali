import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
from scipy import constants, fft

# leggo i file e trasformo in DataFrame
dati1 = pd.read_csv('https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica-2025/refs/heads/main/dati/trasformate_fourier/4FGL_J2202.7%2B4216_weekly_9_15_2023_mcf.csv')
dati2 = pd.read_csv('https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica-2025/refs/heads/main/dati/trasformate_fourier/4FGL_J1256.1-0547_weekly_9_15_2023_mcf.csv')
dati3 = pd.read_csv('https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica-2025/refs/heads/main/dati/trasformate_fourier/4FGL_J2253.9%2B1609_weekly_9_15_2023_mcf.csv')

# grafico con flusso in funzione del giorno giuliano, sorgenti sovrapposte
plt.plot(dati1['Julian Date'], dati1['Photon Flux [0.1-100 GeV](photons cm-2 s-1)'], color = 'royalblue', label = 'sorgente 1')
plt.plot(dati2['Julian Date'], dati2['Photon Flux [0.1-100 GeV](photons cm-2 s-1)'], color = 'green', label = 'sorgente 2')
plt.plot(dati3['Julian Date'], dati3['Photon Flux [0.1-100 GeV](photons cm-2 s-1)'], color = 'tomato', label = 'sorgente 3')
plt.legend(loc = 'upper right')
plt.xlabel('Giorno giuliano')
plt.ylabel('flusso di fotoni')
plt.grid('True')
plt.show()

# 3 grafici diversi
fig, ax = plt.subplots(1,3,figsize=(12,6))
ax[0].plot(dati1['Julian Date'], dati1['Photon Flux [0.1-100 GeV](photons cm-2 s-1)'], color = 'royalblue')
ax[0].set_xlabel('Giorno giuliano')
ax[0].set_ylabel('Flusso di fotoni')
ax[0].grid('True')
ax[0].set_title('Sorgente 1')

ax[1].plot(dati2['Julian Date'], dati2['Photon Flux [0.1-100 GeV](photons cm-2 s-1)'], color = 'green')
ax[1].set_xlabel('Giorno giuliano')
ax[1].set_ylabel('Flusso di fotoni')
ax[1].grid('True')
ax[1].set_title('Sorgente 2')

ax[2].plot(dati3['Julian Date'], dati3['Photon Flux [0.1-100 GeV](photons cm-2 s-1)'], color = 'tomato')
ax[2].set_xlabel('Giorno giuliano')
ax[2].set_ylabel('Flusso di fotoni')
ax[2].grid('True')
ax[2].set_title('Sorgente 2')
plt.show()

# Calcolo la trasformata di Fourier
fft1 = fft.rfft(np.array(dati1['Photon Flux [0.1-100 GeV](photons cm-2 s-1)']))
dt1 = dati1['Julian Date'].iloc[1] - dati1['Julian Date'].iloc[0]
freq_1 = fft.rfftfreq(len(dati1['Julian Date']), dt1)
pot_1 = abs(fft1)**2

fft2 = fft.rfft(np.array(dati2['Photon Flux [0.1-100 GeV](photons cm-2 s-1)']))
dt2 = dati2['Julian Date'].iloc[1] - dati2['Julian Date'].iloc[0]
freq_2 = fft.rfftfreq(len(dati2['Julian Date']), dt2)
pot_2 = abs(fft2)**2

fft3 = fft.rfft(np.array(dati3['Photon Flux [0.1-100 GeV](photons cm-2 s-1)']))
dt3 = dati3['Julian Date'].iloc[1] - dati3['Julian Date'].iloc[0]
freq_3 = fft.rfftfreq(len(dati3['Julian Date']), dt3)
pot_3 = abs(fft3)**2

# grafici trasformate di Fourier
fig, ax = plt.subplots(1,3, figsize=(12,6))
ax[0].plot(freq_1, pot_1, color='royalblue')
ax[0].set_title('Sorgente 1')
ax[0].set_xlabel('Frequenza')
ax[0].set_ylabel('Potenza')
ax[0].grid('True')

ax[1].plot(freq_2, pot_2, color='royalblue')
ax[1].set_title('Sorgente 2')
ax[1].set_xlabel('Frequenza')
ax[1].set_ylabel('Potenza')
ax[1].grid('True')

ax[2].plot(freq_3, pot_3, color='royalblue')
ax[2].set_title('Sorgente 3')
ax[2].set_xlabel('Frequenza')
ax[2].set_ylabel('Potenza')
ax[2].grid('True')
plt.show()

# fit: che tipo di andamento è? white/red/pink noise
def funzione_fit(log_f,A,beta):
    return np.log10(A) - beta*log_f

def f(f, A, beta):
    return A/(np.power(f,beta))

mask1 = freq_1 > 0
mask2 = freq_2 > 0
mask3 = freq_3 > 0
params1, params_covariance1 = optimize.curve_fit(funzione_fit, np.log10(freq_1[mask1]), np.log10(pot_1[mask1]), p0 = [5,2])
print('I parametri trovati sono: ', params1)

params2, params_covariance2 = optimize.curve_fit(funzione_fit, np.log10(freq_2[mask2]), np.log10(pot_2[mask2]), p0 = [5,2])
print('I parametri trovati sono: ', params2)

params3, params_covariance3 = optimize.curve_fit(funzione_fit, np.log10(freq_3[mask3]), np.log10(pot_3[mask3]), p0 = [5,2])
print('I parametri trovati sono: ', params3)

fig, ax = plt.subplots(1,3, figsize=(12,6))
ax[0].plot(freq_1, pot_1, color='royalblue')
ax[0].plot(freq_1,f(freq_1,params1[0],params1[1]), color = 'gold')
ax[0].set_title('Sorgente 1')
ax[0].set_xlabel('Frequenza')
ax[0].set_ylabel('Potenza')
ax[0].grid('True')

ax[1].plot(freq_2, pot_2, color='green')
ax[1].plot(freq_2,f(freq_2,params2[0],params2[1]), color = 'gold')
ax[1].set_title('Sorgente 2')
ax[1].set_xlabel('Frequenza')
ax[1].set_ylabel('Potenza')
ax[1].grid('True')

ax[2].plot(freq_3, pot_3, color='yellow')
ax[2].plot(freq_3,f(freq_3,params3[0],params3[1]), color = 'gold')
ax[2].set_title('Sorgente 3')
ax[2].set_xlabel('Frequenza')
ax[2].set_ylabel('Potenza')
ax[2].grid('True')
plt.show()
