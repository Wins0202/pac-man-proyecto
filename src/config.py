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
negro = (0, 0, 0)  
blanco = (255, 255, 255)
amarillo = (255, 195, 0)    #Color del Pac-man


#Configuración del jugador
tamañoPersonaje = 24     #Tamaño en pixeles que tiene Pac-man
velocidadPersonaje = 5   #Velocidad de movimiento del personaje
velocidadAnimacion = 50 #Velocidad de animación de 100 milisegundos entre cada frame
numeroFrames = 8         #Número total de frames en el sprite


#Configuración de las paredes
celdaTamaño = 32            #Tamaño de cada celda del laberinto
colorPared = (131, 185, 255)  #Color rosa para las paredes


#Configuración de las colisiones
toleranciaColision = 4  #Pixeles de tolerancia para colisiones
deslizamiento = 2       #Velocidad de deslizamiento en las paredes

nivel = [
    "1111111111111101111111111",
    "1000000000000000000000001",
    "1011111111101010000111101",
    "1000000001111111100000001",
    "1011100000000001111111101",
    "1000111110001110000000001",         #Tiene una P porque es el punto de partida
    "1011110000111100010111101",
    "0000000000000000000000000",
    "1011111000000001111111101",
    "1000000111010101000000001",
    "1111111111110000000111111",
    "1000111110001110000000001",        
    "1011110000111100010111101",
    "10000000000P0000000000001",
    "1011111000000001111111101",
    "1000000111010101000000001",
    "1000000111010101000000001",
    "1111110000000000000111111",
    "1111111111111101111111111"
    ]


#Función para cargar imágenes
def cargarImagen (name):
    return pygame.image.load (os.path.join("assets", "images", name)).convert_alpha()

#Direcciones
derecha = 0
izquierda = 1
arriba = 2
abajo = 3


