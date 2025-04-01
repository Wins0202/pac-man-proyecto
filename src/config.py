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
tamañoPersonaje = 30     #Tamaño en pixeles que tiene Pac-man
velocidadPersonaje = 5   #Velocidad de movimiento del personaje
velocidadAnimacion = 50 #Velocidad de animación de 100 milisegundos entre cada frame
numeroFrames = 8         #Número total de frames en el sprite

#Función para cargar imágenes
def cargarImagen (name):
    return pygame.image.load (os.path.join("assets", "images", name)).convert_alpha()

#Direcciones
derecha = 0
izquierda = 1
arriba = 2
abajo = 3

#Configuración de las paredes
celdaTamaño = 32            #Tamaño de cada celda del laberinto
colorPared = (250, 0, 255)  #Color rosa para las paredes

nivel = [
    "111111111111",
    "100000000001",
    "101111111101",
    "100000000001",
    "101111111101",
    "100P00000001",         #Tiene una P porque es el punto de partida
    "101111111101",
    "100000000001",
    "101111111101",
    "100000000001",
    "111111111111"
]
