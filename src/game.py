""" Programa creado como proyecto para el módulo de IDME. En este proyecto está plasmada la 
creación del código del tradicional juego arcade de Pac-Man."""



""" ------------------------------------------------------
    ||||||Desarrollo de la clase "GAME" (class Game)||||||
    ------------------------------------------------------"""


#Importación de librerías:

import pygame #Libreria con la que se programa el juego. 
"""Para la correcta importación de la librería se tiene que descargar con el comando 
"pip install pygame" y se procederá a descargar la librería para su uso"""

from config import * #Importación de la librería creada para las configuraciones

from sprite import * #Importación de la librería creada para los movimientos


"""Este conjunto de líneas sirve para que se inicie el juego. Definiremos las funciones para el
control básico del juego"""
#Definición de variables:

class Game:
    def __init__ (self): 
    
        #Se crea la ventana:
        self.screen = pygame.display.set_mode ((width, height)) #activa el ancho y el alto de la ventana que se había importado de la pestaña creada
        pygame.display.set_caption ("PAC-MAN") #Nombre que tendrá la ventanilla cuando se abrá para jugar

        #Se establece un reloj para controlar la velocidad del juego
        self.clock = pygame.time.Clock ()

        #Se crea una variable para el bucle del juego
        self.running = True
        self.estadoJuego = playing      #Iniciará el juego y cuando cambie a "GAMEOVER" lo terminará

        #Se crea paredes, monedas y jugador:
        self.walls = []
        self.coins = []
        self.player = None
        self.ghosts = []
        self.score = 0
        self.createLevel ()

        #Fuente para el texto de los puntos
        self.font = pygame.font.Font (None, 36)

    def createLevel(self):
        #Creación del nivel a partir del diseño en "config"
        for row_index, row in enumerate (nivel):       #Ennumerar filas
            for col_index, cell in enumerate (row):      #Ennumerar columnas
                if cell == "1":
                    self.walls.append (Wall(col_index, row_index))  #Cuando en la celda sea "1" se crea una pared
                elif cell == "0":
                    self.coins.append (Coin(col_index, row_index))  #Cuando la celdda sea "0" se crean monedas
                elif cell == "P":
                    self.player = Player(col_index, row_index)       #Cuando en la celda sea "P" se crea el jugador
                elif cell == "R":
                    self.ghosts.append(Ghost(col_index, row_index, fantasmaTipo = "rojo"))       #Cuando en la celda sea "R" se crea el fantasma rojo
                elif cell == "A":
                    self.ghosts.append(Ghost(col_index, row_index, fantasmaTipo = "azul"))       #Cuando en la celda sea "A" se crea el fantasma azul
                elif cell == "N":
                    self.ghosts.append(Ghost(col_index, row_index, fantasmaTipo = "naranja"))    #Cuando en la celda sea "N" se crea el fantasma naranja
                elif cell == "V":
                    self.ghosts.append(Ghost(col_index, row_index, fantasmaTipo = "verde"))      #Cuando en la celda sea "V" se crea el fantasma verde

    def handleEvents (self):
        #Manejar los eventos (función de las teclas en pygame)
        for event in pygame.event.get (): #Para cada evento que ocurra, se obtiene el evento en proceso
            #Si el usuario cierra la ventana
            if event.type == pygame.QUIT:
                self.running = False        #Se cierra y se acaba el juego
        if self.estadoJuego == gameOver:    #Si es "GAMEOVER"
            self.running = False            #El juego se termina y deja de correr el programa


    def update(self): 
        #Actualizar al juego
        if self.estadoJuego == playing:
            self.player.update (self.walls)     #Actualiza el estado del pacman
           
            #Actualizar fantasmas
            for ghost in self.ghosts:           #Para cada fantasma de la lista, se actulizaran las acciones de ese fantasma
                ghost.update (self.walls)
                if self.player.rect.colliderect (ghost.rect):       #Si el jugador se choca con cualquier fantasma se acaba el juego
                    self.estadoJuego = gameOver

        #Actualizar monedas y comprobar colisiones
        for coin in self.coins [:]:     #Usar una copia de la lista para poder modificarla
            coin.update()
            if self.player.rect.colliderect (coin.rect):    #Si el jugador colisiona con una moneda
                self.coins.remove (coin)                    #La moneda se quita de la pantalla
                self.score += puntoMoneda                   #Se suma el puntaje de esa moneda

    def draw(self): #Dibujar los elementos en la pantalla
        #Base de la pantalla de color negro
        self.screen.fill (negro)

        #Dibujar las paredes
        for wall in self.walls:
            wall.draw(self.screen)

        #Dibujar las monedas
        for coin in self.coins:
            coin.draw (self.screen)

        #Dibuja al jugador y los fantasmas:
        #Se dibuja el pac.man
        self.player.draw(self.screen) 

        #Se dibuja a los fantasmas
        for ghost in self.ghosts:
            ghost.draw (self.screen)


        #Dibujar el puntaje
        score_text = self.font.render (f"Puntuación: {self.score} pts", True, blanco)
        self.screen.blit (score_text, dest=(10, 10))

        #Actualizar la pantalla
        pygame.display.flip() 

    def run(self): #Bucle principal del juego cuando se llame 'run'
        while self.running: 
            self.handleEvents () #Procesar los eventos
            self.update () #Actualizar el estado del juego
            self.draw () #Dibujar los elementos que están en el juego
            self.clock.tick (60) #60FPS


