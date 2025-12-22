import numpy
import ctypes

#importo la libreria
_libserie = numpy.ctypeslib.load_library('libserie', '.')

#definisco tipi di input e output per la funzione che calcola la serie di fibonacci
_libserie.fibonacci.argtypes = [ctypes.c_int]
_libserie.fibonacci.restype  = ctypes.c_double

#utilizzo di libserie
def serie_fibonacci(n):
    return _libserie.fibonacci(int(n))
