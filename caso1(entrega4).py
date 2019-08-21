from matplotlib.pylab import *
import numpy as np
 
 
a = 1.          #Ancho del dominio
b = 1.          #Largo del dominio
Nx = 50         #Numero de intervalos en x
Ny = 50         #Numero de intervalos en Y
 
dx = b / Nx     #Discretizacion espacial en X
dy = a / Ny     #Discretizacion espacial en Y
 
h = dx    # = dy
 
 
if dx != dy:
    print("ERRROR!!!!! dx != dy")
    exit(-1)   #-1 le dice al SO que el programa fallo.....
  
coords = lambda i, j : (dx*i, dy*j)
x, y = coords(4,2) 
 
print "x = ", x
print "y = ", y

#aqui se crea la matriz que es el caso 2D 
u_k = np.zeros((Nx+1,Ny+1), dtype=double)   #dtype es el tipo de datos (double, float, int32, int16...)
u_km1 = np.zeros((Nx+1,Ny+1), dtype=double)   #dtype es el tipo de datos (double, float, int32, int16...)

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

#Loop en el tiempo
u_k[:,:] = 20 #condicion de la matriz, todos los valores son 20 grados
for k in range(int32(5./dt)):
    t = 1000*dt*(k+1)
    print "k = ", k, " t = ", t
 
    #CB esencial, dando la condicion del abmiente sobre el hormigon
    u_k[:,Nx] = u_ambiente(t,T)
 
    #Loop en el espacio   i = 1 ... n-1   u_km1[0] = 0  u_km1[n] = 20
    for i in range(1,Nx):
        for j in range(1,Ny):
            #Algoritmo de diferencias finitas 2-D para difusion
 
            #Laplaciano, haciendo que el calor se vaya distribuyendo 
            nabla_u_k = (u_k[i-1,j] + u_k[i+1,j] + u_k[i,j-1] + u_k[i,j+1] - 4*u_k[i,j])/h**2
 
            #Forward euler, calculando ki+1
            u_km1[i,j] = u_k[i,j] + alpha*nabla_u_k
 
    #CB natural
    u_km1[Nx,:] = u_km1[Nx-1,:]
    u_km1[:,Ny] = u_km1[:,Ny-1]
 
    #Avanzar la solucion a k + 1
    u_k = u_km1
 
    #CB esencial una ultima vez, con estas definimos que la matriz se mantenga de un paso a otro de modo con los bordes constante de modo que solo varia la parte superior, sin esto la matriz distribuye tanto horizontal como vertical desde los bordes izq e inferior
    u_k[0,:] = u_k[1,:]
    u_k[:,0] = u_k[:,1] 
    u_k[Nx,:] = u_k[Nx-1,:]
    u_k[:,Nx] = u_ambiente(t,T)
    
    
 
    print "Tmax = ", u_k.max()
 
    if t > next_t:
        figure(1)
        imshowbien(u_k)
        title("k = {0:4.0f}   t = {1:05.2f} s".format(k, t))
        savefig("movie/frame_{0:10.0f}.png".format(framenum))
        framenum += 1
        next_t += dnext_t
        close(1)
 
 
 
show()
