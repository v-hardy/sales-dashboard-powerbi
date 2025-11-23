import pandas as pd
import random
from datetime import datetime, timedelta

# 24 provincias argentinas reales con códigos simples
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

# 2 ventas mínimas por provincia (para que ninguna quede en cero en el mapa)
for prov_id, prov_nombre in provincias_arg:
    for _ in range(2):
        order_date = start_date + timedelta(days=random.randint(0, (end_date-start_date).days))
        product_id = f"P{random.randint(1,30):03d}"
        customer_id = f"C{random.randint(1,1500):04d}"
        quantity = random.randint(1, 15)
        unit_price = round(random.uniform(800, 85000), 2)  # precios más argentinos
        discount = round(random.uniform(0, 0.25), 2)     # hasta 25% de descuento
        rows.append([order_id, order_date.strftime("%Y-%m-%d"), product_id, customer_id,
                     prov_id, prov_nombre, quantity, unit_price, discount]) # prov_nombre se agrega para ensuciar el .CSV
        order_id += 1

# Completar hasta 5000 filas (más ventas en provincias grandes)
while len(rows) < 5000:
    prov_id, prov_nombre = random.choices(
        provincias_arg,
        weights=[25, 20, 3, 4, 4, 18, 5, 6, 3, 3, 3, 2, 10, 5, 5, 5, 5, 4, 4, 2, 12, 4, 2, 8],  # más peso a CABA, BsAs, Córdoba, Santa Fe, Mendoza, etc.
        k=1
    )[0]
    order_date = start_date + timedelta(days=random.randint(0, (end_date-start_date).days))
    product_id = f"P{random.randint(1,30):03d}"
    customer_id = f"C{random.randint(1,1500):04d}"
    quantity = random.randint(1, 15)
    unit_price = round(random.uniform(800, 85000), 2)
    discount = round(random.uniform(0, 0.25), 2) 
    rows.append([order_id, order_date.strftime("%Y-%m-%d"), product_id, customer_id,
                 prov_id, prov_nombre, quantity, unit_price, discount])
    order_id += 1

df = pd.DataFrame(rows, columns=["OrderID","OrderDate","ProductID","CustomerID",
                                 "ProvinceID","Province","Quantity","UnitPrice","Discount"])

df.to_csv("data/registro_de_ventas.csv", index=False)
print("registro_de_ventas.csv generado →", len(df), "filas. ¡Listo para Power BI!")
