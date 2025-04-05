""" -------------------------------------------------
    ||||||Código para activar y cerrar el juego||||||
    -------------------------------------------------"""


import pygame #Libreria con la que se programa el juego. 

import sys #Cuando se cierre la ventana deje de correr la aplicación.

from game import Game #Se importa la clase "Game"


#Definición del programa:
def main ():
    try:
        #Se activa pygame
        pygame.init()           #Imágenes
        pygame.mixer.init()     #Sonidos

        #crear y correr el juego
        game = Game() 
        game.run () #Ejecuta el juego

    except Exception as e:  #Se ejecutará el juego excepto si ocurre algún fallo en él
        print (f"Error: {e}")   #Escribirá cuál es el error que ha sucedido
        sys.exit(1) #Se dejará de ejecutar el programa

    finally: #Cuando se deje de ejecutar "try" se saldrá del programa
        pygame.quit()   #Se cerrará el juego
        sys.exit()

if __name__ == "__main__" :
    main ()