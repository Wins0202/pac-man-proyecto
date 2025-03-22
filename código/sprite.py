""" -------------------------------------------------------------------------------
    ||||||Desarrollo de todos los elementos gráficos y móviles dentro del juego||||||
    ------------------------------------------------------------------------------"""

#Importación de librerías:
from config import *

import pygame



"""Sirve para definir las acciones que puede realizar o que le pueden ocurrir al jugador"""
class Player:
    def __init__(self):
        #Posición inicial del jugador (centro de la pantalla):
        self.x = width // 2     #En el eje "x" el personaje está a la mitad del eje
        self.y = height // 2    #En el eje "y" el personaje está a la mitad del eje

        #Creación del espacio-rectángulo del jugador:
        self.rect = pygame.Rect(      
            self.x - tamañoPersonaje // 2,  #Centro del rectángulo en la cordena "x" menos el tamaño divido entre 2
            self.x - tamañoPersonaje // 2,  #Centro del rectángulo en la cordena "y" menos el tamaño divido entre 2
            tamañoPersonaje,
            tamañoPersonaje
        )   

    def move (self, dx, dy):    
        #Movimiento del pac-man según la entrada el jugador
        #Actualizar la posición:
        self.x += dx * velocidadPersonaje  #Coordenada del eje "x" se le suma el delta"x"(dx) por la velocidad del jugador
        self.y += dy * velocidadPersonaje  #Coordenada del eje "x" se le suma el delta"y"(dy) por la velocidad del jugador

        #Actualizar el rectángulo:
        self.rect.center = (self.x, self.y) #el nuevo "self.x y" el nuevo "self.y" es la nueva posición

    def draw(self, screen):
        #Dibujar al pac-man en pantalla:
        pygame.draw.rect (screen, amarillo, self.rect)
















