import pygame
import time
import random
pygame.init()
width=600
height=800
snake_dem=30
font_style=pygame.font.SysFont("castellar",25)
score_style=pygame.font.SysFont("comicsansms",35)
clock=pygame.time.Clock()
colors={"white":(255,255,255),"black":(77, 0, 77),"purple":(51, 0, 20),"sky":(128, 170, 255),"green":(0, 26, 0),"fruit":(77, 0, 38)}
fruits={0:(255, 153, 0),1:(255, 51, 0),2:(255, 255, 0),3:(242, 132, 130),4:(189, 83, 21),5:(255, 51, 153),6:(193, 98, 0),7:(62, 47, 91),8:(250, 201, 184),9:(44, 66, 81)}
dis=pygame.display.set_mode((width,height))
pygame.display.set_caption("remaking snake game")
def score(sc):
    value=score_style.render("Your Score:"+str(sc),True,colors["purple"])
    dis.blit(value,[0,0])
def message(msg,color):
    temp=font_style.render(msg,True,colors[color])
    dis.blit(temp,[width//12,height//2])
def build_snake(snake_list,snake_dem):
    for x in snake_list:
        pygame.draw.rect(dis,colors["green"],[x[0],x[1],snake_dem,snake_dem+5])
def game_loop():
    x_cor=width//2
    y_cor=height//2
    length=1
    sc=0
    x_change=0
    y_change=0
    speed=10
    snake_list=[]
    game_over=False
    game_close=False
    pick=random.randrange(0,10)
    food_x=random.randrange(0,width-snake_dem,20)
    food_y=random.randrange(0,width-snake_dem,20)
    while game_over is False:
        while game_close is True:
            dis.fill(colors["black"])
            message("You Lost!Q-Quit or X-Play Again","white")
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key==pygame.K_q:
                        game_over=True
                        game_close=False
                    if event.key==pygame.K_x:
                        game_loop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change=-speed
                    y_change=0
                if event.key == pygame.K_RIGHT:
                    x_change=speed
                    y_change=0
                if event.key == pygame.K_UP:
                    x_change=0
                    y_change=-speed
                if event.key == pygame.K_DOWN:
                    x_change=0
                    y_change=speed
        x_cor+=x_change
        y_cor+=y_change
        if x_cor<0 or x_cor>width-snake_dem or y_cor<0 or y_cor>height-snake_dem:
            game_close=True
        dis.fill(colors["sky"])
        score(sc)
        pygame.draw.rect(dis,fruits[pick],[food_x,food_y,snake_dem,snake_dem])
        snake_head=[]
        snake_head.append(x_cor)
        snake_head.append(y_cor)
        snake_list.append(snake_head)
        if(len(snake_list)>length):
            del snake_list[0]
        for x in snake_list[:-1]:
            if x==snake_head:
                game_close=True
        build_snake(snake_list,snake_dem)
        print(x_cor,food_x,y_cor,food_y)
        if(food_x==x_cor and food_y==y_cor):
            sc+=100
            length+=1
            pick=random.randrange(0,10)
            food_x=random.randrange(0,width-snake_dem,20)
            food_y=random.randrange(0,width-snake_dem,20)
        pygame.display.update()
        clock.tick(10)
    pygame.quit()
    quit()
game_loop()
