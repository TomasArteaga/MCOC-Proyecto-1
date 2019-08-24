
Introducción
============
En la siguiente entrega se modela la propagación de temperatura dentro de un cubo de hormigón, este cuenta con todas sus caras aisladas a excepción de la superior, la cual se encuentra en contacto directo con el ambiente. Para analizar cómo se difunde la temperatura se estudian dos casos, cada con el bloque sometido a las mismas condiciones de borde y de tmeperatura ambiente, pero con sensores de calor distribuidos de forma distinta dentro del él.

Cabe mencionar que como condiciones de borde se impone que el gradiente de temperatura (du/dx, du/dy, du/dz) sea igual a cero.

Caso I:
======
Se disponen de 9 sensores distribuidos a lo largo del eje z (altura) del bloque como se muestra en la siguiente imágen 

![48d1a631-e3bc-478e-bec5-410bd30b3e44](https://user-images.githubusercontent.com/53712876/63631736-7dd2b400-c5f9-11e9-8fd5-e8a85d181728.JPG)

Resultados:
===========
Para cada punto, el cambiio de temperatura en el tiempo se ilustra en los siguientes gráficos:


![punto 1, 2, 3](https://user-images.githubusercontent.com/53712876/63631770-ae1a5280-c5f9-11e9-9df9-aa83de78cb52.png)
![puntos 4, 5, 6](https://user-images.githubusercontent.com/53712876/63631771-b1add980-c5f9-11e9-9c03-e84e5c4ff912.png)
![Puntos 7, 8, 9](https://user-images.githubusercontent.com/53712876/63631772-b6728d80-c5f9-11e9-9e0d-f7cf092f6118.png)

Caso II:
========
Se dispone de 13 sensores dispuestos en la mitad del bloque, marcando la mited en x (largo), y (ancho) y z (alto). La siguiente imágen ilustra la distribución de los sensores:
![2f4b5508-63f9-46ff-89f6-1cf79737c139](https://user-images.githubusercontent.com/53712876/63631814-2ed94e80-c5fa-11e9-90f7-5e3e5ba3a084.JPG)

Resultados:
===========
La temperatura en cada instante, evaluada para cada sensor, se muestra en los siguientes gráficos. las condiciones de borde imponen que el gradiente de temperatura en (x, y, z) eje debe ser cero, por lo tanto, la temperatura cambia cíclicamente en dirección z.

- Puntos en X

![puntos en X](https://user-images.githubusercontent.com/53712876/63631899-714f5b00-c5fb-11e9-935f-9f56ec8b3529.png)
- Puntos en Y

![Puntos en y](https://user-images.githubusercontent.com/53712876/63631900-714f5b00-c5fb-11e9-8add-b8d80850d203.png)
- Puntos en z

![Puntos en z](https://user-images.githubusercontent.com/53712876/63631901-71e7f180-c5fb-11e9-909a-e4f01b38bf2f.png)
