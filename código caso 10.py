"Proyecto 1, Métodos computacionales"
"caso 10"


#difusión i-d
#omega va desde cero a l=1,0
#definido como ecuacion diferecnial 
from matplotlib.pylab import *

L = 1.0   #largo elemento [m]
n = 100   #subdivisiones elemento
dx =L/n   #discretizacion espacial (cuánto mide cada trozo)

#vector con todos los punto en el espacio dentro del elemento (x)
x = linspace(0, L, n + 1)

#condición inicial
def fun_u0(x):
    return  10*exp(-(x-0.5)**2/0.1**2)

u0= fun_u0(x) 
#creear el vecto de solucion u (u es temperatura en cierto momento y lugar)
u_k=u0.copy() #vector de temperatura según el tiempo, se trabaja sobre el vector de temperatura inicial

#condiciones de borde (esenciales)
u_k[0] =0.0 #temperatura al comienso es cero
u_k[n] =20.0 #temperatura en instante final (n) es 20°c

#crear vector para temperatura en tiempo k+1, se trabaja sobre vector de temperatura para momento inicial
u_km1=u_k.copy()

#parámetro del problema 
dt=4 #indica cuanto cambia el tiempo, variación de tiempo mayor
K=5.5
c=900.0
rho=2400.0
alpha = K*dt/(c*rho*dx**2)
print 'dt=', dt
print 'dx=', dx
print 'K=', K
print 'c=', c
print 'rho=', rho
print 'alpha=', alpha

plot(x,u0,"k--")

#loop en el tiempo 
k = 0.0
for k in range(20000):#avanzo 10 pasos, hasta seg 10
    t = dt*k
    print "k=",k, "t=", t, "dt=", dt
    
    u_k[0]= 0
    u_k[n] =20
    #loop en el espacio 1=1...n-1, u_km1[0]=0 y u_km1[n]= 2
    for i in range(1, n):
        #algoritmo de diferencias finitas 1-D para difusion 
        u_km1[i] = u_k[i] + alpha*(u_k[i+1]-2*u_k[i]+u_k[i-1])
    
    #Avanzar la solucion a k+1
    u_k = u_km1
    
    if k%200==0: #filtra lineas 
        plot(x,u_k)


title('k={} t={} s'.format(k, k*dt))

show()



