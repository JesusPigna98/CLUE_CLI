##Jesús Piña García 19110309
##Practica1 - CLUE
import random
import time
from os import system, name

class juego:
    contador = 0
    x = False
    personaje_final = ''
    lugar_final = ''
    arma_final = ''

    def __init__(self, personajes_iniciales, armas_iniciales, lugares_iniciales) -> None:
        self.personajes_iniciales = personajes_iniciales
        self.armas_iniciales = armas_iniciales
        self.lugares_iniciales = lugares_iniciales

    def randomizar_historia(self):
        self.personajes_random = random.sample(self.personajes_iniciales, len(self.personajes_iniciales))
        self.lugares_random = random.sample(self.lugares_iniciales, len(self.lugares_iniciales))
        self.armas_random = random.sample(self.armas_iniciales, len(self.armas_iniciales))

    def elegir_culpable(self):
        random.seed(time.time())
        self.culpable = random.choice(self.personajes_random)
        self.lugar_culpable = random.choice(self.lugares_random)
        self.arma_culpable = random.choice(self.armas_random)

    
    def eleccion_nombres(self):
        revisador = True

        print(f"****Eleccion de Personaje*****")

        while revisador == True:
            print("Elige uno de los personajes:\n")
            for i in range(len(self.personajes_random)):
                print(f"{i+1}- {self.personajes_random[i]}\n")

            opc = int(input("Opcion: "))    

            if(self.contador <6):
                try:
                    nombre_elegido = self.personaje(opc)
                    clear()
                    print(f"Personaje Elegido: {nombre_elegido}\trestan: {6-self.contador} oportunidades\n")
                
                except (ValueError, KeyError):
                    print("Personaje no existente")
                
                else:
                    revisador = False
                    self.historias_personajes(opc-1)

            else:
                revisador = False
                nombre_elegido = self.personaje(opc)
                self.personaje_final = nombre_elegido
                self.eleccion_lugar()
            

    def eleccion_lugar(self):
        revisador = True
        print(f"****Eleccion de Lugar*****\t restan: {6-self.contador} oportunidades\n")

        while revisador == True:
            print("Elige uno de los lugares:\n")
            for i in range(len(self.lugares_random)):
                print(f"{i+1}- {self.lugares_random[i]}\n")
            
            opc = int(input("Opcion: "))

            if(self.contador <6):
                try:
                    lugar_elegido = self.lugar(opc)
                    clear()
                    print(f"Lugar Elegido: {lugar_elegido}\trestan: {6-self.contador} oportunidades\n")
                
                except (ValueError, KeyError):
                    print("Lugar no existente")
                
                else:
                    revisador = False
                    self.historias_personajes(opc-1)

            else:
                revisador = False
                lugar_elegido = self.lugar(opc)
                self.lugar_final = lugar_elegido
                self.eleccion_arma()
                




    def eleccion_arma(self):
        revisador = True
        print(f"****Eleccion de Arma*****\t restan: {6-self.contador} oportunidades\n")

        while revisador == True:
            print("Elige una de las armas:\n")
            for i in range(len(self.armas_random)):
                print(f"{i+1}- {self.armas_random[i]}\n")
    
            opc = int(input("Opcion: "))

            if(self.contador <6):
                try:
                    arma_elegida = self.arma(opc)
                    clear()
                    print(f"Arma Elegida: {arma_elegida}\trestan: {6-self.contador} oportunidades\n")
                
                except (ValueError, KeyError):
                    print("Arma no existente")

                else:
                    revisador = False
                    self.historias_personajes(opc-1)

            else:
                revisador = False
                arma_elegida = self.arma(opc)
                self.arma_final = arma_elegida
                self.operacion_final(self.personaje_final,self.lugar_final,self.arma_final)

        
##------Función principal para seleccionar las opciones por 5 rondas. El contador inicia en 1.------##
    def iniciar_juego(self):
        for i in range(6):
            self.contador += 1
            self.x = False

            while self.x == False:
                try:
                    if self.contador == 6:
                        self.x = True
                        clear()
                        print(f"Se acabaron las opciones... es momento de decidir ¡quien es el asesino!")
                        self.eleccion_nombres()
                        break

                    opc = int(input("Elige una categoria a investigar:\n 1-Personaje\n 2-Lugar\n 3-Arma\nCategoria:"))
                    self.eleccion_historia(opc)    

                except (ValueError, KeyError):
                    print("****Categoria invalida****")
                
                else:
                    self.x = True

##------Función que elige la historia de forma aleatoria dependiendo de el objeto, lugar o persona seleccionada------##
    def historias_personajes(self, posicion):
        historia = ''
      
        ##Armado de las 5 historias##
        if self.lugares_random[posicion] == "la Sala":
            historia = "fumandose un cigarrito de procedencia desconocida"
        elif self.lugares_random[posicion] == "la Cocina":
            historia = "entrandole duro a un taco de camaron sobrante del dia de ayer"
        elif self.lugares_random[posicion] == "el Taller":
            historia = "afilando unos cuchillos para la cena del fin de semana"
        elif self.lugares_random[posicion] == "el Jardin":
            historia = "enterrando a jerry, el gato, que murio el mismo dia que John"
        elif self.lugares_random[posicion] == "el Almacen":
            historia = "buscando unos objetos faltantes desde el dia del asesinato"


        print(f"{self.personajes_random[posicion]} comenta que estaba {historia} en {self.lugares_random[posicion]} y vio el objeto {self.armas_random[posicion]}")
        
        if self.personajes_random[posicion] == self.culpable:
            print(f"-Juan, el mayordomo, comenta que le es dificil recordar haber visto a {self.personajes_random[posicion]} durante el dia")
        else:
            print(f"-{self.personajes_random[posicion]} fue visto por Juan, el mayordomo mientras hacia su recorrido por la casona")
        
        if self.lugares_random[posicion] == self.lugar_culpable:
            print(f"-Desafortunadamente Juan, el mayordomo, no pudo visitar {self.lugares_random[posicion]}, ya que tuvo que pasear a los perros")
        else:
            print(f"-Juan, el mayordomo, estuvo en {self.lugares_random[posicion]} y aprovecho para terminar unos pendientes")
        
        if self.armas_random[posicion] == self.arma_culpable:
            print(f"-Juan, el mayordomo, menciona que hacia falta el objeto {self.armas_random[posicion]} desde hace un par de dias")
        else:
            print(f"-Juan, el mayordomo, se aseguro de guardar el objeto {self.armas_random[posicion]} en su lugar sin excepcion")


