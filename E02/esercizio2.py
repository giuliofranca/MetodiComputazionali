""" chiedere all'utente un numero intero e fare la somma dei primi n numeri"""
n = input('Inserire un numero intero ')
#devo convertire in intero, di base l'input è una stringa
nn = int(n)
somma = 0
for i in range(nn+1):
    somma = somma + i
print('la somma dei primi ', nn, ' numeri naturali è ', somma)
