def ingresar_notas():
    try:
        cantidad_notas = int(input("Ingrese la cantidad de notas a ingresar: "))  # Solicita al usuario la cantidad de notas a ingresar
        notas = []                                                                 # Inicializa una lista vacía para almacenar las notas

        for i in range(cantidad_notas):                                           # Itera sobre el rango de la cantidad de notas ingresadas
            nota = float(input(f"Ingrese la nota {i+1}: "))                       # Solicita al usuario que ingrese cada nota y la convierte a tipo float
            notas.append(nota)                                                     # Agrega la nota a la lista de notas

        return notas                                                              # Devuelve la lista de notas ingresadas
    except ValueError:                                                            # Manejo de excepción en caso de que se ingrese un valor no válido
        print("Error: Debes ingresar un número válido.")                          # Muestra un mensaje de error
        return []                                                                  # Devuelve una lista vacía en caso de error

def calcular_promedio(notas):
    if not notas:                                                                 # Verifica si la lista de notas está vacía
        return 0                                                                  # Si está vacía, devuelve 0 para evitar división por cero
    
    total = sum(notas)                                                           # Suma todas las notas
    promedio = total / len(notas)                                                # Calcula el promedio dividiendo la suma total por la cantidad de notas
    return promedio                                                             # Devuelve el promedio calculado

def contar_notas_mayores_al_promedio(notas, promedio):
    contador = 0                                                                # Inicializa un contador para contar las notas mayores que el promedio
    for nota in notas:                                                         # Itera sobre cada nota en la lista de notas
        if nota > promedio:                                                   # Compara si la nota es mayor que el promedio
            contador += 1                                                    # Si es mayor, incrementa el contador en 1
    return contador                                                           # Devuelve el contador con la cantidad de notas mayores que el promedio

def main():
    notas = ingresar_notas()                                                # Llama a la función para ingresar las notas
    if notas:                                                               # Verifica si la lista de notas no está vacía
        print("Las notas ingresadas son:", notas)                         # Imprime las notas ingresadas
        
        promedio = calcular_promedio(notas)                              # Calcula el promedio de las notas
        print("El promedio de las notas es:", promedio)                # Imprime el promedio de las notas
        
        notas_mayores_al_promedio = contar_notas_mayores_al_promedio(notas, promedio)  # Cuenta las notas mayores al promedio
        print("Cantidad de notas mayores al promedio:", notas_mayores_al_promedio)   # Imprime la cantidad de notas mayores al promedio

if __name__ == "__main__":
    main()   # Llama a la función principal si el script se ejecuta directamente
