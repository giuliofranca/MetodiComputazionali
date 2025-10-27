import datetime
from datetime import datetime, timedelta

data_str = input('Inserire la data di nascita nel seguente formato: giorno-mese-anno 00:00:00')
data = datetime.strptime(data_str, "%d-%m-%Y %H:%M:%S")

"""calcolo la differenza temporale"""
datenow = datetime.now()
timediff = datenow - data

"""differenza temporale in secondi"""
diff_secondi = timediff.total_seconds()
print(diff_secondi)

"""differenza temporale in giorni"""
diff_giorni = timediff.total_seconds()/(60*60*24)
print(diff_giorni)

diff_anni = diff_giorni/365
print(diff_anni)
