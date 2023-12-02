import math
import pygame
import random
from time import sleep
from CasillaPygame import Casilla

N_MINAS = 10
FILAS = 10
COLUMNAS = 10
EI = 55
EE = 50

def mostrarCasilla(posMatrizX, posMatrizY, matrizCasilla, screen) -> int:
#Mostrar esa casilla
    res = matrizCasilla[posMatrizX][posMatrizY].mostrar()
    if (res == (-1)):
        return 0
    else:
        if (res == 9):
            screen.blit(pygame.image.load("Imagenes/Bomba.png"),(posMatrizX*EI+EE, posMatrizY*EI+EE))
            return N_MINAS*8
        else:
            if (res == 0):
                screen.blit(pygame.image.load("Imagenes/Casilla0v2.png"),(posMatrizX*EI+EE, posMatrizY*EI+EE))
                for j in range(posMatrizX-1, posMatrizX+2):
                    if (j >= 0 and j <= FILAS-1):
                        for k in range(posMatrizY-1,posMatrizY+2):
                            if (k >= 0 and k <= COLUMNAS-1):
                                res = res + mostrarCasilla(j,k, matrizCasilla, screen)
                return res               
            else:
                if (res > 0):
                    screen.blit(pygame.image.load("Imagenes/Casilla"+ str(res) +"v2.png"),(posMatrizX*EI+EE, posMatrizY*EI+EE))
                    return res
 
def crearMinas(primerX, primerY, matrizCasilla):
    minas  = []
    for i in range(N_MINAS):
        pos = [random.randint(0,FILAS-1),random.randint(0,COLUMNAS-1)]
        while(minas.count(pos)==1 or pos == [primerX, primerY]):
            pos = [random.randint(0,FILAS-1),random.randint(0,COLUMNAS-1)]
        minas.append(pos)
        (posMatrizX, posMatrizY) = pos
        matrizCasilla[posMatrizX][posMatrizY].convertirMina()
        for j in range(posMatrizX-1, posMatrizX+2):
            if (j >= 0 and j <= FILAS-1):
                for k in range(posMatrizY-1,posMatrizY+2):
                    if (k >= 0 and k <= COLUMNAS-1):
                        cas = matrizCasilla[j][k]
                        cas.aumentarVal()

def valorMatriz(matrizCasilla) -> int:
    #Consigue el valor de la matriz
    n = 0
    for vectorCasilla in matrizCasilla:
        for casilla in vectorCasilla:
            n = n + casilla.getVal()
    return n
            
def acabar() -> bool:
    sleep(3)
    return False

def recargarSeleccion(matrizCasilla, screen):
    (mouseX,mouseY) = pygame.mouse.get_pos()
    posMatrizX = math.floor((mouseX-EE)/EI)
    posMatrizY = math.floor((mouseY-EE)/EI)
    for x in range(FILAS):
        for y in range(COLUMNAS):
            if matrizCasilla[x][y].seleccion() == 1:
                if x == posMatrizX and y == posMatrizY:
                    screen.blit(pygame.image.load("Imagenes/CasillaSeleccionadav2.png"),(x*EI+EE, y*EI+EE))
                else:
                    screen.blit(pygame.image.load("Imagenes/Casillav2.png"),(x*EI+EE, y*EI+EE)) 
    pygame.display.flip()

def main():
     
    pygame.init()
    pygame.display.set_caption("Buscaminas")
    screen = pygame.display.set_mode((650,650))
    titulo = screen.blit(pygame.image.load("Imagenes/Titulo.png"),(85,100))
    pygame.display.flip()
    sleep(2)
    screen.fill(color=(0,0,0), rect=titulo, special_flags=0)
    pygame.mixer.music.load("Sonidos/MusicaDeJuan.mpeg")
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play()
    

    matrizCasilla = []
    for x in range(FILAS):
        vectorCasilla = []
        for y in range(COLUMNAS):
            casilla = Casilla()
            vectorCasilla.append(casilla)
        matrizCasilla.append(vectorCasilla)
    pygame.display.flip()
     
    running = True
    primera = True
    while running:

        #Se recarganlas casillas para seguir al raton en la seleccion
        recargarSeleccion(matrizCasilla, screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:

                (mouseX,mouseY) = pygame.mouse.get_pos()
                posMatrizX = math.floor((mouseX-EE)/EI)
                posMatrizY = math.floor((mouseY-EE)/EI)
                if posMatrizX >= 0 and posMatrizX <= COLUMNAS-1 and posMatrizY >= 0 and posMatrizY <= FILAS-1:
                    (izquierda, medio, derecha) = pygame.mouse.get_pressed()
                    if izquierda == True:
                        if primera == True:
                            crearMinas(posMatrizX, posMatrizY, matrizCasilla)
                            val = valorMatriz(matrizCasilla)
                            primera = False
                        res = mostrarCasilla(posMatrizX, posMatrizY, matrizCasilla, screen)
                        val = val - res
                        pygame.display.flip()
                        if val <= 0:
                            running = acabar()
                    else: 
                        if derecha == True:
                            marca = matrizCasilla[posMatrizX][posMatrizY].marcar()
                            if marca == 0:
                                screen.blit(pygame.image.load("Imagenes/CasillaMarcadav2.png"),(posMatrizX*EI+EE, posMatrizY*EI+EE))
                            if marca == 1:
                                screen.blit(pygame.image.load("Imagenes/CasillaSeleccionadav2.png"),(posMatrizX*EI+EE, posMatrizY*EI+EE))
                            pygame.display.flip()
                 
     
     

if __name__=="__main__":
    main()