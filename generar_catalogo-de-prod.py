import random
import csv
from datetime import datetime

# ============================
# Datos de productos electrónicos
# ============================

categorias = [
    "Smartphones", "Notebooks", "Tablets", "Auriculares", "Smartwatches",
    "Televisores", "Parlantes Bluetooth", "Cargadores", "Consolas", "Accesorios Gaming"
]

marcas_por_categoria = {
    "Smartphones": ["Samsung", "Apple", "Xiaomi", "Motorola", "Huawei", "Google"],
    "Notebooks": ["Lenovo", "HP", "Dell", "Asus", "Acer", "Apple", "MSI"],
    "Tablets": ["Samsung", "Apple", "Lenovo", "Amazon", "Huawei"],
    "Auriculares": ["Sony", "JBL", "Apple", "Bose", "Xiaomi", "Beats", "Sennheiser"],
    "Smartwatches": ["Apple", "Samsung", "Garmin", "Xiaomi", "Huawei", "Fitbit"],
    "Televisores": ["Samsung", "LG", "Sony", "TCL", "Philips", "Hisense"],
    "Parlantes Bluetooth": ["JBL", "Bose", "Sony", "Ultimate Ears", "Marshall", "Xiaomi"],
    "Cargadores": ["Anker", "Belkin", "Samsung", "Apple", "Xiaomi", "Ugreen"],
    "Consolas": ["Sony", "Microsoft", "Nintendo"],
    "Accesorios Gaming": ["Razer", "Logitech", "HyperX", "SteelSeries", "Corsair"]
}

# Modelos base reales (pocos ejemplos por categoría, el script los combina creativamente)
modelos_base = {
    "Smartphones": ["Galaxy S", "iPhone", "Redmi Note", "Moto G", "Pixel", "P", "Mate"],
    "Notebooks": ["ThinkPad", "Pavilion", "XPS", "ROG", "Ideapad", "MacBook", "Legion"],
    "Tablets": ["Galaxy Tab", "iPad", "Tab", "Fire", "MediaPad"],
    "Auriculares": ["WH-", "AirPods", "Flip", "QuietComfort", "Buds", "Beats Studio"],
    "Smartwatches": ["Watch", "Galaxy Watch", "Forerunner", "Amazfit", "Watch GT"],
    "Televisores": ["QLED", "OLED", "Bravia", "NanoCell", "4K UHD"],
    "Parlantes Bluetooth": ["Flip", "SoundLink", "SRS-", "Boom", "Stanmore"],
    "Cargadores": ["PowerPort", "PowerCore", "MagSafe", "67W GaN"],
    "Consolas": ["PlayStation", "Xbox Series", "Switch"],
    "Accesorios Gaming": ["DeathAdder", "G Pro", "BlackShark", "Arctis", "K70"]
}

# ============================
# Configuración
# ============================
TOTAL_PRODUCTOS = 30
ARCHIVO_SALIDA = "data/catalogo_productos_electronicos.csv"

# ============================
# Generador de productos
# ============================
def generar_precio(categoria):
    rangos = {
        "Smartphones": (250000, 1800000),
        "Notebooks": (400000, 3500000),
        "Tablets": (120000, 1200000),
        "Auriculares": (15000, 450000),
        "Smartwatches": (80000, 850000),
        "Televisores": (180000, 2500000),
        "Parlantes Bluetooth": (25000, 380000),
        "Cargadores": (8000, 85000),
        "Consolas": (450000, 900000),
        "Accesorios Gaming": (20000, 280000)
    }
    min_p, max_p = rangos.get(categoria, (50000, 500000))
    # Distribución realista: más productos baratos que caros
    if random.random() < 0.6:
        return round(random.uniform(min_p, min_p * 2.5), 2)
    elif random.random() < 0.9:
        return round(random.uniform(min_p * 2, min_p * 4), 2)
    else:
        return round(random.uniform(min_p * 4, max_p), 2)

def generar_nombre_producto(categoria, marca):
    base = random.choice(modelos_base.get(categoria, ["Pro", "Plus", "Ultra"]))
    sufijos = ["Pro", "Max", "Ultra", "Lite", "Air", "Mini", "SE", "Gaming", "RGB", ""]
    numero = random.choice(["", " 14", " 15", " 16", " 6", " 7", " 8", " 9", " 10", " 11", " 13", " 2024", " 2025"])
    
    if categoria == "Televisores":
        pulgadas = random.choice(["43\"", "50\"", "55\"", "65\"", "75\"", "85\""])
        return f"{marca} {base} {pulgadas} 4K Smart TV"
    elif categoria == "Consolas":
        return f"{marca} {base} {random.choice(['', 'S', 'X', 'OLED'])}"
    else:
        sufijo = random.choice(sufijos)
        return f"{marca} {base}{numero}{' ' + sufijo if sufijo else ''}".strip()

# ============================
# Generación del catálogo
# ============================

productos = []
usados = set()  # Para evitar nombres duplicados exactos

for i in range(1, TOTAL_PRODUCTOS + 1):
    product_id = f"P{i:03d}"
    
    categoria = random.choices(
        list(marcas_por_categoria.keys()),
        weights=[15, 12, 8, 10, 8, 8, 8, 8, 5, 6],  # Smartphones y notebooks más comunes
        k=1
    )[0]
    
    marca = random.choice(marcas_por_categoria[categoria])
    
    # Generar nombre único
    while True:
        nombre = generar_nombre_producto(categoria, marca)
        if nombre not in usados:
            usados.add(nombre)
            break
    
    precio = generar_precio(categoria)
    
    productos.append({
        "ProductID": product_id,
        "ProductName": nombre,
        "Category": categoria,
        "Brand": marca,
        "Price": precio
    })

# Ordenar por ProductID
productos.sort(key=lambda x: x["ProductID"])

# ============================
# Guardar en CSV
# ============================

keys = productos[0].keys()
with open(ARCHIVO_SALIDA, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=keys)
    writer.writeheader()
    writer.writerows(productos)

# ============================
# Mostrar resultado
# ============================
print(f"Listo! Se generaron {TOTAL_PRODUCTOS} productos electrónicos")
print(f"Archivo: {ARCHIVO_SALIDA}\n")
print("Ejemplos:")
print("-" * 90)
for p in productos[:12]:
    print(f"{p['ProductID']} | {p['ProductName'][:50]:50} | {p['Category']:18} | {p['Brand']:10} | ${p['Price']:,.0f}")
print("... y más!")

# Opcional: guardar también en formato más bonito para leer
with open("data/catalogo_productos_electronicos.txt", "w", encoding="utf-8") as f:
    f.write("CATÁLOGO DE PRODUCTOS ELECTRÓNICOS - ARGENTINA\n")
    f.write("="*90 + "\n\n")
    for p in productos:
        f.write(f"{p['ProductID']} | {p['ProductName']:55} | {p['Category']:18} | {p['Brand']:10} | ${p['Price']:,.0f} ARS\n")
