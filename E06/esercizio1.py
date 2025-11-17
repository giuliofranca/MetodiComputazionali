import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import optimize

dati = pd.read_csv('http://opendata.cern.ch/record/5203/files/Jpsimumu.csv')
lista_masse = []
for i in range(0,20000):
    massa = np.sqrt((dati['E1'][i]+dati['E2'][i])**2 - (dati['px1'][i]+dati['px2'][i])**2 - (dati['py1'][i]+dati['py2'][i])**2 - (dati['pz1'][i]+dati['pz2'][i])**2 )
    lista_masse.append(massa)

array_masse = np.array(lista_masse)

# creo istogramma delle masse calcolate
n, bins, p = plt.hist(array_masse, bins = 200, color = 'gold')
plt.xlabel('Massa invariante (GeV)')
plt.show()

# creo istogramma delle masse calcolate mascherando intervallo
n, bins, p = plt.hist(array_masse, bins = 200,range = (2.8,3.4), color = 'gold')
plt.xlabel('Massa invariante (kg * m/s^2)')
plt.show()

# definisco funzione di fit per i dati attorno al picco centrale massimo
def fg1(x,A,m,sigma,p1,p0):
    return A*np.power(np.e,-((x-m)**2)/(2*np.power(sigma,2))) + p1*x + p0

centri_bins = 0.5 * (bins[:-1] + bins[1:])
mask = n > 0
params, params_covariance = optimize.curve_fit(fg1, centri_bins[mask],n[mask], sigma = np.sqrt(n[mask]))
print('params = ', params)
print('params covariance = ', params_covariance)
print('errori params', np.sqrt(params_covariance.diagonal()))

# plotto grafico istogramma sovrapposto a curva di fit
fig, ax = plt.subplots(1,3, figsize=(12,6))
ax[0].errorbar(centri_bins[mask],n[mask], yerr = np.sqrt(n[mask]), fmt='o',color='yellow')
ax[0].plot(centri_bins[mask],fg1(centri_bins[mask],params[0],params[1],params[2],params[3],params[4]), color='blue')
ax[0].set_title('Fit dati con gaussiana')
ax[0].grid(True)


# plot dello scarto fra dati e fit
ax[1].errorbar(centri_bins[mask],n[mask]-fg1(centri_bins[mask],params[0],params[1],params[2],params[3],params[4]), yerr = np.sqrt(n[mask]), fmt = 'o', color='green')
ax[1].axhline(y=0, color= 'red', linestyle='--')

ax[2].errorbar(centri_bins[mask],(n[mask]-fg1(centri_bins[mask],params[0],params[1],params[2],params[3],params[4]))/np.sqrt(n[mask]), yerr= np.sqrt(n[mask]), color='green')
ax[2].axhline(y=0, color= 'red', linestyle='--')
plt.show()

# chi quadro
somma = 0
for i in range(n[mask].size):
    somma = somma + ((n[mask][i]-fg1(centri_bins[mask][i],params[0],params[1],params[2],params[3],params[4]))**2)/(np.sqrt(n[mask][i]))**2
chi_quadro = somma
# chi quadro ridotto
chi_quadro_ridotto = chi_quadro / (n[mask].size - 4)
print('Chi quadro = ', chi_quadro)
print('Chi quadro ridotto = ', chi_quadro_ridotto)

# ripeto il fit definendo una gaussiana "doppia"
def fg2(x,A1,m,sigma1,A2,sigma2,p1,p0):
    return A1*np.power(np.e,-((x-m)**2)/(2*np.power(sigma1,2)))+ A2*np.power(np.e,-((x-m)**2)/(2*np.power(sigma2,2))) + p1*x + p0

params_best, params_covariance_best = optimize.curve_fit(fg2,centri_bins[mask], n[mask], sigma = np.sqrt(n[mask]))
print('nuovi parametri = ', params_best)
print('matrice di covarianza migliore ', params_covariance_best)
print('errori params', np.sqrt(params_covariance_best.diagonal()))

# plot nuovo fit
fig, ax = plt.subplots(1,3, figsize=(12,6))
ax[0].errorbar(centri_bins[mask],n[mask], yerr = np.sqrt(n[mask]), fmt='o',color='yellow')
ax[0].plot(centri_bins[mask],fg2(centri_bins[mask],params_best[0],params_best[1],params_best[2],params_best[3],params_best[4],params_best[5],params_best[6]), color='blue')
ax[0].set_title('Fit dati con gaussiana')
ax[0].grid(True)


# plot dello scarto fra dati e fit
ax[1].errorbar(centri_bins[mask],n[mask]-fg2(centri_bins[mask],params_best[0],params_best[1],params_best[2],params_best[3],params_best[4],params_best[5],params_best[6]), yerr = np.sqrt(n[mask]), fmt = 'o', color='green')
ax[1].axhline(y=0, color= 'red', linestyle='--')

ax[2].errorbar(centri_bins[mask],(n[mask]-fg2(centri_bins[mask],params_best[0],params_best[1],params_best[2],params_best[3],params_best[4],params_best[5],params_best[6]))/np.sqrt(n[mask]), yerr= np.sqrt(n[mask]), color='green')
ax[2].axhline(y=0, color= 'red', linestyle='--')
plt.show()

# rifaccio il chi quadro
scarti = (n[mask]- fg2(centri_bins[mask],params_best[0],params_best[1],params_best[2],params_best[3],params_best[4],params_best[5],params_best[6]))**2 / n[mask]
new_chi = np.sum(scarti)
new_red = new_chi/(n[mask].size - 6)
print('il nuovo chi quadro è ', new_chi)
print('il nuovo chi quadro ridotto è ',new_red)
