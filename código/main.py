""" Programa creado como proyecto para el módulo de IDME. En este proyecto está plasmada la 
creación del código del tradicional juego arcade de Pac-Man."""


#Importación de librerías:

import pygame #Libreria con la que programa el juego. 

import sys #Cuando se cierre la ventana deje de correr la aplicación.

from config import * #Importación de la librería creada para las configuraciones

"""Para la correcta importación de la librería se tiene que descargar con el comando 
"pip install pygame" y se procederá a descargar la librería para su uso"""


"""Este conjunto de líneas sirve para que se inicie el juego. Definiremos las funciones para el
control básico del juego"""

"""Configuración de la ventana donde se va a visualizar el juego"""


#Definición de variables:

class Game:
    def __init__ (self): 
        #Se activa pygame:
        pygame.init() 
    
        #Se crea la ventana:
        self.screen = pygame.display.set_mode ((width, height)) #activa el ancho y el alto de la ventana que se había importado de la pestaña creada
        pygame.display.set_caption ("PAC-MAN") #Nombre que tendrá la ventanilla cuando se abrá para jugar

        #Se establece un reloj para controlar la velocidad del juego
        self.clock = pygame.time.Clock ()

        #Se crea una variable para el bucle del juego
        self.running = True

    def handleEvents (self):
        #Manejar los eventos (función de las teclas en pygame)
        for event in pygame.event.get (): #Para cada evento que ocurra, se obtiene el evento en proceso
            #Si el usuario cierra la ventana
            if event.type == pygame.QUIT:
                self.running = False #Es decir, se cambia la varible True 'Linea31' a False

    def update(self): 
        #Actualizará las funciones del juego
        pass #no hay que actualizar, así que se deja en "reposo"

    def draw(self): #Dibujar los elementos en la pantalla
        #La base de la pantalla es color negro
        self.screen.fill (negro)

        pygame.display.flip() #Actualizar la pantalla sino no se observa

    def run(self): #Bucle principal del juego cuando se llame 'run'
        while self.running: 
            self.handleEvents () #Procesar los eventos
            self.update () #Actualizar el estado del juego
            self.draw () #Dibujar los elementos que están en el juego
            self.clock.tick (60) #60FPS

        pygame.quit() #Cerrar pygame al terminar
        sys.exit() 


#Creación y ejecución del juego:
if __name__ == "__main__" : #si lo ejecutamos sólo se va a ejecutar este archivo
        game = Game ()          #Si ejecutamos desde otro archivo que no sea "Game" no va a correr
        game.run ()             #Es el que llama a todos los eventos del 

