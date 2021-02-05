import random

class Reflector():
    def __init__(self,conf=''):
        '''
            si conf viene vacio, crear uno (abecedario)
            si conf viene lleno, comprobar que cumple las especificaciones
        '''
        if conf == '':
            pass
            #reflejo = ''
            #abecedario = Enigma.abecedario
            #reflejoLista = list(abecedario)
            #random.shuffle(abecedario)
            #for letra in reflejoLista:
            #    reflejo += letra
            #self.configuracion = (abecedario,reflejo)
        else:
            refD = list(conf[1])
            for letra in conf[0]:
                refD.remove(letra)
            if len(refD) > 0:
                print('Sobran letras en el bastidor derecho')
            else:
                self.configuracion = conf

    def refleja(self,indice):
        letra = self.configuracion[0][indice]
        return self.configuracion[1].index(letra)

class Rotor():
    def __init__(self, abecedario,cortocircuito):
        self.conexion = [abecedario,cortocircuito]
        self._pos_ini = None
        self._pos_salto = None
        self.salto = False
    
    def inicializa(self):
        indiceInicial = self.conexion[0].index(self._pos_ini)
        self.conexion[0] = self.conexion[0][indiceInicial:] + self.conexion[0][:indiceInicial]
        self.conexion[1] = self.conexion[1][indiceInicial:] + self.conexion[1][:indiceInicial]
        self._pos_salto = self.conexion[1][-1]

    def avanza(self):
        self.conexion[0] = self.conexion[0][1:] + self.conexion[0][:1]
        self.conexion[1] = self.conexion[1][1:] + self.conexion[1][:1]
        if self.conexion[0] == self._pos_salto:
            self.salto = True

    def codifica(self, indice):
        letra = self.conexion[0][indice]
        indice_izda = self.conexion[1].index(letra)
        return indice_izda

    def decodifica(self, indice):
        letra = self.conexion[1][indice]
        indice_dcha = self.conexion[0].index(letra)
        return indice_dcha

    @property
    def pos_ini(self):
        return self._pos_ini

    @pos_ini.setter
    def pos_ini(self, value):
        self._pos_ini = self.conexion[0].index(value)

    '''
        TODO:
            - Conexion: Lista de cadenas (abecedario, cortocircuito) que 
              determina la entrada y salida según el caracter de salida o entrada
            - Posicion: Indice/caracter en posición cero de la conexión
            - Pasos ¿?: Número de pasos girados desde que empezamos a codificar
            - Salto: Indice, caracter de abecedario en que se obliga al salto del 
              siguiente rotor si lo hubiera
            - swSalto ¿?: True o False
            - codifica(indice): Devuelve el pin de salida
            - decodifica(indice): Devuelve el pin de entrada
            - avanza(): Rota una posición la conexión. Comprueba si debe activar swSalto 
    '''

class Enigma():
    def __init__(self,mensaje):
        self.abecedario = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
        #self.abecedario = creaABC()
        self.reflectorConfig = ('ABCDEFGHIJKLMNÑOPQRSTUVWXYZ','ZYXWVUTSRQPOÑNMLKJIHGFEDCBA')
        self.rotorConexiones = ('ÑMHCKWNOJFZEPSUBGRXAIQTVYLD')
        self.mensaje = mensaje
        self.mensajeCod = ''
        self.codifica(mensaje)
        
    def codifica(self,mensaje):
        self.reflector = Reflector(self.reflectorConfig)
        self.rotor = Rotor(self.abecedario,self.rotorConexiones)
        self.rotor.pos_ini = 'A'
        print(self.abecedario)
        for letra in self.mensaje:
            #print('letra: {} {}'.format(letra,self.abecedario.index(letra)))
            self.rotor.avanza()
            indiceCod = self.rotor.codifica(self.abecedario.index(letra))
            #print('tras rotor: {} {}'.format(self.abecedario[indiceCod],indiceCod))
            indiceCod = self.reflector.refleja(indiceCod)
            #print('tras reflector: {} {}'.format(self.abecedario[indiceCod],indiceCod))
            indiceCod = self.rotor.decodifica(indiceCod)
            letraCod = self.abecedario[indiceCod]
            #print('tras rotor_back: {} {}'.format(letraCod,indiceCod))
            self.mensajeCod += letraCod
        print(self.mensajeCod)
        '''
        TODO:
            - reflector: su configuración prefijada en principio
            - rotor: su conexión prefijada en principio
            - posi_inicial: Letra inicial del rotor (indice?)
            - codifica(mensaje): Transforma el mensaje en uno nuevo. Solo hay una dirección.
            Si se pasa la salida de codifica como entrada volviendo la posi_inicial. Obtenemos
            la otra entrada. 
        '''

def creaABC():
    abecedario = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ' #abecedario por defecto
    valid = False
    while not valid: #mientras valid es falso solicita diccionario
        print('abecedario predeterminado =',abecedario) #muestra abecedario por defecto
        default = input('Quieres usar diccionario español predeterminado? (S/N) ')
        if default.isalpha and default.upper() == 'S': #si usa abecedario por defecto pone valid a True y sale del bucle
            valid = True
        elif default.isalpha and default.upper() == 'N': #si no quiere usar el abecedario por defecto
            valid = True #pone valid a verdadero y cambiará si hay errores
            abcAux = input ('Introduce el abecedario: ')
            for letra in abcAux: #recorre las letras del abecedario recién creado
                if not letra.isalpha() or abcAux.count(letra) > 1: #si no es letra o ésta se repite pone valid a falso
                    valid = False
            if valid: #si el abecedario introducido es válido lo copia a la variable por defecto
                abecedario = abcAux
    return abecedario
    
def inputMensaje():
    valid = False
    while not valid: #mientras valid es falso solicita mensaje
        valid = True #pone valid a verdadero y cambiará en caso de error
        msg = input ('Introduce el mensaje: ')
        for letra in msg: #recorre las letras del mensaje
            if not letra.isalpha() and letra != ' ' and letra != '.' and letra != ',': #si no es una letra, espacio, punto o coma, valid es falso
                valid = False
    return msg.upper() #devuelve el mensaje en mayúsculas para evitar que no coincida al comparar las letras en enigma

if __name__ == '__main__':
    while True: #bucle general del programa, es infinito, para romper "CTRL + C" en Windows, "command + ." en Mac
        mensaje = inputMensaje() #guarda el mensaje a codificar, llama a una función aparte para incluir la validación
        Enigma(mensaje) #llama a Enigma para iniciar la codificación/decodificación