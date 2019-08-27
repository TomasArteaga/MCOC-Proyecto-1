 #-*- coding: utf-8 -*-
"""
Created on Fri Aug 23 18:43:46 2019
@author: fredd
"""
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 15:33:19 2019
@author: fredd
"""

from matplotlib.pylab import *
from matplotlib import pyplot
import numpy as np
from scipy.interpolate import lagrange

 
a = 1.         #Ancho del dominio
b = 1.          #Largo del dominio
c = 1.          # Alto del dominio
Nx = 50        #Numero de intervalos en x
Ny = 50         #Numero de intervalos en Y
Nz = 50         #Numero de intervalos en Z
 
dx = b / Nx     #Discretizacion espacial en X
dy = a / Ny     #Discretizacion espacial en Y
dz = c / Nz     #Discretizacion espacial en Z
 
h = dx    # = dy

 
 
if dx != dy:
    print("ERRROR!!!!! dx != dy")
    exit(-1)   #-1 le dice al SO que el programa fallo.....
  
coords = lambda i, j, k : (dx*i, dy*j, dz*k)
x, y, k = coords(4,2,2) 
 
print "x = ", x
print "y = ", y


#aqui se crea la matriz que es el caso 2D 
u_k = np.zeros((Nx+1,Ny+1,Nz+1), dtype=double)   #dtype es el tipo de datos (double, float, int32, int16...)
u_km1 = np.zeros((Nx+1,Ny+1,Nz+1), dtype=double)   #dtype es el tipo de datos (double, float, int32, int16...)

#tiempo para el seno 
T = 2000.

#funcion para definir el extremo libre del hormigon en contacto con el ambiente a traves de la funcion seno
def u_ambiente(t,T):
    return 20 + 10*sin((2*np.pi/T)*t)

   
#traspone la matriz para que sea vea con sentido a lo visto en clases 
def printbien(u):
    print u.T[Nx::-1,:]
 
printbien(u_k)

#grafico de colores para entender el movmiento de calor en la cara del hormigon 
def imshowbien(u):
    imshow(u.T[Nx::-1,:])
    colorbar(extend='both',cmap='plasma')
    clim(10, 30)
 
#Parametros del problema (hormigon)
dt = 60.0       # s
K = 10.5       # m^2 / s   
c = 1000.       # J / kg C
rho = 2400.    # kg / m^3
alpha = K*dt/(c*rho*dx**2)

#calculo para evitar overflow 
alpha_bueno = 0.0001
dt = alpha_bueno*(c*rho*dx**2)/K
alpha = K*dt/(c*rho*dx**2)
 
 
#Informar cosas interesantes
print "dt = ", dt
print "dx = ", dx
print "K = ", K
print "c = ", c
print "rho = ", rho
print "alpha = ", alpha
 
k = 0
 
dnext_t = 0.05   #  20.00
next_t = 0.
framenum = 0
Temp1 = []
Tiempo1 = []

Temp2 = []
Tiempo2 = []

Temp3 = []
Tiempo3 = []

Temp4 = []
Tiempo4 = []

Temp5 = []
Tiempo5 = []

Temp6 = []
Tiempo6 = []

Temp7 = []
Tiempo7 = []

Temp8 = []
Tiempo8 = []

Temp9 = []
Tiempo9 = []



#Loop en el tiempo
u_k[:,:] = 20 #condicion de la matriz, todos los valores son 20 grados
for k in range(int32(5./dt)):
    t = 1000*dt*(k+1)
    print "k = ", k, " t = ", t
 
    #CB esencial, dando la condicion del abmiente sobre el hormigon
    u_k[:,Nx] = u_ambiente(t,T)
    if k % 20 == 0:
        Temp1.append(u_km1[25, 46, 46])
        Tiempo1.append(t)
        
        Temp2.append(u_km1[25, 46, 25])
        Tiempo2.append(t)
        
        Temp3.append(u_km1[25, 46, 4])
        Tiempo3.append(t)
        
        Temp4.append(u_km1[25, 25, 46])
        Tiempo4.append(t)
        
        Temp5.append(u_km1[25, 25, 25])
        Tiempo5.append(t)
        
        Temp6.append(u_km1[25, 25, 4])
        Tiempo6.append(t)
        
        Temp7.append(u_km1[46, 46, 46])
        Tiempo7.append(t)
        
        Temp8.append(u_km1[46, 46, 25])
        Tiempo8.append(t)
        
        Temp9.append(u_km1[46, 46, 4])
        Tiempo9.append(t)
       
        
    #Loop en el espacio   i = 1 ... n-1   u_km1[0] = 0  u_km1[n] = 20
    for i in range(1,Nx):
        for j in range(1,Ny):
            for k in range(1,Nz):
            #Algoritmo de diferencias finitas 2-D para difusion
            #Laplaciano, haciendo que el calor se vaya distribuyendo 
                nabla_u_k = (u_k[i-1,j,k] + u_k[i+1,j,k] + u_k[i,j-1,k] + u_k[i,j+1,k]+ u_k[i,j,k-1] + u_k[i,j,k+1] - 6*u_k[i,j,k])/h**2
            #Forward euler, calculando ki+1
                u_km1[i,j,k] = u_k[i,j,k] + alpha*nabla_u_k
    
    #CB natural
    u_km1[Nx,:,:] = u_km1[Nx-1,:,:]
    u_km1[:,Ny,:] = u_km1[:,Ny-1,:]
    u_km1[:,:,Nz] = u_km1[:,:,Nz-1]
 
    #Avanzar la solucion a k + 1
    u_k = u_km1
 
    #CB esencial una ultima vez, con estas definimos que la matriz se mantenga de un paso a otro de modo con los bordes constante de modo que solo varia la parte superior, sin esto la matriz distribuye tanto horizontal como vertical desde los bordes izq e inferior
    u_k[0,:,:] = u_k[1,:,:]
    u_k[:,0,:] = u_k[:,1,:]
    u_k[:,:,0] = u_k[:,:,1] 
    
    u_k[Nx,:,:] = u_k[Nx-1,:,:]
    u_k[:,Nx,:] = u_ambiente(t,T)
    
    
 
    print "Tmax = ", u_k.max()
    

#    if t > next_t:
#       figure(1)
#       imshowbien(u_k)
#       title("k = {0:4.0f}   t = {1:05.2f} s".format(k, t))
#       savefig("movie/frame_{0:10.0f}.png".format(framenum))
#       framenum += 1
#       next_t += dnext_t
#       close(1)
 
#g´raficos tiempo temperatura

print ("Curva Punto 1") 
pyplot.plot(Tiempo1, Temp1)
pyplot.show()

print ("Curva Punto 2") 
pyplot.plot(Tiempo2, Temp2)
pyplot.show()

print ("Curva Punto 3") 
pyplot.plot(Tiempo3, Temp3)
pyplot.show()

print ("Curva Punto 4") 
pyplot.plot(Tiempo4, Temp4)
pyplot.show()

print ("Curva Punto 5") 
pyplot.plot(Tiempo5, Temp5)
pyplot.show()

print ("Curva Punto 6") 
pyplot.plot(Tiempo6, Temp6)
pyplot.show()

print ("Curva Punto 7") 
pyplot.plot(Tiempo7, Temp7)
pyplot.show()

print ("Curva Punto 8") 
pyplot.plot(Tiempo8, Temp8)
pyplot.show()

print ("Curva Punto 9") 
pyplot.plot(Tiempo9, Temp9)
pyplot.show()


#interpolar curva
#crear función
temp1 = lagrange(Tiempo1, Temp1)
temp2 = lagrange(Tiempo2, Temp2)
temp3 = lagrange(Tiempo3, Temp3)
temp4 = lagrange(Tiempo4, Temp4)
temp5 = lagrange(Tiempo5, Temp5)
temp6 = lagrange(Tiempo6, Temp6)
temp7 = lagrange(Tiempo7, Temp7)
temp8 = lagrange(Tiempo8, Temp8)
temp9 = lagrange(Tiempo9, Temp9)


show()

