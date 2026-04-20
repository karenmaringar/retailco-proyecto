# 📊 Reporte EDA — RetailCo

## 🔍 Problemas de calidad encontrados

### Problema 1 — Date con tipo incorrecto
- **Columna:** Date
- **Problema:** Está guardada como texto (str)
- **Impacto:** No se pueden hacer cálculos por 
  mes, trimestre o año sin convertirla primero

### Problema 2 — fulfilled-by con 69.55% nulos
- **Columna:** fulfilled-by
- **Problema:** 7 de cada 10 filas están vacías
- **Impacto:** No se puede analizar el método 
  de cumplimiento de los pedidos

### Problema 3 — Unnamed: 22 columna basura
- **Columna:** Unnamed: 22
- **Problema:** Columna sin nombre ni datos útiles
- **Impacto:** Contamina el dataset y ocupa memoria

### Problema 4 — ship-postal-code es float
- **Columna:** ship-postal-code
- **Problema:** Guardada como número decimal
- **Impacto:** Pierde ceros iniciales y agrega 
  decimales innecesarios ej: 01001 → 1001.0

### Problema 5 — Qty y Amount con valores en 0
- **Columnas:** Qty, Amount
- **Problema:** Existen ventas con valor 0
- **Impacto:** Distorsiona promedios y totales

### Problema 6 — Amount con 7,795 nulos
- **Columna:** Amount
- **Problema:** 6.04% de filas sin monto
- **Impacto:** El total de ventas real 
  podría ser mayor

## ❓ Columnas con tipo de dato incorrecto

| Columna | Tipo actual | Tipo correcto | ¿Por qué es crítico? |
|---|---|---|---|
| Date | str | datetime | Sin esto no hay análisis temporal |
| ship-postal-code | float | str | Pierde ceros iniciales |

## 📊 Estadísticas descriptivas

| Métrica | Qty | Amount |
|---|---|---|
| Total registros | 128,975 | 121,180 |
| Promedio | 0.90 | 648.56 |
| Mínimo | 0 | 0 |
| Máximo | 15 | 5,584 |