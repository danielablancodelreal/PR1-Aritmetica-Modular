import sys
import modular
import time

def procesar_argumentos_entrada(argumentos):
    if len(sys.argv) == 1:
        modo = 1
    elif len(sys.argv) == 3:
        modo = 2
    return modo

def procesar_archivos(argumentos):
    # ficheros
    fichero_entrada = sys.argv[1]
    fichero_salida = sys.argv[2]
    # abrimos el fichero de entrada y creamos el de salida.
    file1 = open(fichero_entrada, "r")
    file2 = open(fichero_salida, "w")
    # devolvemos ficheros
    return [file1, file2]

def run_commands(file1, file2):
    
    exception = False

    print("Modo procesamiento por lotes")
    
    contenido = file1.readlines()
    automatico_lineas = 0

    while automatico_lineas != len(contenido):

        # Cogemos entrada
        entrada = contenido[automatico_lineas]
        if entrada[-1] == "\n": entrada = entrada[:-1]
        automatico_lineas += 1

        try: 
            argumentos = procesar_entrada(entrada)
            r  = procesar_operacion(argumentos)
            if r == None: 
                file2.write("NE\n")
            else:
                file2.write(str(r) + "\n")
        except:
            file2.write("NOP\n")

    # Cuando no quedan más lineas, se sale
    file1.close
    file2.close

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
        except: 
            raise exception
    
    elif op == "primos":
        # Los operandos no son enteros --> Error (NOP)
        try:
            entero(argumentos[1])
            if len(argumentos[1]) == 2:
                a = argumentos[1][0]
                b = argumentos[1][1]
                return modular.lista_primos(a,b) 
        except:
            raise exception
    
    elif op == "factorizar":
        # Los operandos no son enteros --> Error (NOP)
        try:
            entero(argumentos[1])
            if len(argumentos[1]) == 1:
                n = argumentos[1][0]
                return modular.factorizar(n)
        except:
            raise exception
    
    elif op == "mcd":
        # Los operandos no son enteros --> Error (NOP)
        try:
            entero(argumentos[1])
            if len(argumentos[1]) == 2:
                a = argumentos[1][0]
                b = argumentos[1][1]
                return modular.mcd(a,b)
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
                # Si el exponente es menor que 0 o el módulo es 0, NOP
                return modular.potencia_mod_p(base,exp,p)
        except:
            raise exception
    
    elif op == "inv":
        # Los operandos no son enteros --> Error (NOP)
        try:
            entero(argumentos[1])
            if len(argumentos[1]) == 2:
                n = argumentos[1][0]
                p = argumentos[1][1]
                return modular.inversa_mod_p(n,p)
        except:
            raise exception
    
    elif op == "euler":
        # Los operandos no son enteros --> Error (NOP)
        try:
            entero(argumentos[1])
            if len(argumentos[1]) == 1:
                n = argumentos[1][0]
                return modular.euler(n)
        except:
            raise exception

    elif op == "legendre":
        # Los operandos no son enteros --> Error (NOP)
        try:
            entero(argumentos[1])
            if len(argumentos[1]) == 2:
                n = argumentos[1][0]
                p = argumentos[1][1]
                return modular.legendre
        except: 
            raise exception
    
    elif op == "resolverSistema":
        arg = []
        a = []
        b = []
        p = []
        try:
            for l in range(len(argumentos[1])):
                arg.append(argumentos[1][l][argumentos[1][l].find("[")+1:argumentos[1][l].find("]")].split(";"))
            for k in range(len(arg)):
                if len(arg[k]) != 3:
                    return
                else:
                    a.append(int(arg[k][0]))
                    b.append(int(arg[k][1]))
                    p.append(int(arg[k][2]))
            return modular.resolver_sistema_congruencias(a,b,p)
        except: 
            raise exception 

    elif op == "mcd_n":
        p = []
        try:
            argumentos[1][0] = argumentos[1][0][argumentos[1][0].find("[")+1:len(argumentos[1][0])+1]
            argumentos[1][len(argumentos[1])-1] = argumentos[1][len(argumentos[1])-1][0:argumentos[1][len(argumentos[1])-1].find("]")]
            for k in range(len(argumentos[1])):
                p.append(int(argumentos[1][k]))
            return modular.mcd_n(p, p[0], 1)
        except: 
            raise exception
    
    elif op == "coprimos_n":
        p = []
        try:
            argumentos[1][0] = argumentos[1][0][argumentos[1][0].find("[")+1:len(argumentos[1][0])+1]
            argumentos[1][len(argumentos[1])-1] = argumentos[1][len(argumentos[1])-1][0:argumentos[1][len(argumentos[1])-1].find("]")]
            for k in range(len(argumentos[1])):
                p.append(int(argumentos[1][k]))
            print(p)
            return modular.coprimos_n(p)
        except: 
            raise exception

    elif op == "raiz":
        ...

    else:
        raise exception

def entero(operandos):
    # Para cada número de la lista, comprobamos si es entero
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
        ficheros = procesar_archivos(sys.argv)

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
                    if r == None: 
                        print("NE")
                    else:
                        print(r)
                except:
                    print("NOP")    
                    
                          
        else:

            # Llamamos función run commands
            run_commands(ficheros[0], ficheros[1])


            
