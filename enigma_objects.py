import random

class Enigma():
    mensaje = ''
    mensajeCodigo = ''

    def __init__(self):
        self.rotor=Rotor()
        #self.reflector = Rotor()
        #self.configuracion()
        self.inputMensaje()
        for letra in self.mensaje:
            if letra != ' ' and letra != '.':
                self.mensajeCodigo += self.rotor.codifica(letra)
            else:
                self.mensajeCodigo += letra
        print(self.mensajeCodigo)

    def configuracion(self):
        self.respAleatorio = ''
        self.respAleatorio = input('rotores aleatorios? ')

    def inputMensaje(self):
        valid = False
        while not valid:
            self.mensaje = input ('Introduce el mensaje: ')
            valid = True
            for letra in self.mensaje:
                if not letra.isalpha() and letra != ' ' and letra != '.':
                    valid = False
        self.mensaje = self.mensaje.upper()
        print(valid)
        print (self.mensaje)

class Rotor():

    def __init__(self,abecedario = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'):
        self.abecedario = abecedario
        self.rotor = []
        self.abecedarioLista = list(self.abecedario)

        for letra in self.abecedario:
            letraRandom = random.choice(self.abecedarioLista)
            #print ('letra {} - letraRandom {}'.format(letra, letraRandom))
            self.rotor.append((letra, letraRandom))
            self.abecedarioLista.pop(self.abecedarioLista.index(letraRandom))

        self.rotorCopy = self.rotor[:]
        #print(self.rotorCopy)

    def codifica(self, letra):
        posLetra = self.abecedario.index(letra)
        print(letra,posLetra)
        return self.rotorCopy[posLetra][1]

        #for t in self.rotor:
        #    if letra == t[0]:
        #        return t[1]
        #raise ValueError('{} no pertenece al abecedario'.format(letra))

    def posicion(self,letra):
        position = self.abecedario.index(letra)
        self.rotorCopy = self.rotor[position:] + self.rotor[:position]

    def avanza(self):
        self.rotorCopy = self.rotorCopy[1:] + self.rotorCopy[0]

if __name__ == '__main__':
    while True:
        Enigma()