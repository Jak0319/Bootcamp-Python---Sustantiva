#------------------------------------------------------ Actividad ----------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------------------------------#
# Programa que pida un número por teclado, este será un número de mes, y que diga cuántos días tiene el mes.                            #
# hay que usar listas para guardar los meses de año y los días que cada uno tiene, Febrero lo definiremos con 28 días.                  #
#---------------------------------------------------------------------------------------------------------------------------------------#
# Función #
#---------------------------------------------------------------------------------------------------------------------------------------#
def obtener_dias_del_mes(numero_mes):
    # Lista de días por mes (indexados desde 1)
    meses = ["", "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
             "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    dias_por_mes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Verificar si el mes es válido
    if 1 <= numero_mes <= 12:                                  # Verifica si el número de mes está dentro del rango válido
        return meses[numero_mes], dias_por_mes[numero_mes]     # Retorna el nombre del mes y la cantidad de días correspondientes al mes
    else:
        return "Mes inválido"                                  # Retorna un mensaje de error si el mes no es válido
#---------------------------------------------------------------------------------------------------------------------------------------#
while True:                                                    # Bucle para ejecutar siempre
    # Solicitar al usuario ingresar el número de mes
    numero_mes = int(input("Ingrese el número de mes (1 - 12), o ingrese 0 para salir: "))
    
    if numero_mes == 0:                                        # Si el usuario ingresa 0, salir del bucle y terminar el programa
        print("¡Hasta luego!")
        break
    
    nombre_mes_dias = obtener_dias_del_mes(numero_mes)         # Obtener el nombre del mes y el número de días del mes ingresado
    
    # Mostrar el resultado
    if nombre_mes_dias != "Mes inválido":                      # Verifica si el mes es válido
        nombre_mes, dias_del_mes = nombre_mes_dias
        print(f"{nombre_mes} tiene {dias_del_mes} días.")      # Muestra el nombre del mes y la cantidad de días del mes
    else:
        print(nombre_mes_dias)                                 # Muestra el mensaje de error si el mes no es válido
