Introducción 
============

Como segunda parte del proyecto se modeló el comportamiento de un muro de hormigón, de "a" metros de alto y "b" metros de largo, cuando es sometida a temperatura ambiente "T", con el fin de estudiar cómo se disipa el calor en ella. Para esto se definen dos casos, cada uno de ellos con diferentes condiciones de borde, el primero tres de sus msantienen contemperatura constante en el tiempo, mientras que en el segundo la temperatura en los bordes puede variar, pero el gradiente de esta es cero.

Caso I
======
Condiciones de Borde:

- u(0,y,t) = 20
- u(x,0,t) = 20
- u(b,y,t) = 20

La temperatura en todos los bordes, a excepción del borde superior (en contacto con el ambiente), se mentiene igual a 20°C en todo momento

Condiciones Iniciales:
- u(x,y,0) = 20 

En t = 0 todo el muro se encontraba a 20°C

Parámetros:

- a = 1 m. (alto del muro)
- b = 1 m. (largo del muro)
- Nx = Ny = 50 (número de intervalos en x; y)
- dt = i min. (variación del tiempo)
- c = 450 J/kg°C (calor específico)
- rho = 7800 kg/m^3 (densidad)
- K = 79.5 m^2/s

Resultados
==========

Caso II
=======
Condiciones de Borde:

- du/dx (0,y,t) = 0
- du/dy (x,0,t) = 0
- du/dx (b,y,t) = 0

La temperatura en todos los bordes, a excepción del borde superior (en contacto con el ambiente), puede variar en el tiempo a medida que se disipa el calor, pero el gradiente en los extremos del muro se mantiene igual a cero.

Condiciones Iniciales:
- u(x,y,0) = 20 

En t = 0 todo el muro se encontraba a 20°C

Parámetros:

- Iguales al caso I

Resultados
==========
