import random #inmporta módulo random de python

def configuracion(): #establece configuración de la máquina
    abecedario = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ' #abecedario por defecto
    valid = False
    while not valid: #mientras valid es falso
        print('abecedario predeterminado =',abecedario) #muestra abecedario por defecto
        default = input('Quieres usar el diccionario predeterminado? (S/N) ')
        if default.isalpha and default.upper() == 'N': #si no quiere usar el abecedario por defecto
            abcAux = input ('Introduce el abecedario: ')
            valid = True #pone valid a verdadero
            for letra in abcAux: #recorre todas las letras del abecedario
                if not letra.isalpha() or abcAux.count(letra) > 1: #si no es letra o la letra se repite vuelve a poner valid a falso, en otro caso se mantiene verdadero
                    valid = False
            if valid: #si el abecedario introducido es válido lo copia a la variable por defecto
                abecedario = abcAux
        elif default.isalpha and default.upper() == 'S': #si quiere usar el abecedario por defecto pone valid a True
            valid = True
    abecedario = abecedario.upper() #asegura que el diccionario está en mayúsculas
    rotorNum = 1 #por ahora no hay selección de número de rotores ¯\_(ツ)_/¯
    config = (abecedario,rotorNum) #crea un tupla con la configuración
    return config

def creaRodillo(tipo,abecedario): #recibe como argumentos el tipo de rodillo (rotor, reflector) y abecedario que usar, para usar en otros idiomas
    abecedarioLista = list(abecedario) #convierte a lista la cadena abecedario
    if tipo == 'reflectorRandom': #si es un reflector al azar lo creamos
        reflector = [] #crea el reflector como una lista vacía
        while len(abecedarioLista) > 0: #mientras haya letras sin emparejar en el reflector las empareja
            letra = random.choice(abecedarioLista) #elige una letra al azar de la lista creada a partir del abecedario
            abecedarioLista.pop(abecedarioLista.index(letra)) #elimina de abecedarioLista la letra que se codifica para no repetir
            letraRandom = random.choice(abecedarioLista) #elige otra letra al azar de la lista creada a partir del abecedario para emparejar con la anterior
            abecedarioLista.pop(abecedarioLista.index(letraRandom)) #elimina de abecedarioLista la letra a la cual se ha emparejado la anterior para no repetir
            reflector.append((letra,letraRandom)) #en la lista rotor mete la pareja de índices letra original y letra codificada
        return (reflector) #devuelve la lista con las parejas de índices del reflector

    elif tipo == 'rotorRandom': #si es un rotor al azar lo creamos
        rotor = random.shuffle(abecedarioLista) #crea el rotor haciendo un shuffle del abecedario
        return rotor #devuelve la lista de índices del rotor

def inputLetra(abecedario):
    valid = False
    while not valid:
        letra = input('Introduce una letra para establecer la posición inicial del rotor: ')
        if letra.isalpha() and letra.upper() in abecedario: #si la letra de inicialización es válida y se encuentra en abecedario devolverla
            return letra.upper()

def inputMensaje(): #introducir mensaje
    valid = False
    while not valid: #mientras valid es falso
        msg = input ('Introduce el mensaje: ')
        valid = True #pone valid a verdadero
        for letra in msg: #recorre todas las letras del mensaje
            if not letra.isalpha() and letra != ' ' and letra != '.': #si no es letra, espacio o punto vuelve a poner valid a falso, si no se mantiene verdadero
                valid = False
    return msg.upper() #pone el mensaje en mayúsculas para evitar que no coincida luego al comparar

def inicializa(rotor,letra): #inicializa el rotor en la letra seleccionada
    pos = rotor.index(letra) #posición de la letra en el rotor
    #print('posición de la letra en el abecedario: {}, posición en rotor: {}'.format(posLetra,pos))
    #print(rotor)
    rotorAux = rotor[pos:] + rotor[:pos] #ponemos el rotor a 0 a la altura de la letra inicial
    #posAux = rotorAux.index(letra)
    #print('posición de la letra en el abecedario: {}, posición en rotorAux: {}'.format(posLetra,posAux))
    #print(rotorAux)
    return rotorAux

def avanza(rotor): #adelanta el rotor una posición
    rotor = rotor[1:] + rotor[:1] #coge desde la posición 2 del rotor hasta el final y le suma la primera
    return rotor

