import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import simpson


I = 1
R = 1
u0 = 4 * np.pi * 1e-7
gamma = np.linspace(0, 2 * np.pi, 10)
dl = 1

def calcolo_campo_magn(x, y, z):
    dBx = np.array([])
    dBy = np.array([])
    dBz = np.array([])
    P0 = np.array([x, y, z])

    for i in range(len(gamma)):
        dl_vett = np.array([dl * np.sin(gamma[i]), -dl * np.cos(gamma[i]), 0])
        P1 = np.array([R * np.cos(gamma[i]), R * np.sin(gamma[i]), 0])

        r = P0 - P1
        norm_r = np.linalg.norm(r)

        if norm_r == 0:
            ur = np.array([0, 0, 0])
        else:
            ur = r / norm_r


        dB = (u0 * I) / (4 * np.pi) * (np.cross(dl_vett, ur) / (norm_r**2))

        dBx = np.append(dBx, dB[0])
        dBy = np.append(dBy, dB[1])
        dBz = np.append(dBz, dB[2])

    Bx = simpson(dBx, x=gamma)
    By = simpson(dBy, x=gamma)
    Bz = simpson(dBz, x=gamma)

    return Bx, By, Bz


x = np.linspace(-5, 5, 30)
y = np.linspace(-5, 5, 30)
X, Y = np.meshgrid(x, y)

arr1 = np.zeros(X.shape)
arr2 = np.zeros(Y.shape)
#plot nel piano XZ
for i in range(X.shape[0]):
    for j in range(X.shape[1]):
        Bx, By, Bz = calcolo_campo_magn(X[i, j], 0, Y[i, j])
        arr1[i, j] = Bx
        arr2[i, j] = Bz

U = arr1
V = arr2


print(U.shape)
print(V.shape)
print(X.shape)
print(Y.shape)

fig, ax = plt.subplots(figsize=(7, 7))
strm = ax.streamplot(X, Y, U, V, color=U, linewidth=2, cmap="autumn")
plt.show()

