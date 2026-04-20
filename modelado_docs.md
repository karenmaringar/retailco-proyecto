Se eligió el esquema estrella porque:

1. Organización clara — separa las métricas (fact_ventas) 
   del contexto (dimensiones), evitando duplicación de datos.

2. Rendimiento — las consultas analíticas son más rápidas 
   porque cada dimensión es pequeña y enfocada.

3. Simplicidad — a diferencia del esquema copo de nieve, 
   las dimensiones no están normalizadas en subtablas, 
   lo que hace las consultas más simples de escribir.

4. Tabla plana vs estrella — una tabla plana repite 
   información como el nombre del producto en cada fila 
   de venta. El esquema estrella lo guarda una sola vez 
   en dim_producto.
❓ Pregunta 2
¿Qué diferencia hay entre una base OLTP y una base OLAP, y por qué RetailCo necesita ambas?

Te doy una pista con un ejemplo de la vida real:

Cuando un cliente hace un pedido en la tienda → eso se guarda en tiempo real → eso es OLTP
Cuando el gerente quiere ver cuánto vendió en todo el año → eso es un análisis → eso es OLAP
¿Con esa pista puedes explicar la diferencia con tus palabras? 😊



OLTP (Online Transaction Processing):
- Diseñada para operaciones en tiempo real
- Registra cada pedido, pago y actualización 
  al instante
- Muchas escrituras simultáneas
- Ejemplo en RetailCo: cuando un cliente 
  hace un pedido, se guarda inmediatamente

OLAP (Online Analytical Processing):
- Diseñada para análisis y toma de decisiones
- Consultas sobre grandes volúmenes de datos
- Pocas escrituras, muchas lecturas
- Ejemplo en RetailCo: el gerente analiza 
  las ventas del último trimestre

¿Por qué RetailCo necesita ambas?
- OLTP para operar el negocio día a día
- OLAP para entender el negocio y tomar 
  decisiones estratégicas

  Columnas excluidas del modelo y sus razones:

1. promotion-ids — contiene texto muy largo y poco 
   estructurado, no aporta valor analítico directo.
   Se podría modelar en una dimensión aparte en 
   una versión más avanzada.

2. currency — todos los registros tienen la misma 
   moneda (INR), no aporta variación analítica.

3. Unnamed: 22 — columna vacía sin información, 
   producto de un error en el archivo original.

4. fulfilled-by y Fulfilment — son redundantes 
   entre sí y no se necesitan para las métricas 
   principales de ventas