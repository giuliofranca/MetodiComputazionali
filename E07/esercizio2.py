import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

lunghezza = 0.5
w0 = 0
theta0 = np.pi/4
condizioni_iniziali = np.array([w0,theta0])
def drdt(r,t,l):
    dxdt = r[1]
    dydt = -(9.81/l) * np.sin(r[0])
    drdt = [dxdt,dydt]
    return drdt

tempi = np.linspace(0,10,1000)
r_soluzioni = integrate.odeint(drdt,condizioni_iniziali, tempi,args=(lunghezza,))
angoli = r_soluzioni[:,1]
angoli_gradi = angoli*360/(2*np.pi)
plt.plot(tempi,angoli_gradi, color='royalblue', label='Angolo in funzione del tempo')
plt.xlabel('t(s)')
plt.ylabel('angoli(gradi)')
plt.grid(True)
plt.legend(loc='upper right')
plt.show()

fig, ax = plt.subplots(1,2,figsize=(12,6))
ciniz1 = np.array([w0,np.pi/4])
r_soluzioni = integrate.odeint(drdt,ciniz1, tempi,args=(1,))
ax[0].plot(tempi,(r_soluzioni[:,1]*360/(2 * np.pi)), color='red')
ax[0].set_label('t(s)')
ax[0].set_ylabel('angolo(gradi)')
ax[0].grid(True)
ax[0].set_title('Condizioni iniziali 1')

ciniz2 = np.array([w0,np.pi/6])
r_soluzioni = integrate.odeint(drdt,ciniz2, tempi,args=(0.5,))
ax[1].plot(tempi,(r_soluzioni[:,1]*360/(2 * np.pi)), color='blue')
ax[1].set_xlabel('t(s)')
ax[1].set_ylabel('angolo(gradi)')
ax[1].grid(True)
ax[1].set_title('Condizioni iniziali 2')

plt.show()