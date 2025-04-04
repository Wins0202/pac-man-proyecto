""" -------------------------------------------------------------------------------
    ||||||Desarrollo de todos los elementos gráficos y móviles dentro del juego||||||
    ------------------------------------------------------------------------------"""

#Importación de librerías:
from config import *

import pygame

import random



"""Sirve para definir las acciones que puede realizar o que le pueden ocurrir a las paredes"""
class Wall:
    def __init__(self, x, y):
        #Definición del tamaño de la celda dentro de la pantalla de juego
        self.rect = pygame.Rect (x * celdaTamaño, y * celdaTamaño, celdaTamaño, celdaTamaño) 

    def draw (self, screen):
        #Dibujar la pared en la pantalla
        pygame.draw.rect(screen, colorPared, self.rect)



"""Sirve para definir las acciones que puede realizar o que le pueden ocurrir a las monedas"""
class Coin:
    def __init__(self, x, y):
        #Posición de la moneda 
        self.x = x * celdaTamaño + celdaTamaño // 2     #En el eje "x" la moneda está a la mitad del eje
        self.y = y * celdaTamaño + celdaTamaño // 2     #En el eje "y" la moneda está a la mitad del eje

        #Cargar sprite sheet de la moneda
        self.sprite_sheet = cargarImagen ("Coin.png") #Carga una imagen desde la carpeta sprite

        #Cargar todos los frames para animar:
        self.frames = []
        for i in range (monedaFrames):
            #Creación de superficie para los frames
            frame = pygame.Surface ((16, 16), pygame.SRCALPHA)
            #Copiar el frame del sprite sheet:
            frame.blit(self.sprite_sheet, dest = (0, 0), area =(i * 16, 0, 16, 16)) #Dependiendo de lo que valga "i" tomará la imagen del sprite y se multiplicará para dar tamaño
            #Poner a escala la imagen:
            frame = pygame.transform.scale (frame, size = (monedaTamaño, monedaTamaño))   #Se ponen a escala todos los frames
            self.frames.append (frame) #Se le agrega a la variable "frames" la variable "frame"

        #Variables de la animación:
        self.frameActual = 0    #El frame "0" será la primera imagen del "sprite sheet"
        self.timerAnimacion = pygame.time.get_ticks() #Cuando llegue a los 100 milisegundos se cambien al siguiente frame
        
        #Rectángulo para colisión
        self.rect = self.frames [0].get_rect(center=(self.x, self.y))

    def update (self):
        tiempoActual = pygame.time.get_ticks ()
        if tiempoActual - self.timerAnimacion > monedaAnimacion: #mayor a 100 milisegundos
            self.frameActual =(self.frameActual + 1) % monedaFrames
            self.timerAnimacion = tiempoActual

    def draw (self, screen):
        #Dibujar la moneda en pantalla
        screen.blit (self.frames[self.frameActual], self.rect)


