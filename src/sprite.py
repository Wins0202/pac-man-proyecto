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
        self.originalmagen = pygame.Surface ((16, 16), pygame.SRCALPHA) #size: 16x16 tamaño de la imagen y uso de transparencia en la imagen y no le coloque un fondo
        self.originalmagen.blit (self.sprite_sheet, dest=(0, 0), area=(96, 0, 16, 16))   # Se toma el septimo frame de la imagen 6*16=96 en el eje "x" y 0 e el eje "y"
        self.originalmagen = pygame.transform.scale(self.originalmagen, size=(tamañoPersonaje, tamañoPersonaje)) #Coloca a imagen a la escala que previamente habiamos definido 

        #Imagen actual del jugador
        self.image = self.originalmagen     #Cuando se vaya a la derecha se quede la imagen original

        #Creación del espacio-rectángulo del jugador:
        self.rect = self.image.get_rect(center=(self.x, self.y))   #Se centrará en el eje "x" e "y" la imagen que se le definió el tamaño

        #Dirección actual (0: derecha, 1: izquierda)
        self.direction = 0   #Predetermina que cuando empieze el juego se mueva a la derecha
        self.flipped = False #La imagen no va a estar volteada 

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

        #Actualizar imagen en el movimiento:
            #Movimiento en horizontal
        if dx > 0 and self.direction != 0:    #Si la dirección es distinta de 0
            self.direction = 0                #Irá a la derecha
            self.image = self.originalmagen   #La imagen será la original
            self.flipped = False              #No se girará la imagen
        elif dx < 0 and self.direction != 1:    #Si la dirección es distinta de 1
            self.direction = 1                  #Irá a la izquierda
            self.image = pygame.transform.flip (self.image, flip_x=True, flip_y=False)  #La imagen que se mostrará será volteada
            self.flipped = True                 #Se volteará la imagen

         #Movimiento en vertical:
        elif dy < 0 and self.direction != 2:    #Si se dirige hacia arriba
            self.direction = 2      
            self.image = pygame.transform.rotate (self.originalmagen, angle = 90)   #Se girará la imagen 90 grados
            self.flipped = True
        elif dy > 0 and self.direction != 3:    #Si se dirige hacia abajo
            self.image = pygame.transform.rotate (self.originalmagen, angle = -90)  #Se girará la imagen -90 grados
            self.flipped = True
            
    def draw(self, screen):
        #Dibujar al pac-man en pantalla:
        screen.blit (self.image, self.rect) #El dibujo será rectángular pero tendrá la imagen agregada















