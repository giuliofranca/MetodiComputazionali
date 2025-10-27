import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

dati = pd.read_csv('kplr010666592-2011240104155_slc.csv')
print(dati.columns)

#produco un grafico del flusso in funzione del tempo
tempo = dati['TIME']
flusso = dati['PDCSAP_FLUX']
errore = dati['PDCSAP_FLUX_ERR']
plt.errorbar(tempo, flusso, yerr =errore, fmt='o', color = 'green', label = 'flusso')
plt.xlabel('tempo (BJD)')
plt.ylabel('flusso (e-/s)')
plt.legend()
plt.show()


dati_locali = dati.loc[(dati['TIME']>947.9) & (dati['TIME']<948.4)]
plt.errorbar(dati_locali['TIME'],dati_locali['PDCSAP_FLUX'], yerr=dati_locali['PDCSAP_FLUX_ERR'], fmt='o', color='blue')
plt.xlabel('tempo (BJD)')
plt.ylabel('flusso (e-/s)')
plt.show()

#creo grafico con inset che mostra zoom su minimo del flusso
fig, ax = plt.subplots(figsize=(12,6))
plt.errorbar(tempo,flusso,yerr= errore,fmt= 'o', color='red')
riquadro = inset_axes(ax, width='20%', height='20%', loc='upper right')
riquadro.errorbar(dati_locali['TIME'], dati_locali['PDCSAP_FLUX'], fmt='o', color='blue')
plt.show()

             
