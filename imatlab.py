import sys
import re
import modular

def procesar_argumentos_entrada(argumentos):
    if len(sys.argv) == 1:
        print("Modo interactivo")
        modo = 1
    elif len(sys.argv) == 3:
        print("Modo procesamiento por lotes")
        modo = 2
    return modo

def procesar_ficheros(argumentos):
    # variables
    contenido = []
    automatico_lineas = 0
    # ficheros
    fichero_entrada = sys.argv[1]
    fichero_salida = sys.argv[2]
    # abrimos el fichero de entrada y creamos el de salida.
    file = open(fichero_entrada, "r")
    contenido = file.readlines()
    file.close()
    file = open(fichero_salida, "w")
    file.close()
    # devolvemos ficheros
    ficheros = [fichero_salida, contenido, automatico_lineas]
    return ficheros

def entero(operandos):
    for num in operandos:
        try: num = int(num)
        except ValueError as error: raise error

if __name__ == "__main__":

    salir = False
    error = False

    # Miramos de que modo queremos que se ejecute el programa, por pantalla, o por ficheros
    modo = procesar_argumentos_entrada(sys.argv)

    if modo == 2:
        # Llamamos a la función de lectura de ficheros
        ficheros = procesar_ficheros(sys.argv)

    while not salir:
        
        if modo == 1:
            # Pedimos la operación a realizar
            entrada = input("Introduce la operación a realizar (introduzca OFF si desea salir del programa):")

            # Si el usuario introduce OFF, significa que desea salir
            if entrada == "OFF":
                salir = True

        else:
            # Leemos línea a línea
            contenido = ficheros[1]
            automatico_lineas = ficheros[2]
            ficheros[2] += 1

            # Cuando no quiedan más lineas, se sale
            if automatico_lineas == len(contenido): salir = True

            # Cogemos entrada
            else: 
                entrada = contenido[automatico_lineas]
                if entrada[-1] == "\n":
                    entrada = entrada[:-1]

        if not salir:

            # Procesar entrada
            try:
                operacion = entrada.split("(")
                op = operacion[0]
                variables = re.findall(r'[(](.*?)[)]', entrada)
                var = variables[0].split(",")
            except: error = True

            if not error:
                operandos = []
                # Los operandos no son enteros --> Error (NOP)
                try: entero(operandos)
                except: error = True

            
