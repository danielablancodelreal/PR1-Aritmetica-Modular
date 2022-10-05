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

def run_commands():
    # ficheros
    fichero_entrada = sys.argv[1]
    fichero_salida = sys.argv[2]
    # abrimos el fichero de entrada y creamos el de salida.
    file1 = open(fichero_entrada, "r")
    file2 = open(fichero_salida, "w")
    # devolvemos ficheros
    ficheros = [file1, file2]
    return ficheros

def procesar_entrada(entrada):
    try:
        lis = entrada.split("(", 1)
        operacion = lis[0]
        variables = lis[1].split(")", -1)
        operandos = variables[0].split(",")
        argumentos = [operacion, operandos]
    except: 
        raise error
    return argumentos
    
def procesar_operacion(op):
    ...

def entero(operandos):
    for num in range(len(operandos)):
        try: operandos[num] = int(operandos[num])
        except error: raise error

if __name__ == "__main__":

    salir = False
    error = False

    # Miramos de que modo queremos que se ejecute el programa, por pantalla, o por ficheros
    modo = procesar_argumentos_entrada(sys.argv)

    while not salir:
        
        if modo == 1:
            # Pedimos la operación a realizar
            entrada = input("Introduce la operación a realizar (introduzca OFF si desea salir del programa):")
            # Si el usuario introduce OFF, significa que desea salir
            if entrada == "OFF":
                salir = True
            #############################################################################
            if not salir:
                try: argumentos = procesar_entrada(entrada)
                except: error = True

                if not error:
                    procesar_operacion(argumentos[0])               


                    # Los operandos no son enteros --> Error (NOP)
                    try: entero(argumentos[1])
                    except: raise error
                    print(argumentos)

        else:
            ficheros = run_commands()
            # Leemos línea a línea
            contenido = ficheros[0].readlines()
            automatico_lineas = 0
            # Cuando no quedan más lineas, se sale
            if automatico_lineas == len(contenido):
                salir = True
                ficheros[0].close
                ficheros[1].close
            # Cogemos entrada
            else: 
                entrada = contenido[automatico_lineas]
                if entrada[-1] == "\n":
                    entrada = entrada[:-1]
                automatico_lineas += 1
            ##############################################################################
            if not salir:
                try: argumentos = procesar_entrada(entrada)
                except: error = True
            

            