##------Función final que recibe las elecciones finales del jugador------##
    def operacion_final(self,personaje, lugar, arma):
        if personaje == self.culpable and lugar == self.lugar_culpable and arma == self.arma_culpable:
            print("¡¡FELICIDADES!! Has dado con el asesino, el lugar y el arma de forma impecable")
        
        else:
            clear()
            print(f"Has perdido :( ¡suerte para la proxima! mis elecciones: [{personaje},{lugar},{arma}]\n")
            print("\t***********NOTAS DE DETECTIVE***********\n")
            if(personaje != self.culpable):
                print(f"{personaje} era inocente ya que Juan, el mayordomo, lo vio mientras hacia su reccorido")
            
            if(lugar != self.lugar_culpable):
                print(f"{lugar} no fue el lugar del asesinato ya que Juan, el mayordomo, visito el area mientras hacia su recorrido")
            
            if(arma != self.arma_culpable):
                print(f"{arma} no fue el arma utilizada en el asesinato ya que fue guardada en su lugar por Juan, el mayordomo")



##------Switchers para historia, arma, personaje y lugar------##
    def eleccion_historia(self,i):
        switch = {
                1:self.eleccion_nombres,
                2:self.eleccion_lugar,
                3:self.eleccion_arma,
            }
        
        return switch[i]()

    def personaje(self,i):
        switch = {
                1:self.personajes_random[0],
                2:self.personajes_random[1],
                3:self.personajes_random[2],
                4:self.personajes_random[3],
                5:self.personajes_random[4]
            }

        return switch[i]

    def lugar(self,i):
        switch = {
                1:self.lugares_random[0],
                2:self.lugares_random[1],
                3:self.lugares_random[2],
                4:self.lugares_random[3],
                5:self.lugares_random[4]
            }
        
        return switch[i]

    def arma(self,i):
        switch = {
                1:self.armas_random[0],
                2:self.armas_random[1],
                3:self.armas_random[2],
                4:self.armas_random[3],
                5:self.armas_random[4]
            }
        return switch[i]

    

def instrucciones():
    print("""

   _____ _     _    _ ______             _____           _____  ____  _   _          
  / ____| |   | |  | |  ____|           / ____|   /\    / ____|/ __ \| \ | |   /\    
 | |    | |   | |  | | |__     ______  | |       /  \  | (___ | |  | |  \| |  /  \   
 | |    | |   | |  | |  __|   |______| | |      / /\ \  \___ \| |  | | . ` | / /\ \  
 | |____| |___| |__| | |____           | |____ / ____ \ ____) | |__| | |\  |/ ____ \ 
  \_____|______\____/|______|           \_____/_/    \_\_____/ \____/|_| \_/_/    \_\
                                                                                     
 """)
    
    
    print("""
   _                             _               _  ___  _ _  ___ _____  ___   ___  
  (_) ___  ___ _   _ ___   _ __ (_)_ __   __ _  / |/ _ \/ / |/ _ \___ / / _ \ / _ \ 
  | |/ _ \/ __| | | / __| | '_ \| | '_ \ / _` | | | (_) | | | | | ||_ \| | | | (_) |
  | |  __/\__ \ |_| \__ \ | |_) | | | | | (_| | | |\__, | | | |_| |__) | |_| |\__, |
 _/ |\___||___/\__,_|___/ | .__/|_|_| |_|\__,_| |_|  /_/|_|_|\___/____/ \___/   /_/ 
|__/                      |_|                                                       
     """)
    
    
    
    print("\t\t*****CLUE - LA CASONA*****\n")
    print("John era un empresario muy exitoso que vivia en la casona 'Los Muertos', construida por el mismo.")
    print("El vivia con sus 5 hermanos que le tenian envidia por sus exitos y fortuna.")
    print("El dia de hoy.. John fue asesinado a sangre fria por alguien dentro de la casona y con un objeto perteneciente a la misma.\n Es tu trabajo encontrar al asesino, donde fue cometido el asesinato y el arma utilizada.\n\n\n")
    print("Hay 5 personas, armas y lugares donde se pudo cometer el asesinato. Tienes unicamente 5 rondas para deducir todo el crimen. SUERTE\n\n\n\n")

def clear():
    # windows
    if name == 'nt':
        _ = system('cls')
  
    #mac o linux
    else:
        _ = system('clear')



##----------------Main-----------------##
personajes_iniciales = ["Filiponcio", "Facundo", "Giselle", "Pancracio", "Chepina"]
armas_iniciales = ["Bolillo", "Sarten", "Cuchillo", "Hacha", "Machete"]
lugares_iniciales = ["el Almacen", "la Cocina", "el Taller", "la Sala", "el Jardin"]

instrucciones()
obj_inicializacion = juego(personajes_iniciales, armas_iniciales, lugares_iniciales)
obj_inicializacion.randomizar_historia()
obj_inicializacion.elegir_culpable()
obj_inicializacion.iniciar_juego()





