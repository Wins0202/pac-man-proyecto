""" Programa creado como proyecto para el módulo de IDME. En este proyecto está plasmada la 
creación del código del tradicional juego arcade de Pac-Man."""



""" ------------------------------------------------------
    ||||||Desarrollo de la clase "GAME" (class Game)||||||
    ------------------------------------------------------"""


#Importación de librerías:

import pygame #Libreria con la que se programa el juego. 
"""Para la correcta importación de la librería se tiene que descargar con el comando 
"pip install pygame" y se procederá a descargar la librería para su uso"""

from config import * #Importación de la librería creada para las configuraciones

from sprite import * #Importación de la librería creada para los movimientos


"""Este conjunto de líneas sirve para que se inicie el juego. Definiremos las funciones para el
control básico del juego"""
#Definición de variables:

class Game:
    def __init__ (self): 
    
        #Se crea la ventana:
        self.screen = pygame.display.set_mode ((width, height)) #activa el ancho y el alto de la ventana que se había importado de la pestaña creada
        pygame.display.set_caption ("PAC-MAN") #Nombre que tendrá la ventanilla cuando se abrá para jugar

        #Se establece un reloj para controlar la velocidad del juego
        self.clock = pygame.time.Clock ()

        #Se crea una variable para el bucle del juego
        self.running = True

        #Se crea al jugador:
        self.player = Player() 

    def handleEvents (self):
        #Manejar los eventos (función de las teclas en pygame)
        for event in pygame.event.get (): #Para cada evento que ocurra, se obtiene el evento en proceso
            #Si el usuario cierra la ventana
            if event.type == pygame.QUIT:
                self.running = False #Es decir, se cambia la varible True 'Linea31' a False

    def update(self): 
        #Actualiza las funciones del juego según las teclas presionadas
        keys = pygame.key.get_pressed () #Para saber las teclas que presiona el usuario
        
        #Calcula el moviento según las teclas presionadas
        dx = keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]    #Delta "x" es la diferencia entre tecla "derecha" menos tecla "izquierda"
        dy = keys[pygame.K_DOWN] - keys[pygame.K_UP]    #Delta "y" es la diferencia entre tecla "abajo" menos tecla "arriba"

        #Mover el jugador:
        self.player.move(dx, dy)


    def draw(self): #Dibujar los elementos en la pantalla
        #Base de la pantalla de color negro
        self.screen.fill (negro)

        #Dibuja al jugador:
        self.player.draw(self.screen) 

        #Actualizar la pantalla
        pygame.display.flip() 

    def run(self): #Bucle principal del juego cuando se llame 'run'
        while self.running: 
            self.handleEvents () #Procesar los eventos
            self.update () #Actualizar el estado del juego
            self.draw () #Dibujar los elementos que están en el juego
            self.clock.tick (60) #60FPS


