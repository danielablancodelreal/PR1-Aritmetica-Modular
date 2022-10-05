from operator import not_
import sys
import re
import modular
import time

def procesar_argumentos_entrada(argumentos):
    if len(sys.argv) == 1:
        print("Modo interactivo")
        modo = 1
    elif len(sys.argv) == 3:
        print("Modo procesamiento por lotes")
        modo = 2
    return modo

def run_commands(argumentos):
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
    
def procesar_operacion(argumentos):
    op = argumentos[0]

    if op == "primo":
        # Los operandos no son enteros --> Error (NOP)
        try:
            entero(argumentos[1])
            if len(argumentos[1]) == 1:
                n = argumentos[1][0]
                return modular.es_primo(n)
            else: raise error
        except:
            raise error
    
    elif op == "primos":
        # Los operandos no son enteros --> Error (NOP)
        try:
            entero(argumentos[1])
            if len(argumentos[1]) == 2:
                a = argumentos[1][0]
                b = argumentos[1][1]
                print(op,a,b)
            else: raise error
        except:
            raise error
    
    elif op == "factorizar":
        # Los operandos no son enteros --> Error (NOP)
        try:
            entero(argumentos[1])
            if len(argumentos[1]) == 1:
                n = argumentos[1][0]
                print(op,n)
            else: raise error
        except:
            raise error
    
    elif op == "mcd":
        # Los operandos no son enteros --> Error (NOP)
        try:
            entero(argumentos[1])
            if len(argumentos[1]) == 2:
                a = argumentos[1][0]
                b = argumentos[1][1]
                return modular.mcd(a,b)
            else: raise error
        except:
            raise error
    
    elif op == "coprimos":
        # Los operandos no son enteros --> Error (NOP)
        try:
            entero(argumentos[1])
            if len(argumentos[1]) == 2:
                a = argumentos[1][0]
                b = argumentos[1][1]
                return modular.coprimos(a,b)
            else: raise error
        except:
            raise error
    
    elif op == "pow":
        # Los operandos no son enteros --> Error (NOP)
        try:
            entero(argumentos[1])
            if len(argumentos[1]) == 3:
                base = argumentos[1][0]
                exp = argumentos[1][1]
                p = argumentos[1][2]
                print(op,base,exp,p)
            else: raise error
        except:
            raise error
    
    elif op == "inv":
        # Los operandos no son enteros --> Error (NOP)
        try:
            entero(argumentos[1])
            if len(argumentos[1]) == 2:
                n = argumentos[1][0]
                p = argumentos[1][1]
                r = modular.inversa_mod_p(n,p)
                if r == None: return "NOP"
                else: return r
            else: raise error
        except:
            raise error
    
    elif op == "euler":
        # Los operandos no son enteros --> Error (NOP)
        try:
            entero(argumentos[1])
            if len(argumentos[1]) == 1:
                n = argumentos[1][0]
                print(op,n)
            else: raise error
        except:
            raise error

    elif op == "legendre":
        # Los operandos no son enteros --> Error (NOP)
        try:
            entero(argumentos[1])
            if len(argumentos[1]) == 2:
                n = argumentos[1][0]
                p = argumentos[1][1]
                print(op,n,p)
            else: raise error
        except: raise error
    
    elif op == "resolverSistema":
        arg = []
        a = []
        b = []
        p = []
        try:
            for l in range(len(argumentos[1])):
                arg.append(argumentos[1][l][argumentos[1][l].find("[")+1:argumentos[1][l].find("]")].split(";"))
            for k in range(len(arg)):
                if len(arg[k]) == 3:
                    a.append(int(arg[k][0]))
                    b.append(int(arg[k][1]))
                    p.append(int(arg[k][2]))
                else: raise error        
            return modular.resolver_sistema_congruencias(a,b,p)
        except: raise error 
    
    elif op == "raiz":
        ...

    elif op == "ecCuadratica":
        ...

    else:
        raise error

def entero(operandos):
    for num in range(len(operandos)):
        try:
            operandos[num] = int(operandos[num])
        except:
            raise error

if __name__ == "__main__":

    salir = False

    # Miramos de que modo queremos que se ejecute el programa, por pantalla, o por ficheros
    modo = procesar_argumentos_entrada(sys.argv)
    
    if modo == 2:
        # Si es modo 2 abrimos ficheros
        ficheros = run_commands(sys.argv)
        # Leemos línea a línea
        contenido = ficheros[0].readlines()
        automatico_lineas = 0
    
    s = time.time()

    while not salir:
        
        error = False
        exception = False

        if modo == 1:

            # Pedimos la operación a realizar
            entrada = input("Introduce la operación a realizar (introduzca OFF si desea salir del programa):")
            # Si el usuario introduce OFF, significa que desea salir
            if entrada == "OFF":
                salir = True

            #############################################################################

            if not salir:
                try: 
                    argumentos = procesar_entrada(entrada)
                    r  = procesar_operacion(argumentos)
                    if r != None: print(r)
                except: 
                    if error:
                        print("NE")  
                    if exception:
                        print("NOP")
                    
        else:

            # Cuando no quedan más lineas, se sale
            if automatico_lineas == len(contenido):
                salir = True
                ficheros[0].close
                ficheros[1].close
            # Cogemos entrada
            else:
                entrada = contenido[automatico_lineas]
                if entrada[-1] == "\n": entrada = entrada[:-1]
                automatico_lineas += 1

            ##############################################################################

            if not salir:
                try: 
                    argumentos = procesar_entrada(entrada)
                    r  = procesar_operacion(argumentos)
                    if r != None: ficheros[1].write(str(r) + "\n")
                except: 
                    ficheros[1].write("NE\n")
    
    
    f = time.time()
    print("tiempo:", f-s) 

            
