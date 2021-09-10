##Jesús Piña García 19110309
##Practica1 - CLUE
import random


class juego:
    def __init__(self, personajes_iniciales, armas_iniciales, lugares_iniciales) -> None:
        self.personajes_iniciales = personajes_iniciales
        self.armas_iniciales = armas_iniciales
        self.lugares_iniciales = lugares_iniciales

    def randomizar_historia(self):
        self.personajes_random = random.sample(self.personajes_iniciales, len(self.personajes_iniciales))
        self.lugares_random = random.sample(self.armas_iniciales, len(self.lugares_iniciales))
        self.armas_random = random.sample(self.lugares_iniciales, len(self.armas_iniciales))

    def elegir_culpable(self):
        self.culpable = self.personajes_random[0]
        self.lugar_culpable = self.lugares_random[0]
        self.arma_culpable = self.armas_random[0]

        return self.culpable, self.lugar_culpable, self.arma_culpable ##Retornamos en orden: Culpable, lugar, arma
    

    



personajes_iniciales = ["Filiponcio", "Facundo", "Giselle", "Pancracio", "Chepina"]
armas_iniciales = ["Bolillo", "Sarten", "Cuchillo", "Hacha", "Machete"]
lugares_iniciales = ["Almacen", "Cocina", "Herreria", "Sala", "Jardin"]


obj_inicializacion = juego(personajes_iniciales, armas_iniciales, lugares_iniciales)

obj_inicializacion.randomizar_historia()
print(obj_inicializacion.elegir_culpable())