def cruzaRotor(rotor,pos): #avanza a través del rotor
        letra = rotor[pos] #según la posición de la letra en el avance anterior (abecedario para el 1º y último) elige la letra correspondiente en el rotor
        return letra

def cruzaReflector(reflector,letra): #avanza a través de los rotores
    #print('reflector:',reflector) #comprobación debug
    for pareja in reflector: #para cada pareja de letras del reflector
        if pareja[0].count(letra) > 0 or pareja[1].count(letra) > 0: #si encuentra la letra
            print('pareja reflector',pareja) #comprobación debug
            if pareja[0] == letra: #devuelve la derecha si está en el lado izquierdo
                letraCod = pareja[1]
            else: #devuelve la izquierda si está en el lado derecho
                letraCod = pareja[0]
    return letraCod

#donde ponga "#comprobación debug" es un print de variables para entender mejor qué está ocurriendo, eliminar # del inicio de línea para que lo muestre en consola
if __name__ == '__main__': #si se ejecuta directamente el programa en lugar de llamarlo desde otro hacer esto
    config = configuracion() #archivo de configuración para elegir número de rotores, cuáles o que los genere de forma aleatoria y el abecedario
    abecedario = config[0]
    if (len(abecedario) % 2) != 0: #comprueba si el número de letras del abecedario es par, debe serlo para usar el reflector, que se empareja consigo mismo
        abecedario += '@' #si no es par añade el caracter @
    #rotor = creaRodillo('rotorRandom',abecedario) #crea un rotor del tipo que se le diga, generado al azar o predefinido, con el abecedario elegido
    rotor = ['I', 'S', 'U', 'R', 'P', 'Q', '@', 'H', 'G', 'V', 'T', 'W', 'N', 'A', 'Ñ', 'B', 'X', 'L', 'M', 'Z', 'F', 'O', 'C', 'D', 'Y', 'J', 'E', 'K']
    #reflector = creaRodillo('reflectorRandom',abecedario) #crea el reflector del tipo que se le diga, generado al azar o predefinido, con el abecedario elegido
    reflector = [('U', 'O'), ('Q', '@'), ('F', 'G'), ('W', 'A'), ('L', 'K'), ('X', 'M'), ('J', 'E'), ('H', 'V'), ('Y', 'N'), ('C', 'S'), ('Ñ', 'P'), ('D', 'I'), ('R', 'B'), ('T', 'Z')]
    letraInicio = inputLetra(abecedario) #pide la posición inicial del rotor del abecedario elegido
    while True: #bucle general del programa, es infinito, para romper "CTRL + C" en Windows, "command + ." en Mac
        rotorAux = inicializa(rotor,letraInicio) #crea una copia del rotor en el punto de inicio
        #print('rotor original:',rotor) #comprobación debug
        #print('rotor inicializado',rotorAux) #comprobación debug
        mensaje = inputMensaje() #pide el mensaje a codificar, que está en una función aparte para incluir la validación
        mensajeCod = '' #define variable donde guardar el mensaje codificado
        for letra in mensaje: #recorre cada letra del mensaje
            if letra != ' ' and letra != '.': #si no es espacio ni punto
                rotorAux = avanza(rotorAux) #avanza el rotor
                #print('avanza rotor',rotorAux) #comprobación debug
                posLetra = abecedario.index(letra) #saca su posición en la lista abecedario
                print('Letra pulsada:',letra,posLetra) #comprobación debug
                letraCod = cruzaRotor(rotorAux,posLetra) #según la posición de la letra en la lista devuelve la codificada
                print('tras rotor:',letraCod,rotorAux.index(letraCod)) #comprobación debug
                letraCod = cruzaReflector(reflector,letraCod) #devuelve la pareja conectada mediante el reflector
                posLetra = rotorAux.index(letraCod) #saca la posición en el rotor de la letra devuelta por el reflector
                print('tras reflector:',letraCod) #comprobación debug
                letraCod = cruzaRotor(rotorAux,posLetra) #según la posición de la letra en la lista devuelve la codificada (con un rotor es irrelevante)
                print('tras rotor:',letraCod,posLetra) #comprobación debug
                bombilla = abecedario[posLetra] #devuelve la letra codificada que corresponde a la posición del rotor en el abecedario
                print('bombilla:',bombilla,posLetra) #comprobación debug
            else: #si es espacio o punto lo añade directamente
                bombilla = letra
            mensajeCod += bombilla #añade la letra codificada a través de los rotores al mensaje
        print(mensajeCod) #imprime mensaje codificado