#------------------------------------------------------ Actividad ----------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------------------------------#
# Ingresar un número cualquiera que sea del 0 al 100, si se ingresa un número par, que se imprima en pantalla todos los números pares   #
# siguientes hasta el 100, y si se ingresa un número impar, que se impriman los números impares siguientes hasta el 99, si se ingresa   #
# un 0 o un número mayor a 100, que el programa envíe un mensaje de ERROR y que vuelva a preguntar por el ingreso de un número.         #
#---------------------------------------------------------------------------------------------------------------------------------------#
# Función #
#---------------------------------------------------------------------------------------------------------------------------------------#
def imprimir_siguientes_numeros(numero):
    if numero % 2 == 0:                                          # Si el número es par
        print("Los números pares siguientes hasta 100 son:")     # imprime los números pares hasta 100
        for i in range(numero + 2, 101, 2):
            print(i, end=" ")                                    # Imprime el número seguido de un espacio en la misma línea
    else:                                                        # Si el número es impar
        print("Los números impares siguientes hasta 99 son:")    # imprime los números impares hasta 99
        for i in range(numero + 2, 100, 2):
            print(i, end=" ")                                    # Imprime el número seguido de un espacio en la misma línea
#---------------------------------------------------------------------------------------------------------------------------------------#
# Bucle principal
while True:
    num = int(input("Ingrese un número (entre 1 y 100): "))      # Solicita al usuario ingresar un número
    if num == 0 or num > 100:                                    # Si el número es igual a 0 o mayor que 100
        print("Error: El número debe estar entre 1 y 100. Inténtelo de nuevo.")  # Muestra un mensaje de error
    else:
        imprimir_siguientes_numeros(num)                         # Llama a la función imprimir_siguientes_numeros con el número ingresado como argumento
        print("\n")                                              # Imprime una nueva línea después de imprimir los números siguientes

        

