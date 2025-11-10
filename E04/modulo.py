import numpy as np
import sys
sys.path.append('.')
import somme

print('La somma dei primi 5 numeri naturali è ', somme.somma(5))
print('La somma delle prime 5 radici dei numeri naturali è ', somme.somma_rad(5))

print('La somma dei primi 3 numeri naturali elevati al quadrato è ', somme.somma_opzionale(3,2))
