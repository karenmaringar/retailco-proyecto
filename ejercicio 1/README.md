# 📊 RetailCo — Proyecto de Analítica de Datos

## 📋 Descripción
Proyecto de analítica de datos para RetailCo, una tienda 
de comercio electrónico. Incluye el flujo completo desde 
el modelado del Data Warehouse hasta la visualización ejecutiva.

## 👩‍💻 Autora
Karen — Analista de Datos Jr.

## 📦 Dataset
- **Fuente:** Kaggle — E-Commerce Sales Dataset
- **Tamaño:** 128.975 filas, 31 columnas
- **Archivo principal:** Amazon Sale Report.csv

## 📁 Estructura del proyecto
retailco_proyecto/
├── schema.sql          # Script SQL con el esquema estrella
├── star_schema.png     # Diagrama visual del esquema
├── modelado_docs.md    # Documentación del modelado
├── exploracion.ipynb   # Notebook de exploración del dataset
└── README.md           # Este archivo

## 🗄️ Ejercicio 1 — Modelado OLAP
Diseño del esquema estrella en PostgreSQL con:
- `fact_ventas` — tabla de hechos
- `dim_producto` — dimensión de productos
- `dim_cliente` — dimensión de clientes
- `dim_envio` — dimensión de envíos
- `dim_tiempo` — dimensión de tiempo

## 🛠️ Tecnologías usadas
- Python 3.14
- Pandas
- PostgreSQL
- VS Code

retailco_proyecto/
├── 📄 schema.sql
├── 📄 modelado_docs.md
├── 🖼️ star_schema.png
├── 📓 exploracion.ipynb
└── 📄 README.md