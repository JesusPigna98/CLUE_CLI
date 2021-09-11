##Jesús Piña García 19110309
##Practica1 - CLUE
import random
import time

class juego:
    contador = 0
    x = False

    def __init__(self, personajes_iniciales, armas_iniciales, lugares_iniciales) -> None:
        self.personajes_iniciales = personajes_iniciales
        self.armas_iniciales = armas_iniciales
        self.lugares_iniciales = lugares_iniciales

    def randomizar_historia(self):
        self.personajes_random = random.sample(self.personajes_iniciales, len(self.personajes_iniciales))
        self.lugares_random = random.sample(self.armas_iniciales, len(self.lugares_iniciales))
        self.armas_random = random.sample(self.lugares_iniciales, len(self.armas_iniciales))
        return self.personajes_random, self.lugares_random, self.armas_random ##Retornamos en orden: Culpable, lugar, arma

    def elegir_culpable(self):
        random.seed(time.time())
        self.culpable = random.choice(self.personajes_random)
        self.lugar_culpable = random.choice(self.lugares_random)
        self.arma_culpable = random.choice(self.armas_random)

        return self.culpable, self.lugar_culpable, self.arma_culpable ##Retornamos en orden: Culpable, lugar, arma

    
    def eleccion_nombres(self):
        print("La espiga de autlan")
        self.x = True

    def eleccion_lugar(self):
        print("kepedo")
        self.x = True

    def eleccion_arma(self):
        self.x = True

    def opciones_juego(self):
        for i in range(6):
            self.contador += 1
            self.x = False

            while self.x == False:
                try:
                    if self.contador == 5:
                        self.x = True
                        break

                    opc = int(input("Elige una categoria a investigar:\n 1-Personaje\n 2-Lugar\n 3-Arma\nCategoria:"))
                    self.eleccion(opc)    

                except (ValueError, KeyError):
                    print("****Categoria invalida****")

        ##Función final
                
                    

    def eleccion(self,i): ##Switch-case para repetir unicamente 5 veces
        switch = {
                1:self.eleccion_nombres,
                2:self.eleccion_lugar,
                3:self.eleccion_arma,
            }
        
        return switch[i]()
            


    
"""
def instrucciones():
    print("*****")
"""

    


##----------------Main-----------------##
personajes_iniciales = ["Filiponcio", "Facundo", "Giselle", "Pancracio", "Chepina"]
armas_iniciales = ["Bolillo", "Sarten", "Cuchillo", "Hacha", "Machete"]
lugares_iniciales = ["Almacen", "Cocina", "Herreria", "Sala", "Jardin"]


obj_inicializacion = juego(personajes_iniciales, armas_iniciales, lugares_iniciales)

personajes, lugares, armas = obj_inicializacion.randomizar_historia()
culpable_personaje, culpable_lugar, culpable_arma = obj_inicializacion.elegir_culpable()

obj_inicializacion.opciones_juego()





