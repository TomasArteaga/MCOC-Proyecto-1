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

![frame_        16](https://user-images.githubusercontent.com/53712876/63398959-27693980-c39d-11e9-91de-21cb8bd1d0bb.png)
![frame_        75](https://user-images.githubusercontent.com/53712876/63399022-364fec00-c39d-11e9-8538-482ab55f4e28.png)
![frame_       127](https://user-images.githubusercontent.com/53712876/63399038-3fd95400-c39d-11e9-8761-54fa85f15532.png)
![frame_       156](https://user-images.githubusercontent.com/53712876/63399049-44057180-c39d-11e9-9182-2826b4bbb1f4.png)
![frame_       207](https://user-images.githubusercontent.com/53712876/63399054-4962bc00-c39d-11e9-86f1-604c84d8b90d.png)
![frame_       465](https://user-images.githubusercontent.com/53712876/63399066-5a133200-c39d-11e9-86b1-6eaba5ee12a3.png)


De los resultados obtenidos se puede apreciar que el cambio de temperatura en el hormigón es cíclica, además, al tener los bordes temperatura constante (por condiciones de borde), la temperatura tiende a disiparse hacia al centro.

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

![frame_         0](https://user-images.githubusercontent.com/53712876/63398488-cc831280-c39b-11e9-89c8-f7e1a2a47255.png)
![frame_        15](https://user-images.githubusercontent.com/53712876/63398508-dad12e80-c39b-11e9-9077-205c6f1d2c9c.png)
![frame_        41](https://user-images.githubusercontent.com/53712876/63398519-e6245a00-c39b-11e9-982b-fc17c3e51e83.png)
![frame_        90](https://user-images.githubusercontent.com/53712876/63398527-efadc200-c39b-11e9-9242-7fa799f51106.png)
![frame_       105](https://user-images.githubusercontent.com/53712876/63398534-f4727600-c39b-11e9-804b-dc29fed0f290.png)
![frame_       121](https://user-images.githubusercontent.com/53712876/63398546-fb998400-c39b-11e9-9959-a6e52c994ec1.png)
![frame_       139](https://user-images.githubusercontent.com/53712876/63398557-ffc5a180-c39b-11e9-8114-54e86a5e69d4.png)
![frame_       225](https://user-images.githubusercontent.com/53712876/63398569-06ecaf80-c39c-11e9-951c-78d9cd65bad0.png)

Dados los resultados, podemos ver que la temperatura se disipa a lo largo del eje y, manteniendo su valor constante en x, esto se debe a que las condiciones de borde permiten el cambio de temperatura entre el muro y el exterior.

Recursos
==========

https://www.dropbox.com/s/9ugea32ulu186oi/2019%2C%20Methodology%20Comparison%20for%20Concrete%20Adiabatic%20Temperature%20Rise%20%28Riding%20et%20al.%29.pdf?dl=0

