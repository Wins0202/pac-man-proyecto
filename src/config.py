""" -------------------------------------------------------------------------
    ||||||Configuración de la ventana donde se va a visualizar el juego||||||
    -------------------------------------------------------------------------"""
import pygame   #Librería de programación de juegos
import os       #Librería para trabajar con el sistema operativo

#Definción del tamaño de la pantalla
width = 800     #Ancho de la ventana
height = 600    #Altura de la ventana


#Configuración de colores
"""Los colores son tomados del código de colores en RGB"""
negro = (199, 21, 133)  
blanco = (255, 255, 255)
amarillo = (255, 215, 0)   
rojo = (219, 112, 147)
azul = (219, 112, 147)
negrito = (0, 0, 0)


#Configuración del jugador
tamañoPersonaje = 23     #Tamaño en pixeles que tiene Pac-man
velocidadPersonaje = 5   #Velocidad de movimiento del personaje
velocidadAnimacion = 50 #Velocidad de animación de 100 milisegundos entre cada frame
numeroFrames = 8         #Número total de frames en el sprite


#Configuración de lo fantasmas
fantasmaTamaño = 25         #Tamaño del sprite del fantasma
fantasmaFrame = 8           #Número de frmes de animación del fantasma
fantasmaAnimación = 150     #Velocidad de animación del fantasma

#Velocidades de los fantasmas
fantasmaVelocidad = {
    "rojo": 3,          #El más rápido, persigue directamente
    "azul": 2,          #Velocidad media, movimiento errático
    "naranja": 2,       #Velocidad media, movimiento circular
    "verde": 1          #El más lento, movimiento predecible
}

#Tiempos para el cambio de dirección de los fantasmas
fantasmaDireccion = {
    "rojo": 2000,          #Cambia de dirección cada 2 segundos
    "azul": 3000,          #Cambia de dirección cada 3 segundos
    "naranja": 4000,       #Cambia de dirección cada 4 segundos
    "verde": 5000          #Cambia de dirección cada 5 segundos
} 

#Nombre de los archivos-imagen de los fantasmas
ghostSprites = {
    "rojo": "redGhost.png",          #Cambia de dirección cada 2 segundos
    "azul": "blueGhost.png",          #Cambia de dirección cada 3 segundos
    "naranja": "orangeGhost.png",       #Cambia de dirección cada 4 segundos
    "verde": "greenGhost.png"
}

#Configuración de las paredes
celdaTamaño = 32            #Tamaño de cada celda del laberinto
colorPared = (255, 192, 203)  #Color rosa para las paredes


#Configuración de las monedas
monedaTamaño = 16       #Tamaño de las monedas
monedaAnimacion = 200   #Velocidad de animación de las monedas
monedaFrames = 8        #Número de frames de animación de las monedas
puntoMoneda = 10        #Puntos ganados por cada moneda

#Estados del juego
playing = "playing"
gameOver = "gameOver"
intro = "intro"

#Direcciones
derecha = 0
izquierda = 1
arriba = 2
abajo = 3

nivel = [
    "1111111111111100000000011",
    "100R000000000000000000001",
    "1011111111101010000111101",
    "1000000001111111100000001",
    "1011100000000001111111101",
    "1000111110001110000000001",         #Tiene una P porque es el punto de partida
    "1011110000111100010111101",
    "0000000A00000000000000000",
    "1011111000000001111111101",
    "1000000111010101000000001",
    "1111111111110000000111111",
    "1000111110001110000000001",        
    "1011110000111100010111101",
    "1000000000000000000000001",
    "10111110000P0001111111101",
    "100000011101010100000N001",
    "1000000111010101000000001",
    "11111100V0000000000111111",
    "1111111111111100000000111"
    ]


#Función para cargar imágenes
def cargarImagen (name):
    return pygame.image.load (os.path.join("assets", "images", name)).convert_alpha()




"""Esta configuración no se van a usar porque el código funciona muy rápido con ese trozo de codigo en "move"
 #Movimiento en X:

        if self.dx != 0:
            #Comprueba la colisión en x
            if not self.checkCollision(walls, dx=self.dx, dy=0):
                #Si no hay colision, se moverá a esa posición
                self.x += self.dx
            else:
                #Deslizarse verticalmente si hay colisión
                if self.checkCollision (walls, self.dx, -deslizamiento):        #Se desplaza hacia arriba
                    if not self.checkCollision (walls, self.dx, deslizamiento): #Se desplaza hacia abajo
                        self.y += deslizamiento
                else:
                    self.y -= deslizamiento
        #Movimiento en Y:
        if self.dy != 0:   
            #Comprueba la colisión en Y
            if not self.checkCollision (walls, dx=0, dy=self.dy):
                #Si no hay colisión se moverá en esa posición
                self.y += self.dy
            else:
                #Deslizarse horizontalemente si hay colisión
                if self.checkCollision (walls, -deslizamiento, self.dy):        
                    if not self.checkCollision (walls, deslizamiento, self.dy): 
                        self.x += deslizamiento
                else:
                    self.x -= deslizamiento"""
#Configuración de las colisiones
toleranciaColision = 4  #Pixeles de tolerancia para colisiones
deslizamiento = 2       #Velocidad de deslizamiento en las paredes
