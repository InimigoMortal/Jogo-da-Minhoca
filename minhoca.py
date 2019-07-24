import pygame
from random import randint
pygame.init()

jan = pygame.display.set_mode((500,500))

pygame.display.set_caption("Minhoca")
x = 250
y = 210
width= 20
height = 20
vel = 10
conta = 0

cima = False
baixo = False
esq = False
dire = False



    





#mainloop
run = True

lis = []
cont = 0
for i in range(47):
    conta += 10
    lis.append(conta)


    
   


xal = lis[randint(0,46)]
yal = lis[randint(0,46)]
conta2 = 0
massa = 5
liscords = []

while run:
    pygame.time.delay(100)
    tam = 8
    pygame.draw.ellipse(jan, (0,250,0),(xal,yal,tam,tam))
    pygame.display.update()
    
    
    
            

    if cima:
        y -= vel
        conta2 += 1
        cord = [x,y]
        if cord in liscords:
            print("Você comeu a própria Carne!")
            print("Você Morreu")
            run = False
        liscords.append(cord)
    
        
        
    if baixo:
        y += vel
        conta2 += 1
        cord = [x,y]
        if cord in liscords:
            print("Você comeu a própria Carne!")
            print("Você Morreu")
            run = False
        liscords.append(cord)
        
    if esq:
        x -= vel
        conta2 += 1
        cord = [x,y]
        if cord in liscords:
            print("Você comeu a própria Carne!")
            print("Você Morreu")
            run = False
        liscords.append(cord)
        
    if dire:
        x += vel
        conta2 += 1
        cord = [x,y]
        if cord in liscords:
            print("Você comeu a própria Carne!")
            print("Você Morreu")
            run = False
        liscords.append(cord)
        
    
    
    if x == xal-10 and y == yal-10:
        xal = lis[randint(0,46)]
        yal = lis[randint(0,46)]
        massa += 5
        
        
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > vel - 5:
        esq = True
        dire = False
        cima = False
        baixo = False
    if keys[pygame.K_RIGHT] and x < 500 - width - 5:
        x += vel
        dire = True
        esq = False
        cima = False
        baixo = False

    if keys[pygame.K_UP] and y > vel - 5:
        esq = False
        dire = False
        cima = True
        baixo = False
    if keys[pygame.K_DOWN] and y < 500 - height - 5:
        esq = False
        dire = False
        baixo = True
        cima = False
    

    if x >= 480 or x == 0:
        print("Você Morreu")
        run = False
    if y >= 480 or y == 0:
        print("Você Morreu")
        run = False

    pygame.draw.ellipse(jan, (101, 67, 33),(x,y,width,height))
    pygame.display.update()
    
    if conta2 >= massa:
        jan.fill((0,0,0))
        conta2 = 0
        liscords = []
pygame.quit()