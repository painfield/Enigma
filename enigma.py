import random

mensajeCodigo = ''


class Rotor():
    def __init__(self,abecedario = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'):
        self.abecedario = abecedario
        self.rotor = []
        otrasLetras = list(self.abecedario)
        for l in self.abecedario:
            letraRandom = random.choice(letrasAux)
            #print (letra, letraRandom)
            resultado.append((letra, letraRandom))
            letrasAux.pop(letrasAux.index(letraRandom))
        self.rotorC= self.rotor[:]

    def codifica(self, letra):
        posLetra = self.abecedario.index(letra)
        return self.rotorC[posLetra][1]
        self.avanza()

        #for t in self.rotor:
        #    if letra == t[0]:
        #        return t[1]
        #raise ValueError('{} no pertenece al abecedario')

    def posicion(self,letra):
        position = self.abecedario.index(letra)
        self.rotorC = self.rotor[position:] + self.rotor[:position]

    def avanza(self):
        self.rotorC = self.rotorC[1:] + self.rotorC[0]


"""
def creaRotor():
    
    letrasAux = list(letras)
    resultado = []

    for letra in letras:
        letraRandom = random.choice(letrasAux)
        #print (letra, letraRandom)
        resultado.append((letra, letraRandom))
        letrasAux.pop(letrasAux.index(letraRandom))
    return resultado

rotor = creaRotor()
reflector = creaRotor()

mensaje = input ('Introduce el mensaje: ')

for letra in mensaje:
    print(letra)
    for par in rotor:
        print(par)
        print(par[0],par[1])
        if letra == par[0]:
            print(letra)
            print(par[0],par[1])
            mensajeCodigo += par[1]
            print(mensajeCodigo)
    
#print(creaRotor())
print(mensajeCodigo)
"""