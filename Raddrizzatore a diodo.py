import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

Vp=5 #ampiezza di tensione
w=314.6 #pulsazione
V_gamma=0.7 #barriera di potenziale del diodo
R_on=5 #resistenza interna del diodo
R=1000 #resistenza filtro
C=47e-6 #capacità filtro
Vin = lambda t: Vp*np.sin(w*t)
"""
Si tratta di un'equazione differenziale con solo una componente
"""

"""
Event detection & location 
"""
def change_voltage(t,y,Vin,V_gamma):
    return Vin(t)-y[0]-V_gamma
change_voltage.terminal = False #non interrompere il calcolo
change_voltage.direction=-1


def funzione(t,y,Vin,V_gamma):
    f=np.zeros(1)
    [Vc]=y
    if Vin(t)>(Vc+V_gamma):
        f[0]=(Vin(t)-V_gamma-Vc)/(R_on*C)
    elif Vin(t)<(Vc+V_gamma):
        f[0]=-Vc/(R*C)
    return f
y_0=[0]
tf=0.5
sol=solve_ivp(funzione,[0,tf],y_0,events=change_voltage,args=(Vin,V_gamma),t_eval=np.arange(0,tf,0.001))

plt.figure()
plt.plot(sol.t,sol.y[0])
plt.show()

print("Il diodo si è spento ai seguenti tempi: ", sol.t_events[0])