"""Sirve para definir las acciones que puede realizar o que le pueden ocurrir a los fantasmas"""
class Ghost:
    def __init__(self, x, y, fantasmaTipo):
        #Posición inicial del jugador (centro de la pantalla):
        self.x = x * celdaTamaño + celdaTamaño // 2     #En el eje "x" el fantasma está a la mitad del eje
        self.y = y * celdaTamaño + celdaTamaño // 2     #En el eje "y" el fantasma está a la mitad del eje

        #Tipo de fantasma y sus características
        self.fantasmaTipo = fantasmaTipo                            #Define el tipo de fantasma
        self.speed = fantasmaVelocidad [fantasmaTipo]               #Degine la velocidad de ese tipo de fantasma
        self.direccionCambio = fantasmaDireccion [fantasmaTipo]     #Define el tiempo que tarda en cambiar de dirección

        #Cargar sprite sheet del fantasma
        self.sprite_sheet = cargarImagen (ghostSprites [fantasmaTipo]) #Carga una imagen desde la carpeta sprite

         #Cargar todos los frames para animar:
        self.frames = []
        for i in range (fantasmaFrame):
            #Creación de superficie para los frames
            frame = pygame.Surface ((16, 16), pygame.SRCALPHA)
            #Copiar el frame del sprite sheet:
            frame.blit(self.sprite_sheet, dest = (0, 0), area =(i * 16, 0, 16, 16)) #Dependiendo de lo que valga "i" tomará la imagen del sprite y se multiplicará para dar tamaño
            #Poner a escala la imagen:
            frame = pygame.transform.scale (frame, size = (fantasmaTamaño, fantasmaTamaño))   #Se ponen a escala todos los frames
            self.frames.append (frame) #Se le agrega a la variable "frames" la variable "frame"

        #Variables de la animación:
        self.frameActual = 0    #El frame "0" será la primera imagen del "sprite sheet"
        self.timerAnimacion = pygame.time.get_ticks () #Cuando llegue a los 100 milisegundos se cambien al siguiente frame
       
        #Variables de movimiento
        self.direction = random.randint (0, 3)  #Dara una dirección random entre lasdirecciones "0" siendo derecha y "3" abajo
        self.direccionTimer = pygame.time.get_ticks ()
        self.rect = self.frames [0].get_rect(center=(self.x, self.y)) 

    def getNextDirection (self):
        #Determinar la siguiente dirección según el tipo de fantasma
        if self.fantasmaTipo == "rojo":
            #Fantasma rojo elige una dirección aleatoria
            return random.randint(0, 3)
        elif self.fantasmaTipo == "blue":
            #Fantasma azul alterna entre horizontal y vertical
            if self.direction in [derecha, izquierda]:      #No irá hacia atrás, elige entre arriba y abajo cuando eliga entre derch o izq 
                return random.choice([arriba, abajo])
            else:
                return random.choice ([derecha, izquierda])
        elif self.fantasmaTipo == "naranja":
            #Fantasma naranja se mueve en sentido horario
            return (self.direction + 1)% 4
        else:
            #Fantasma verde se mueve en sentido antihorario
            return (self.direction - 1) % 4
        
        

    def changeDirection (self, walls):
        #Cambiar la dirección del fantasma según su tipo
        if self.fantasmaTipo == "rojo":
            #El rojo prueba todas las direcciones hasta encontrar una valida
            direcciones = list(range(4))
            random.shuffle (direcciones)                #Elige alguna de las 4 direcciones
            for nuevaDir in direcciones:                #Comprueba si se puede mover en esa dirección
                if self.puedeMoverse (nuevaDir, walls):
                    self.direction = nuevaDir           #Si sí se puede mover, se dirige a ella
                    break
        
        else:
            #Los demás fantasmas siguen su patrón especifico
            nuevaDir = self.getNextDirection ()
            if self.puedeMoverse (nuevaDir, walls):
                self.direction = nuevaDir
            else:
                #Si no pueden moverse en la dirección deseada, eligen aleatoria
                self.direction = random.randint(0, 3)
        
        self.direccionTimer = pygame.time.get_ticks ()

    def puedeMoverse (self, direction, walls):
        #Comprobar si el fantasma puede moverse en esa dirección
        dx = dy = 0
        if direction == derecha:
            dx = self.speed
        elif direction == izquierda:
            dx = -self.speed
        elif direction == arriba:
            dy = -self.speed
        elif direction == abajo:
            dy = self.speed

        #Prueba si se puede mover derecha o izquierda, arriba o abajo
        testRect = self.rect.copy ()   
        testRect.x += dx
        testRect.y += dy

        #Comprueba si existe alguna colisión con las paredes
        for wall in walls:
            if testRect.colliderect (wall.rect):
                return False                        #No se puede mover si se choca contra paredes
        return True                                 #Se mueve si no hay choque con paredes

    def move (self, walls):
        #Mover fantasma y manejar colisiones
        #Cambiar dirección después de cierto tiempo
        tiempoActual = pygame.time.get_ticks ()
        if tiempoActual - self.direccionTimer > self.direccionCambio: #mayor a 2000 milisegundos
            self.changeDirection (walls)

        #Calcular movimiento según la dirección
        dx = dy = 0
        if self.direction == derecha:
            dx = self.speed
        elif self.direction == izquierda:
            dx = -self.speed
        elif self.direction == arriba:
            dy = -self.speed
        elif self.direction == abajo:
            dy = self.speed


         #Comprobar colisión en la nueva posición
        nuevoRect = self.rect.copy ()
        nuevoRect.x += dx
        nuevoRect.y += dy 

        #Si hay colisión, cambia dirección
        moverse = True
        for wall in walls:
            if nuevoRect.colliderect (wall.rect):   #Si el nuevoRect colisiona con alguna de las paredes
                moverse = False
                self.changeDirection(walls)              #Se cambia de posición
                break

        #Si no hay colisión, se actualiza la posición
        if moverse:
            self.x += dx
            self.y += dy
            self.rect.center = (self.x, self.y)     #Se actualiza la posición enre el eje X y el eje Y

         #Mantener al jugador dentro de la pantalla:
            #Moviemiento horizontal
        if self.x > width - fantasmaTamaño: 
            self.x = 0                       #Si el personaje entra por el lado derecho saldra por el lado izquierdo
        elif self.x < 0:                       
            self.x = width - fantasmaTamaño #Si el personaje sale por el lado izquierdo entrará por el lado derecho
        
            #Movimiento vertical
        if self.y > height - fantasmaTamaño:
            self.y = 0                          #Si el personaje sale por abajo, entrará por arriba
        elif self.y < 0:
            self.y = height - fantasmaTamaño   #Si el personaje sale por arriba entrará por abajo



    def update (self, walls):
        #Actualizar estado del fantasma
        #Actualizar animación:
        tiempoActual = pygame.time.get_ticks ()
        if tiempoActual - self.timerAnimacion > fantasmaAnimación:
            self.frameActual =(self.frameActual + 1) % fantasmaFrame
            self.timerAnimacion = tiempoActual

        #Actualizar movimiento
        self.move (walls)

    def draw (self, screen):
        #Dibujar al fantasma en pantalla
        screen.blit (self.frames[self.frameActual], self.rect)




"""Sirve para definir las acciones que puede realizar o que le pueden ocurrir al jugador"""
class Player:
    def __init__(self, x, y):
        #Posición inicial del jugador (centro de la pantalla):
        self.x = x * celdaTamaño + celdaTamaño // 2     #En el eje "x" el personaje está a la mitad del eje
        self.y = y * celdaTamaño + celdaTamaño // 2     #En el eje "y" el personaje está a la mitad del eje

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
        if self.dx > 0:                              #Si la dirección es distinta de 0
            self.direction = derecha                 #Irá a la derecha
            self.image = self.originalImagen         #La imagen será la original
        elif self.dx < 0:                            #Si la dirección es distinta de 1
            self.direction = izquierda               #Irá a la izquierda
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
            if futuroRect.colliderect (wall.rect): #Si el rect colisiona con alguna pared
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















