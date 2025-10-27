""" creo lista coi giorni della settimana, creo lista col nome die giorni della
settimana per tutto il mese di ottobre 2025"""

settimana = ['lunedi','martedi','mercoledi','giovedi','venerdi','sabato','domenica']
settimanacorta1 = settimana[2:7]
settimanacorta2 = settimana[0:5]
ottobre = settimanacorta1 + settimana*3 + settimanacorta2

"""creo lista vuota per riempirla coi numeri dei giorni"""
giorni = []
for i in range(1,32):
    giorni.append(i)

for n,m in zip(giorni, ottobre):
    print(n,'-->',m)
    
