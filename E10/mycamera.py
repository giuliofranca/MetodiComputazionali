import numpy
import ctypes

# carico la libreria mycamera
_libmycamera = numpy.ctypeslib.load_library('libmycamera', '.')

# definisco tipi di input e output
_libmycamera.read_camera.argtypes = [ctypes.c_char_p]
_libmycamera.read_camera.restype = ctypes.c_int

def read_camera(x):
    out = _libmycamera.read_camera(x)
    return x