import pygame
import math
import sys

ROJO=[255,0,0]
AZUL=[0,17,255]
VERDE=[0,159,5]
BLANCO=[255,255,255]
AMARILLO=[255,246,3]
NEGRO=[0,0,0]
ANCHO=1200
ALTO=600

def Traslacion(p, t):
    xp = p[0] + t[0]
    yp = p[1] + t[1]

    return [xp, yp]

def cartesiano(p,c):
    xp=p[0] + c[0]
    yp= -p[1] + c[1]
    return[xp,yp]

def ProductoEscalar(v, e):
    nv=[]
    for c in v:
        nc=c*e
        nv.append(nc)
    return nv

def RotacionAnti(p, t):

    tr = math.radians(t)

    xp = int(p[0] * math.cos(tr) - p[1] * math.sin(tr))
    yp = int(p[0] * math.sin(tr) + p[1] * math.cos(tr))

    return [xp, yp]

if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])

    iso=[ [100,100], [100,290], [350,350], [350,300], [150,110], [100,100], [150,110], [350,80], [150,110], [350,300],[530,250], [350,80],
    [530,250], [530,130], [350,80],[150,110], [100,100], [350,60], [570,120], [530,130], [350,80],
    [530,130], [570,120], [570,280], [350,350], [350,300], [530,250], [350,80], [150,110]]

    Pf = [-80, 100]
    T = ProductoEscalar(Pf, -1)

    pygame.draw.polygon(pantalla, ROJO, iso, 2)
    print('Presiona la tecla ESPACIO para escalar el Isometrico.')
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()   
                    
        iso_t=[]
        for p in iso:
            np = Traslacion(p, T)
            iso_t.append(np)
        #pygame.draw.polygon(pantalla, BLANCO, iso_t, 1)
        
        iso_rot = [RotacionAnti(p, 30) for p in iso_t]
        pygame.draw.polygon(pantalla, VERDE, iso_rot, 1)

        pygame.display.flip()