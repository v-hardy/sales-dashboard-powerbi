import random
from datetime import datetime, timedelta
import csv

# ============================
# Datos base
# ============================

# Lista de provincias con código y peso aproximado según población real (2025)
# Buenos Aires y CABA tienen mucho más peso que Tierra del Fuego, por ejemplo
provincias_arg = [
    (101, "Buenos Aires",          450),   # ~17M hab → mucho peso
    (102, "Ciudad Autónoma de Buenos Aires", 280),
    (106, "Córdoba",              100),
    (121, "Santa Fe",              90),
    (113, "Mendoza",               50),
    (124, "Tucumán",               45),
    (118, "Salta",                 40),
    (103, "Catamarca",             12),
    (104, "Chaco",                 30),
    (105, "Chubut",                15),
    (107, "Corrientes",            30),
    (108, "Entre Ríos",            35),
    (109, "Formosa",               16),
    (110, "Jujuy",                 20),
    (111, "La Pampa",              10),
    (112, "La Rioja",              10),
    (114, "Misiones",              35),
    (115, "Neuquén",               20),
    (116, "Río Negro",             20),
    (119, "San Juan",              22),
    (120, "San Luis",              15),
    (122, "Santiago del Estero",   28),
    (123, "Tierra del Fuego",       5),
]

# Nombres y apellidos comunes en Argentina
nombres = ["Juan", "María", "Luis", "Ana", "Carlos", "Laura", "Diego", "Valeria", "Martín", "Sofía",
           "José", "Carolina", "Pablo", "Lucía", "Federico", "Julieta", "Gabriel", "Camila", "Matías", "Florencia"]

apellidos = ["González", "Rodríguez", "Gómez", "Fernández", "López", "Martínez", "Díaz", "Pérez", "Sánchez",
             "Romero", "Sosa", "Torres", "Ruiz", "Ramírez", "Flores", "Benítez", "Acosta", "Medina", "Herrera", "Aguirre"]

# ============================
# Configuración
# ============================
TOTAL_CLIENTES = 1500
ARCHIVO_SALIDA = "data/cartera_clientes.csv"

# ============================
# Generador de datos
# ============================
def generar_dni():
    return random.randint(25000000, 45000000)

def generar_telefono():
    return f"+54 9 11 {random.randint(1000,9999)} {random.randint(1000,9999)}"

def generar_email(nombre, apellido):
    dominios = ["gmail.com", "hotmail.com", "yahoo.com.ar", "outlook.com", "fibertel.com.ar", "speedy.com.ar"]
    base = f"{nombre.lower()}.{apellido.lower()}"
    if random.random() < 0.3:
        base += str(random.randint(10, 99))
    return f"{base}@{random.choice(dominios)}"

def generar_fecha_alta():
    start_date = datetime(2015, 1, 1)
    end_date = datetime(2025, 11, 23)
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return (start_date + timedelta(days=random_days)).strftime("%Y-%m-%d")

def generar_saldo_o_valor():
    # Distribución realista: muchos con saldo bajo, pocos con saldo alto
    if random.random() < 0.7:      # 70% clientes con saldo bajo
        return round(random.uniform(5000, 150000), 2)
    elif random.random() < 0.95:   # 25% saldo medio-alto
        return round(random.uniform(150000, 800000), 2)
    else:                          # 5% clientes premium
        return round(random.uniform(800000, 5000000), 2)

# ============================
# Generación de cartera
# ============================

clientes = []

# Separamos la lista para usar los pesos en random.choices
codigos, nombres_prov, pesos = zip(*provincias_arg)

for i in range(1, TOTAL_CLIENTES + 1):
    customer_id = f"C{i:04d}"
    
    nombre = random.choice(nombres)
    apellido = random.choice(apellidos)
    dni = generar_dni()
    email = generar_email(nombre, apellido)
    telefono = generar_telefono()
    fecha_alta = generar_fecha_alta()
    saldo = generar_saldo_o_valor()
    
    # Provincia ponderada por población
    prov_codigo = random.choices(codigos, weights=pesos, k=1)[0]
    prov_nombre = nombres_prov[codigos.index(prov_codigo)]
    
    clientes.append({
        "customer_id": customer_id,
        "nombre": nombre,
        "apellido": apellido,
        "nombre_completo": f"{nombre} {apellido}",
        "dni": dni,
        "provincia_codigo": prov_codigo,
        "provincia": prov_nombre,
        "email": email,
        "telefono": telefono,
        "fecha_alta": fecha_alta,
        "saldo_cuenta": saldo
    })

# ============================
# Guardar en CSV
# ============================

keys = clientes[0].keys()
with open(ARCHIVO_SALIDA, "w", newline="", encoding="utf-8") as f:
    dict_writer = csv.DictWriter(f, keys)
    dict_writer.writeheader()
    dict_writer.writerows(clientes)

print(f"Listo! Se generaron {TOTAL_CLIENTES} clientes en el archivo:")
print(f"→ {ARCHIVO_SALIDA}")
print("\nEjemplo de los primeros 5:")
for c in clientes[:5]:
    print(f"{c['customer_id']} | {c['nombre_completo']:25} | {c['provincia']:25} | ${c['saldo_cuenta']:,.2f}")