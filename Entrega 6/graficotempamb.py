# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 01:45:00 2019

@author: Andrés Vera
"""
import scipy as sp
from matplotlib import pyplot
import matplotlib.pylab as plt
from numpy import *

tempamb = []
archivo = open("datos1.txt")
print archivo
for l in archivo:
    l= l.strip('\n')
    dato=(l.split(';')[0]).split(',')
    arreglo = [dato[0], dato[1], dato[2], dato[3]] #tomo los valores del archivo 
    tempamb.append(arreglo)
    
temp= []
t = []
for k in tempamb:
    temp.append(float(k[3]))
    t.append(float(k[2]))

minutos = []
for m in t:
    n = m*1000
    minutos.append(int(n))
    
#grafico 
plt.figure()
plt.plot(minutos, temp, label="temperatura ambiente") 
plt.xlabel("Tiempo en minutos")
plt.ylabel("Temperatura")
plt.title("Temperatura Ambiente")
plt.savefig("grafico temperatura ambiente.png")
plt.show()