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

        #Cargar imagen de pacman
        self.sprite_sheet = cargarImagen ("PacMan.png") #Carga una imagen desde la carpeta sprite
 
        #Obtener el primer frame (mirando hacia la derecha)
        self.image = pygame.Surface ((16, 16), pygame.SRCALPHA) #size: 16x16 tamaño de la imagen y uso de transparencia en la imagen y no le coloque un fondo
        self.image.blit (self.sprite_sheet, dest=(0, 0), area=(0, 0, 16, 16))   # Se toma el primer frame desde la coordeada 0 de la imagen se obtiene el primer frame y los que les sigue
        self.image = pygame.transform.scale(self.image, size=(tamañoPersonaje, tamañoPersonaje)) #Coloca a imagen a la escala que previamente habiamos definido 

        #Creación del espacio-rectángulo del jugador:
        self.rect = self.image.get_rect(center=(self.x, self.y))   #Se centrará en el eje "x" e "y" 

    def move (self, dx, dy):    
        #Movimiento del pac-man según la entrada el jugador
            #Actualizar la posición:
        self.x += dx * velocidadPersonaje  #Coordenada del eje "x" se le suma el delta"x"(dx) por la velocidad del jugador
        self.y += dy * velocidadPersonaje  #Coordenada del eje "x" se le suma el delta"y"(dy) por la velocidad del jugador

        #Mantener al jugador dentro de la pantalla:
            #Moviemiento horizontal
        if self.x > width - tamañoPersonaje: 
            self.x = 0                       #Si el personaje entra por el lado derecho saldra por el lado izquierdo
        elif self.x < 0:                       
            self.x = width - tamañoPersonaje #Si el personaje sale por el lado izquierdo entrará por el lado derecho
        
            #Movimiento vertical
        if self.y > height - tamañoPersonaje:
            self.y = 0                          #Si el personaje sale por abajo, entrará por arriba
        elif self.y < 0:
            self.y = height - tamañoPersonaje   #Si el personaje sale por arriba entrará por abajo

        #Actualizar el rectángulo:
        self.rect.center = (self.x, self.y) #el nuevo "self.x y" el nuevo "self.y" es la nueva posición

    def draw(self, screen):
        #Dibujar al pac-man en pantalla:
        screen.blit (self.image, self.rect) #El dibujo será rectángular pero tendrá la imagen agregada















