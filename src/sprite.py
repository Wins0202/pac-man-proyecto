""" -------------------------------------------------------------------------------
    ||||||Desarrollo de todos los elementos gráficos y móviles dentro del juego||||||
    ------------------------------------------------------------------------------"""

#Importación de librerías:
from config import *

import pygame


"""Sirve para definir las acciones que puede realizar o que le pueden ocurrir a las paredes"""
class Wall:
    def __init__(self, x, y):
        #Definición del tamaño de la celda dentro de la pantalla de juego
        self.rect = pygame.Rect (x * celdaTamaño, y * celdaTamaño, celdaTamaño, celdaTamaño) 

    def draw (self, screen):
        #Dibujar la pared en la pantalla
        pygame.draw.rect(screen, colorPared, self.rect)




"""Sirve para definir las acciones que puede realizar o que le pueden ocurrir al jugador"""
class Player:
    def __init__(self, x, y):
        #Posición inicial del jugador (centro de la pantalla):
        self.x = x * celdaTamaño + celdaTamaño // 2     #En el eje "x" el personaje está a la mitad del eje
        self.y = y * celdaTamaño + celdaTamaño // 2    #En el eje "y" el personaje está a la mitad del eje

        #Cargar imagen de pacman
        self.sprite_sheet = cargarImagen ("PacMan.png") #Carga una imagen desde la carpeta sprite
 
        #Cargar todos los frames para animar:
        self.framesAnimados = []
        for i in range (numeroFrames):
            #Creación de superficie para los frames
            frame = pygame.Surface ((16, 16), pygame.SRCALPHA)
            #Copiar el frame del sprite sheet:
            frame.blit(self.sprite_sheet, dest = (0, 0), area =(i * 16, 0, 16, 16)) #Dependiendo de lo que valga "i" tomará la imagen del sprite y se multiplicará para dar tamaño
            #Poner a escala la imagen:
            frame = pygame.transform.scale (frame, size = (tamañoPersonaje, tamañoPersonaje))   #Se ponen a escala todos los frames
            self.framesAnimados.append (frame) #Se le agrega a la variable "framesAnimados" la variable "frame"

        #Variables de la animación:
        self.frameActual = 0    #El frame "0" será la primera imagen del "sprite sheet"
        self.timerAnimacion = pygame.time.get_ticks () #Cuando llegue a los 100 milisegundos se cambien al siguiente frame
        self.movimiento = False #Para que no cambie de frame cuando esté quieto
    
        #Imagen actual del jugador
        self.originalImagen = self.framesAnimados [0]  #Cuando se vaya a la derecha se quede la imagen original
        self.image = self.originalImagen

        #Creación del espacio-rectángulo del jugador:
        self.rect = self.image.get_rect(center=(self.x, self.y))   #Se centrará en el eje "x" e "y" la imagen que se le definió el tamaño

        #Dirección actual:
        self.direction = derecha   #Predetermina que cuando empieze el juego se mueva a la derecha
        
        #Deltas:
        self.dx = 0
        self.dy = 0

    def updateAnimation (self):
        #Actualiza el frame de animación:
        if not self.movimiento:     #Si no está en movimiento no se debe mover
            self.frameActual = 0
            return

        tiempoActual = pygame.time.get_ticks ()
        if tiempoActual - self.timerAnimacion > velocidadAnimacion: #mayor a 100 milisegundos
            self.frameActual =(self.frameActual + 1) % numeroFrames
            self.timerAnimacion = tiempoActual

    def updateImage (self):
       #Actualizar la imagen según la dirección y frame
            #Obtener frame actual:
        self.originalImagen = self.framesAnimados [self.frameActual] 

        #Actualizar imagen en el movimiento:
            #Movimiento en horizontal
        if self.dx > 0:    #Si la dirección es distinta de 0
            self.direction = derecha                #Irá a la derecha
            self.image = self.originalImagen   #La imagen será la original
        elif self.dx < 0:    #Si la dirección es distinta de 1
            self.direction = izquierda                  #Irá a la izquierda
            self.image = pygame.transform.flip (self.originalImagen, flip_x=True, flip_y=False)  #La imagen que se mostrará será volteada

         #Movimiento en vertical:
        elif self.dy < 0:    #Si se dirige hacia arriba
            self.direction = arriba      
            self.image = pygame.transform.rotate (self.originalImagen, angle = 90)   #Se girará la imagen 90 grados
        elif self.dy > 0:    #Si se dirige hacia abajo
            self.direction = abajo
            self.image = pygame.transform.rotate (self.originalImagen, angle = -90)  #Se girará la imagen -90 grados

    def move (self, walls):    
        #Movimiento del pac-man según la entrada del jugador
        #Guardar la posición anterior 
        antX = self.x
        antY = self.y

         #Actualizar la posición:
        self.x += self.dx  #Coordenada del eje "x" se le suma el delta"x"(dx) por la velocidad del jugador
        self.y += self.dy  #Coordenada del eje "x" se le suma el delta"y"(dy) por la velocidad del jugador

        #Actualizar el rectángulo:
        self.rect.center = (self.x, self.y) #el nuevo "self.x y" el nuevo "self.y" es la nueva posición

        #Comprobación de colisión con paredes
        for wall in walls:
            if self.rect.colliderect(wall.rect):   
                #Si hay una colisión, volver a la posición anterior
                self.x = antX
                self.y = antY
                self.rect.center = (self.x, self.y)
                break
            
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


    def handleInput (self):
        #Unir la entrada del usuario con velocidad actualizada
        keys = pygame.key.get_pressed ()

        #Reiniciar la velocidad
        self.dx = 0
        self.dy = 0

        #Actualiza las funciones del juego según las teclas presionadas
            #Si la tecla es presionada a la derecha
        if keys [pygame.K_RIGHT]:
            self.dx = velocidadPersonaje
            self.direction = derecha
            #Si la tecla es presionada a la izquierda
        elif keys[pygame.K_LEFT]:
            self.dx = - velocidadPersonaje
            self.direction = izquierda
            #Si la tecla es presionada hacia arriba
        elif keys [pygame.K_UP]:
            self.dy = - velocidadPersonaje
            self.direction = arriba
            #Si la tecla es presionada hacia abajo
        elif keys [pygame.K_DOWN]:
            self.dy = velocidadPersonaje
            self.direction = abajo

        #Actualizar el estado de movimiento:
        self.movimiento = self.dx != 0 or self.dy != 0      #Se está moviendo si cualquiera de los deltas es distinto a 0
            
    def checkCollision (self, walls, dx=0, dy=0):
        #Comprobar si hay colisión en una posición futura
            #Creación de rectángulo temporal en la posición futura
            futuroRect = self.rect.copy()   #Es una copia del rect que ya se tiene
            futuroRect.x += dx
            futuroRect.y += dy 

        #Comprobar colisión con cada pared
            for wall in walls:
                #Si el rect colisiona con alguna pared
                if futuroRect.colliderect (wall.rect):
                    return True
            return False
        
    


    def update (self, walls):
        self.handleInput ()
        self.updateAnimation ()    #Actualizar animación
        self.updateImage ()        #Actualizar imagen
        self.move (walls)           #Se actualiza el jugador y las paredes 

    def draw(self, screen):
        #Dibujar al pac-man en pantalla:
        screen.blit (self.image, self.rect) #El dibujo será rectángular pero tendrá la imagen agregada















