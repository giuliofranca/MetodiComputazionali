import numpy as np
import mycamera
import ctypes
import matplotlib.pyplot as plt

buffer = ctypes.create_string_buffer(1536 * 1024 * 2)
risultato = mycamera.read_camera(buffer)

print(risultato)

# creo immagine creando matrice 2D
img = np.frombuffer(risultato, dtype='<u2')
img = img.reshape((1024, 1536), order = 'C')
img = np.flipud(img)


plt.imshow(img, cmap="gray")
plt.colorbar()
plt.title("Immagine")
plt.show()
