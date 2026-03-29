import numpy as np
import matplotlib.pyplot as plt 
from scipy.integrate import solve_ivp

alpha=1.1
beta=0.4
gamma=0.1
delta=0.4

def lotka_volterra(t,y,alpha,beta,gamma,delta):
    f=np.zeros(2)
    [x_LV,y_LV]=y
    f[0]=alpha*x_LV-beta*x_LV*y_LV
    f[1]=delta*x_LV*y_LV-gamma*y_LV
    return f
y_0=np.array([1.0,1.0])
tf=50
sol=solve_ivp(lotka_volterra,[0,tf],y_0,args=(alpha,beta,gamma,delta),t_eval=np.arange(0,tf,0.1))
plt.figure()
plt.plot(sol.t,sol.y[0],c="red") #plot di x (prede)
plt.plot(sol.t,sol.y[1],c="blue") #plot di y (predatori)
plt.grid(True)
plt.title("Plot con il numero di prede e predatori nel tempo")
plt.xlabel("Tempo")
plt.ylabel("Numero di prede/predatori")
plt.show()
"""
Il picco dei predatori si ha solo dopo il picco delle prede perché questi si 
riproducono solo quando le risorse sono abbondanti. Le prede crescono subito 
dopo il punto di minimo dei predatori perché non vengono sterminate.
"""