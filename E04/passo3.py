import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
sys.path.append('.')
import reco

#creazione funzione che crea array
def creo_array(nome):
    lista = []
    dati = pd.read_csv(nome)
    for ir, rr in dati.iterrows():
       riga = reco.hit(rr['mod_id'],rr['det_id'],rr['hit_time'])
       lista.append(riga)
    array = np.array(lista)

    return array

array0 = creo_array('hit_times_M0.csv')
array1 = creo_array('hit_times_M1.csv')
array2 = creo_array('hit_times_M2.csv')
array3 = creo_array('hit_times_M3.csv')

array_totale = np.concatenate((array0, array1, array2, array3))

ordinati = np.sort(array_totale)
diff_tempi_ordinate = ordinati.diff().fillna(0)
diff_log = np.log10(diff_tempi_ordinate)
mask = diff_log > 0
n, bins, p = plt.hist(diff_log[mask], bins = 50, color='limegreen')
plt.xlabel('logaritmo differenze temporali')
plt.show()
