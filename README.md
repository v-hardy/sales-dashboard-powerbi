# TP Power BI - Análisis de Ventas

## 📌 Objetivo
Este proyecto corresponde al Trabajo Práctico de **Análisis de Datos**.  
El objetivo es aplicar conocimientos de **Power BI Desktop** para transformar datos crudos, modelar un esquema relacional en estrella y crear un **dashboard interactivo** que facilite la toma de decisiones.

## 🛠️ Requerimientos Técnicos
- Entorno: Power BI Desktop
- Repositorio: Público
- Entregables:
  - Archivo `.pbix` con el informe completo
  - Documento PDF explicando brevemente el proceso ETL y el modelo de datos

## 📂 Estructura del Repositorio

/data → Archivos CSV/Excel utilizados como fuentes 
/pbix → Informe final en Power BI (.pbix) 
/docs → Documento PDF con explicación del ETL y modelado 
README.md

## 🔄 Proceso ETL
- Conexión a **3+ fuentes de datos** (CSV, Excel, Web).
- Transformaciones en Power Query:
  - Renombrado de columnas y tipos de datos
  - Limpieza de valores nulos
  - Creación de columnas calculadas (ej. Importe de línea)
  - Combinación de tablas (merge/anexar)
- Datos listos para modelado relacional.

## 🗂️ Modelado de Datos
- Esquema **estrella** con:
  - Tabla de hechos: `FactSales`
  - Dimensiones: `DimProduct`, `DimCustomer`, `DimDate`, `DimGeo`
- Relaciones 1:M correctamente definidas.
- Tabla calendario creada en DAX y marcada como Date Table.

## 📊 Dashboard
- Visuales incluidos:
  - Tarjeta KPI (Total Ventas)
  - Gráfico de líneas (tendencia temporal)
  - Gráfico de columnas (ventas por categoría/segmento)
  - Mapa (ventas por ciudad/país)
- Segmentadores: Fecha y Categoría/Segmento
- Interactividad asegurada entre todos los visuales.

## ✅ Criterios de Evaluación
- Modelado de datos (30%)
- Transformación ETL (25%)
- Medidas DAX (20%)
- Diseño y visualización (15%)
- Documentación (10%)

## 📸 Capturas
*(Agregar aquí imágenes del dashboard para ilustrar el resultado final)*

---

### Autor
- Nombre: Victor Hardy
- Materia: Análisis de Datos
- Universidad/Instituto: Informatorio Chaco
