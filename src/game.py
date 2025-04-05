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
        self.estadoJuego = intro     #Iniciará el juego y cuando cambie a "GAMEOVER" lo terminará

        #Cargar los sonidos
        self.musica = cargarSonido (archivoSonidos["musica"])
        self.wakaSound = cargarSonido (archivoSonidos["waka"])
        self.shakira = cargarSonido (archivoSonidos ["shakira"])

        #Ajustar el volumen
        self.musica.set_volume (musicaVolumen)
        self.wakaSound.set_volume (sonidoVolumen)
        self.shakira.set_volume (musicaVolumen)                        

        #Se crea paredes, monedas y jugador:
        self.walls = []
        self.coins = []
        self.player = None
        self.ghosts = []
        self.score = 0
        self.createLevel ()

        #Fuente para el texto de los puntos
        self.font = pygame.font.Font (None, 36)
        self.fontBig = pygame.font.Font (None, 100)
        self.fontMedium = pygame.font.Font (None, 50)
        self.fontSmall = pygame.font.Font (None, 30)
    
        #iniciar música de fondo
        self.musica.play (-1)    #"-1" es para que el sonido corra repetidamente

    def introScreen (self):
        #Pantalla de inicio
        #Descripción del texto
        tituloTexto = self.fontBig.render ("PACMAN", True, (amarillo))
        startTexto = self.font.render("Dale al ESPACIO para comenzar merequetengue", True, blanco)
        controlTexto = self.fontSmall.render("Usa las flechas para moverte de lado a lado como el pescao ><(((º>", True, rojo)

        #Posición del rectángulo que contiene el texto
        tituloRect = tituloTexto.get_rect (center = (width/2, height/3))
        startRect = startTexto.get_rect (center = (width/2, height/2))
        controlRect = controlTexto.get_rect (center = (width/2, 2*height/3))

        self.screen.fill (negro)
        self.screen.blit (tituloTexto, tituloRect)
        self.screen.blit (startTexto, startRect)
        self.screen.blit (controlTexto, controlRect)

    def gameOverScreen(self):
        #Pantalla de final de juego
        #Descripción del texto
        gameOverTexto = self.fontMedium.render("TE COMIÓ UN ESPÍRITU CHOCARRERO (T-T)", True, negro)
        puntajeTexto = self.fontMedium.render (f"Tenías {self.score} puntitos, corazón de melón", True, blanco)
        restartTexto = self.fontSmall.render ("Pulsa vengativamente ESPACIO para jugar otra y ganarle a los bichitos", True, rojo)

        #Posición del restángulo que contiene el texto
        gameOverRect = gameOverTexto.get_rect(center = (width/2, height/3))
        puntajeRect = puntajeTexto.get_rect(center = (width/2, height/2))
        restartRect = restartTexto.get_rect(center = (width/2, 2*height/3))

        self.screen.fill (negrito)
        self.screen.blit (gameOverTexto, gameOverRect)
        self.screen.blit (puntajeTexto, puntajeRect)
        self.screen.blit (restartTexto, restartRect)

    def victoryScreen(self):
       #Pantalla de victoria
        #Descripción del texto
        victoriaTexto = self.fontBig.render("¡¡GANASTE!! (^-^)", True, negro)
        puntajeTexto = self.font.render (f"Conseguiste {self.score} puntitos y no te mataron en el intento", True, blanco)
        restartTexto = self.fontSmall.render ("Pulsa con felicidad ESPACIO para volver a jugar al waka waka", True, rojo)

        #Posición del restángulo que contiene el texto
        victoriaRect = victoriaTexto.get_rect(center = (width/2, height/3))
        puntajeRect = puntajeTexto.get_rect(center = (width/2, height/2))
        restartRect = restartTexto.get_rect(center = (width/2, 2*height/3))

        self.screen.fill (amarillo)
        self.screen.blit (victoriaTexto, victoriaRect)
        self.screen.blit (puntajeTexto, puntajeRect)
        self.screen.blit (restartTexto, restartRect) 


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
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if self.estadoJuego == "intro":
                        self.estadoJuego = "playing"
                    elif self.estadoJuego in ["gameOver", "victory"]:
                        #Se crea un nuevo nivel con los valores restaurados cuando acaba el juego
                        self.createLevel()
                        self.score = 0
                        self.estadoJuego = "playing"
                        self.wakaSound.stop ()
                        


    def update(self): 
        #Actualizar al juego
        if self.estadoJuego in ["gameOver", "victory"]:
            self.wakaSound.stop ()             #Pare el sonido de waka waka cuando mueres o ganas
        if self.estadoJuego in ["playing"]:
            self.shakira.stop ()               #Pare el sonido de shakira cuando se vuelve a iniciar el juego
        if self.estadoJuego == playing:
            self.player.update (self.walls)     #Actualiza el estado del pacman
            self.musica.stop ()           

            #Manejar sonido de movimiento
            #sonido del waka waka
            if self.player.movimiento and not self.player.movimientoPasado: #Si el jugador se está moviendo pero no se estuvo miviendo anteriormente
                self.wakaSound.play (-1) #se reproduce en loop
            elif not self.player.movimiento and self.player.movimientoPasado:
                self.wakaSound.stop()

            #Actualizar fantasmas
            for ghost in self.ghosts:           #Para cada fantasma de la lista, se actulizaran las acciones de ese fantasma
                ghost.update (self.walls)
                if self.player.rect.colliderect (ghost.rect):       #Si el jugador se choca con cualquier fantasma se acaba el juego
                    self.estadoJuego = gameOver
                    self.coins = []
                    self.ghosts = []

        #Actualizar monedas y comprobar colisiones
        for coin in self.coins [:]:     #Usar una copia de la lista para poder modificarla
            coin.update()
            if self.player.rect.colliderect (coin.rect):    #Si el jugador colisiona con una moneda
                self.coins.remove (coin)                    #La moneda se quita de la pantalla
                self.score += puntoMoneda                   #Se suma el puntaje de esa moneda
                if len (self.coins) == 0:
                   self.estadoJuego = "victory" 
                   self.musica.stop()                       #Detener la música de fondo
                   self.shakira.play()                     #Reproducirá el sonido de la victoria


    def draw(self): #Dibujar los elementos en la pantalla
        #Base de la pantalla de color negro
        self.screen.fill (negro)
        if self.estadoJuego == intro :
            self.introScreen ()
        elif self.estadoJuego == gameOver:
            self.gameOverScreen ()  
        elif self.estadoJuego == victory:
            self.victoryScreen ()
        elif self.estadoJuego == playing:
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
            score_text = self.font.render (f"Puntitos: {self.score} pts", True, blanco)
            self.screen.blit (score_text, dest=(10, 10))

        #Actualizar la pantalla
        pygame.display.flip() 

    def run(self): #Bucle principal del juego cuando se llame 'run'
        while self.running: 
            self.handleEvents () #Procesar los eventos
            self.update () #Actualizar el estado del juego
            self.draw () #Dibujar los elementos que están en el juego
            self.clock.tick (60) #60FPS


