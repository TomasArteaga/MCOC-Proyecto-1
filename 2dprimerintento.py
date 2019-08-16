"Proyecto 1, Métodos computacionales"
"caso 8"


#difusión i-d
#omega va desde cero a l=1,0
#definido como ecuacion diferecnial 
from matplotlib.pylab import *


##genera overflow con dx, dy = 100, con 6 funciona perfecto###
a = 1.0  #ancho del dominio
b = 1.   #largo del dominio 
Nx = 100   #subdivisiones elemento
Ny = 100
dx = b/Nx   #discretizacion espacial en x 
dy = a/Ny #discretizacion espacial en y 
h = dx # = dy

if dx != dy: #supuesto por si llego a cambiar el dx vs el dy
    print "errore dx!= dy"
    exit(-1) #el -1 dice que termina con error
#funcion de convivencia para calcular coordenadas del punto (i,j)
#def coords(i,j):
 #   return (dx*i,dy*j)


#i, j = 4, 2
#x , y = dx*i, dy*j 

###PARA QUE ES ESTO?###
coords = lambda i, j : (dx*i, dy*j)
x, y = coords(4,2) #tupla definir dos variables en una linea, oh baia


print "x = ", x
print "y = ", y

u_k = zeros((Nx+1, Ny+1), dtype = float64) #dtype es el tipo de datos (double, float, int32)
u_km1 = zeros((Nx+1, Ny+1), dtype = float64)

#CB esencial
u_k[0, :] = 20.
u_k[:, 0] = 20.

#buena idea definir funciones que hagan el codigo expresivo

#funciones para dejar la matriz como la de clases, primera fila y columna con temp = 20, condiciones de borde = CB##
def printbien(u):
    print u_k.T[Nx::-1,:] #lo arrelga

#esto imprime el grafico 2d a colores
def imshowbien(u):
    imshow(u_k.T[Nx::-1,:])

#print u_k imprime el eje y invertdio
printbien(u_k)
###imshowbien(u_k)

k = 0
alpha = K*dt/(c*rho*dx**2)
figure(1)
imshowbien(u_k)
colorbar()
title("K = {}  t = {} s".format(k, k*dt))

#vector con todos los punto en el espacio dentro del elemento (x)
#x = linspace(0, L, n + 1)

#exit(0) ejecucion llega hasta aqui

#parametros del problema, casos del hormigon 
dt=0.001 #indica cuanto cambia el tiempo 
K=5.5
c=900.0
rho=2400.0 # se usa densidad de hormigón 
alpha = K*dt/(c*rho*dx**2)


#informar cosas interesantes
####print 'dt=', dt
####print 'dx=', dx
####print 'K=', K
####print 'c=', c
####print 'rho=', rho
print 'alpha=', alpha


#euler esta dejando la patá cuidado con el overflow, quizas achicar el dt, dy = 0.1
#plot(x,u0,"k--")
#exit(0) #dice que termina bien el programirijillo

#loop en el tiempo 

for k in range(1000):
    t=dt*(k+1)
    #Definicion de las condiciones de bordes
    u_k[0,:]=20
    u_k[:,0]=20
    #Loop en el espacio
    for i in range(1,Nx-1):
        for j in range(1,Ny-1):
            #laplaciano, aqui es donde queda la crema, posiblemente los 4 primeros valores son muy parecidos al 4*... asi que da algo muy chico y el h es muy chico tmb
            nabla_u_k = (u_k[i-1,j] + u_k[i+1,j] + u_k[i,j+1] + u_k[i,j-1] - 4*u_k[i,j])/h**2
            #forward euler, sigue la crema del nabla 
            u_km1[i,j]= u_k[i,j] + Alpha*nabla_u_k
    u_km1[Nx,:] = u_km1[Nx-1,:]
    u_km1[:,Ny] = u_km1[:,Ny-1]
    #Avanza al tiempo k+1
    u_k = u_km1
    #esto imprime graficos cada 100 valores de k, lo pueden editar segun cuan especificos quieran los graficos
    if k %100 == 0 :
        figure()
        imshowbien(u_k)
        colorbar()
        title('k={} t={} s'.format(k, k*dt))

#CB una ultima vez  
u_k[0,:]=20
u_k[:,0]=20

figure(2)         
imshowbien(u_k)
title("k = {}  t = {} s".format(k, k*dt))
colorbar()

#esto es para guardar los graficos cada 0.04 segundos y hacer una pelicula de como va cambiando el grafico, blablA
#savefig("movie/frame_{0:04.of}".format(k)) #cambiar dependiendo del tiempo
#close("all")

