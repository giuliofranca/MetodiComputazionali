import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

# definizione costanti
m = 0.2
k = 2
C = 0.5
# condizioni iniziali
x0 = 0
v0 = 0
condiz_iniziali = np.array([x0,v0])

# definisco la funzione delle derivate
def drdt(r,t,m,k,C,F,wf):
    dxdt = r[1]
    dydt = -2*(C/(2*m))*r[1] - (k/m)*r[0] + (F(t,wf)/(m))
    drdt = [dxdt,dydt]
    return drdt

# definisco la funzione da passare come argomento
def f(t,wf):
    return 2*np.sin(wf*t)

# risolvo eq differenziale
tempo = np.linspace(0,10,2000)
wf0 = 2
r_soluzioni = integrate.odeint(drdt,condiz_iniziali,tempo,args=(m,k,C,f,wf0))
print (r_soluzioni)

# grafico F(t), x(t) e v(t)
plt.plot(tempo, f(tempo,wf0), label='F(N)')
plt.xlabel('tempo (s)')
plt.ylabel('forza (N)')
plt.title('Forza in funzione del tempo')
plt.grid(True)

plt.plot(tempo, r_soluzioni, label=('v(t)', 'x(t)'))
plt.xlabel('tempo(s)')
plt.title('Risoluzione eq differenziale')
plt.grid(True)
plt.legend()
plt.show()

array_wf = np.linspace(0.1,10,100)
massimi = []
for i in range(len(array_wf)):
    r_soluzioni = integrate.odeint(drdt,condiz_iniziali,tempo,args=(m,k,C,f,array_wf[i]))
    x = r_soluzioni[:,1]
    massimo = np.max(x)
    massimi.append(massimo)

plt.plot(array_wf, massimi, color='limegreen')
plt.xlabel('wf(Hz)')
plt.ylabel('Amax(m)')
plt.title('Massimi in funzione delle frequenze')
plt.show()