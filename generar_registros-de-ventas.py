import pandas as pd
import random
from datetime import datetime, timedelta

# ============================
# CARGAR CATÁLOGO REAL (precios de lista)
# ============================
catalogo = pd.read_csv("data/catalogo_productos_electronicos.csv")
# Asegurarnos de que ProductID sea string con formato P001
catalogo['ProductID'] = catalogo['ProductID'].astype(str)

# ============================
# Provincias argentinas (tu código original, lo dejo igual)
# ============================
provincias_arg = [
    (101, "Buenos Aires"), (102, "Ciudad Autónoma de Buenos Aires"),
    (103, "Catamarca"), (104, "Chaco"), (105, "Chubut"), (106, "Córdoba"),
    (107, "Corrientes"), (108, "Entre Ríos"), (109, "Formosa"), (110, "Jujuy"),
    (111, "La Pampa"), (112, "La Rioja"), (113, "Mendoza"), (114, "Misiones"),
    (115, "Neuquén"), (116, "Río Negro"), (117, "Salta"), (118, "San Juan"),
    (119, "San Luis"), (120, "Santa Cruz"), (121, "Santa Fe"),
    (122, "Santiago del Estero"), (123, "Tierra del Fuego"), (124, "Tucumán")
]

rows = []
order_id = 1001
start_date = datetime(2023, 1, 1)
end_date = datetime(2025, 11, 30)

# ============================
# 2 ventas mínimas por provincia
# ============================
for prov_id, prov_nombre in provincias_arg:
    for _ in range(2):
        order_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
        
        # Elegir producto del catálogo real
        producto = catalogo.sample(1).iloc[0]
        product_id = producto['ProductID']
        precio_lista = producto['Price']
        
        customer_id = f"C{random.randint(1,1500):04d}"
        quantity = random.randint(1, 15)
        
        # Descuento realista (0–25%, pero más frecuente bajo)
        discount = round(random.choices([0, 0.05, 0.10, 0.15, 0.20, 0.25], 
                                      weights=[40, 25, 15, 10, 7, 3])[0], 2)
        
        # Precio de venta = precio de lista con descuento aplicado
        unit_price = round(precio_lista * (1 - discount), 2)
        
        rows.append([order_id, order_date.strftime("%Y-%m-%d"), product_id, customer_id,
                     prov_id, prov_nombre, quantity, unit_price, discount])
        order_id += 1

# ============================
# Completar hasta 5000 ventas con distribución realista
# ============================
while len(rows) < 5000:
    prov_id, prov_nombre = random.choices(
        provincias_arg,
        weights=[25, 20, 3, 4, 4, 18, 5, 6, 3, 3, 3, 2, 10, 5, 5, 5, 5, 4, 4, 2, 12, 4, 3, 5],  
    k=1
)[0]
    
    order_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
    
    producto = catalogo.sample(1).iloc[0]
    product_id = producto['ProductID']
    precio_lista = producto['Price']
    
    customer_id = f"C{random.randint(1,1500):04d}"
    quantity = random.randint(1, 15)
    discount = round(random.choices([0, 0.05, 0.10, 0.15, 0.20, 0.25], 
                                  weights=[40, 25, 15, 10, 7, 3])[0], 2)
    
    unit_price = round(precio_lista * (1 - discount), 2)
    
    rows.append([order_id, order_date.strftime("%Y-%m-%d"), product_id, customer_id,
                 prov_id, prov_nombre, quantity, unit_price, discount])
    order_id += 1

# ============================
# Guardar
# ============================
df = pd.DataFrame(rows, columns=["OrderID","OrderDate","ProductID","CustomerID",
                                 "ProvinceID","Province","Quantity","UnitPrice","Discount"])

df.to_csv("data/registro_de_ventas.csv", index=False)
print(f"registro_de_ventas.csv generado → {len(df):,} filas")
print("¡Ahora los precios son coherentes con el catálogo! Ganancia bruta será positiva")