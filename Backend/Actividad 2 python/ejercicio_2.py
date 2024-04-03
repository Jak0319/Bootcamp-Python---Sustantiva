#------------------------------------------------------ Actividad ----------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------------------------------#
# Ingresar 5 números flotantes por teclado que estén comprendidas entre 0 y 10,                                                         #
# luego mostrar todas las notas, luego la nota media, luego la nota más alta que se obtiene así como la nota menor                      #
#---------------------------------------------------------------------------------------------------------------------------------------#

# Función obtener notas #
def obtener_notas():
    notas = []
    for i in range(5):
        while True:
            nota = float(input(f"Ingrese la nota {i+1} (entre 0 y 10): "))
            if 0 <= nota <= 10:
                notas.append(nota)   
                break
            else:
                print("Error: La nota debe estar entre 0 y 10. Inténtelo de nuevo.")
    return notas
#----------------------------------------------------------------------------------------------------#
# Función nota media 
def calcular_media(notas):
    return sum(notas) / len(notas)
#----------------------------------------------------------------------------------------------------#
# Función nota más alta
def obtener_nota_mas_alta(notas):
    return max(notas)
#----------------------------------------------------------------------------------------------------#
# Función nota más baja
def obtener_nota_mas_baja(notas):
    return min(notas)
#----------------------------------------------------------------------------------------------------#
notas = obtener_notas()
print( )   
print("Todas las notas ingresadas:", notas)   # imprime las notas ingresadas
print( )   
media = calcular_media(notas)                 # llamado a función nota media
print("Nota media:", media)                   # imprime la nota media
print( )   
nota_mas_alta = obtener_nota_mas_alta(notas)  # llamado a función nota más alta
print("Nota más alta:", nota_mas_alta)        # imprime la nota más alta
print( ) 
nota_mas_baja = obtener_nota_mas_baja(notas)  # llamado a función nota más baja 
print("Nota más baja:", nota_mas_baja)        # imprime la nota más baja
print( )   
