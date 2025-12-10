import pandas as pd

# ============================
# Cargar catálogo existente
# ============================
catalogo_path = "data/catalogo_productos_electronicos.csv"
df = pd.read_csv(catalogo_path)

# ============================
# Definir márgenes estándar por categoría
# ============================
margenes_estandar = {
    "Smartphones": 0.28,
    "Notebooks": 0.25,
    "Tablets": 0.30,
    "Auriculares": 0.35,
    "Smartwatches": 0.32,
    "Televisores": 0.22,
    "Parlantes Bluetooth": 0.35,
    "Cargadores": 0.40,
    "Consolas": 0.18,
    "Accesorios Gaming": 0.33
}

# ============================
# Calcular el costo estándar
# ============================
costos = []

for _, row in df.iterrows():
    product_id = row["ProductID"]
    categoria = row["Category"]
    price = row["Price"]       # ahora ya no existe Price_ARS

    margen_std = margenes_estandar.get(categoria, 0.30)
    costo_std = round(price * (1 - margen_std), 2)

    costos.append({
        "ProductID": product_id,
        "Category": categoria,
        "Price": price,
        "Margen_Estandar": margen_std,
        "Costo_Estandar": costo_std
    })

df_costos = pd.DataFrame(costos)

# ============================
# Guardar CSV final
# ============================
output_path = "data/costos_estandar_productos.csv"
df_costos.to_csv(output_path, index=False)

print(f"Archivo generado: {output_path}")
print(df_costos.head(10))

