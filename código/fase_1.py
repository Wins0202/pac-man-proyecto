""" Programa creado como proyecto para el módulo de IDME. En este proyecto está plasmada la 
creación del código del tradicional juego arcade de Pac-Man."""


#Importación de librerías:

import pygame #Libreria con la que programa el juego. 

import sys #Cuando se cierre la ventana deje de correr la aplicación.

from confi_ventana import * #desde la pestaña creada, importamos todo lo que esté allí escrito.

"""Para la correcta importación de la librería se tiene que descargar con el comando 
"pip install pygame" y se procederá a descargar la librería para su uso"""


"""Este conjunto de líneas sirve para que se inicie el juego. Definiremos las funciones para el ´
control básico del juego"""

#Definición de variables:

class Game:
    def __init__ (self): 
        #Se activa pygame:
        pygame.init() 
    
        #Se crea la ventana:
        self.screen = pygame.display.set_mode ((screenWidth, screenHeight)) #activa el ancho y el alto de la ventana que se había importado de la pestaña creada
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
        pass #no hay que actulizar, así que se deja en "reposo"




