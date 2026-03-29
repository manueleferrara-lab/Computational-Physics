import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

sigma=10.0
rho=28.0
beta=8/3
def attrattore_Lorentz(t,y,sigma,rho,beta):
    f=np.zeros(3)
    [x_L,y_L,z_L]=y
    f[0]=sigma*(y_L-x_L)
    f[1]=x_L*(rho-z_L)-y_L
    f[2]=x_L*y_L-beta*z_L
    return f
y_0=np.array([1.0,1.0,1.0])
tf=50

sol1=solve_ivp(attrattore_Lorentz,[0,tf],y_0,args=(sigma,rho,beta),t_eval=np.arange(0,tf,0.01))

#Provo che al variare delle condizioni iniziali le soluzioni divergono 

y_0 += 0.01
sol2=solve_ivp(attrattore_Lorentz,[0,tf],y_0,args=(sigma,rho,beta),t_eval=np.arange(0,tf,0.01))
diff=sol2.y-sol1.y
for i in range(3):
    plt.figure()
    plt.plot(sol1.t,diff[i])
    plt.grid(True)
    plt.title("Divergenza delle soluzioni")
    plt.xlabel("Tempo")
    plt.ylabel("Soluzione")
plt.show()

#Plot 3D
fig1=plt.figure()
ax=fig1.add_subplot(111,projection="3d")
ax.plot(sol1.y[0],sol1.y[1],sol1.y[2],c="red")
plt.title("Soluzione nello spazio")
plt.show()

fig2=plt.figure()
ax=fig2.add_subplot(111,projection="3d")
ax.plot(diff[0],diff[1],diff[2],c="red")
plt.title("Divergenza delle soluzioni")
plt.show()

"""
Osservare che inizialmente le traiettorie non divergono, dunque bisogna
attendere un certo tempo prima di notare variazioni sostanziali tra le 
soluzioni. Ciò è previsto dalla teoria del caos: la minima variazione 
delle condizioni iniziali conduce a comportamenti molto diversi delle
soluzioni.
"""