import pygame

ROJO=[255,0,0]
AZUL=[0,17,255]
VERDE=[0,159,5]
BLANCO=[255,255,255]
AMARILLO=[255,246,3]
NEGRO=[0,0,0]
ANCHO=1200
ALTO=600

def escalar(p,s):
    xp=p[0]*s[0]
    yp=p[1]*s[1]
    return[xp,yp]

if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])

    iso=[ [100,100], [100,290], [350,350], [350,300], [150,110], [100,100], [150,110], [350,80], [150,110], [350,300],[530,250], [350,80],
    [530,250], [530,130], [350,80],[150,110], [100,100], [350,60], [570,120], [530,130], [350,80],
    [530,130], [570,120], [570,280], [350,350], [350,300], [530,250], [350,80], [150,110]]

    n = 0.9
    S = [n, n]

    pygame.draw.polygon(pantalla,ROJO, iso,2)
    print('Presiona la tecla ESPACIO para escalar el Isometrico.')
    pygame.display.flip()

     #Escalar la figura
    iso_e=[]
    for p in iso:
        pp=escalar(p,S)
        iso_e.append(pp)

    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if S[0] < 0.3 or S[1] > 2:
                        print("ERROR en los parametros de escalamiento.") 
                    elif S[0] >= 0.3 or S[1] <= 2:
                        n+=0.1
                        #pantalla.fill(NEGRO)
                        pygame.draw.polygon(pantalla,AZUL, iso_e, 2)
                        pygame.display.flip()