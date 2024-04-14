class Automovil:
    def __init__(self, color, marca, modelo, num_puertas, placa):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.num_puertas = num_puertas
        self.placa = placa
    
    def __str__(self):
        return f"Automóvil: {self.color} {self.marca} {self.modelo}, Puertas: {self.num_puertas}, Placa: {self.placa}"

# Función para crear instancias de Automovil
def crear_automovil():
    color = input("Introduce el color del automóvil: ")
    marca = input("Introduce la marca del automóvil: ")
    modelo = input("Introduce el modelo del automóvil: ")
    num_puertas = int(input("Introduce el número de puertas del automóvil: "))
    placa = input("Introduce la placa del automóvil: ")
    return Automovil(color, marca, modelo, num_puertas, placa)

# Crear una lista para almacenar los automóviles
inventario = []

# Solicitar al usuario la información de cinco automóviles y agregarlos al inventario
for _ in range(5):
    print("\nIntroduce la información del automóvil:")
    automovil = crear_automovil()
    inventario.append(automovil)

# Imprimir los automóviles en el inventario
print("\nAutomóviles en el inventario:")
for i, automovil in enumerate(inventario, 1):
    print(f"\nAutomóvil {i}:")
    print(automovil)
