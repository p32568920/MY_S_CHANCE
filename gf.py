#game_functions
import pygame
import pygame.font
from evil_hero import Evil_Hero

def game_over():
    pygame.quit()# 退出pygame
    sys.exit()# 退出系统

def text_print(screen,text,left,top,text_color,bg_color):
    font = pygame.font.Font('simhei.ttf',20)
    text = font.render(text, True, text_color,bg_color)
    screen.blit(text, (left, top))
    pygame.display.flip()

def line_writer(screen):
    pygame.draw.line(screen,(99,99,99),
                     (10,10),
                     (screen.get_width()-10,10))
    pygame.draw.line(screen,(99,99,99),(10,10),(10,70))
    pygame.draw.line(screen,(99,99,99),
                     (10,70),
                     (screen.get_width()-10,70))
    pygame.draw.line(screen,(99,99,99),
                     (screen.get_width()-10,10),
                     (screen.get_width()-10,70))

    pygame.draw.line(screen,(99,99,99),(10,80),(400,80))
    pygame.draw.line(screen,(99,99,99),(10,80),
                     (10,screen.get_height()-10))
    pygame.draw.line(screen,(99,99,99),(400,80),
                     (400,screen.get_height()-10))
    pygame.draw.line(screen,(99,99,99),
                     (10,screen.get_height()-10),
                     (400,screen.get_height()-10))
        
    pygame.draw.line(screen,(99,99,99),(410,70),
                     (screen.get_width()-10,70))
    pygame.draw.line(screen,(99,99,99),
                     (410,screen.get_height()-10),
                     (screen.get_width()-10,screen.get_height()-10))
    pygame.draw.line(screen,(99,99,99),(410,70),
                     (410,screen.get_height()-10))
    pygame.draw.line(screen,(99,99,99),
                     (screen.get_width()-10,70),
                     (screen.get_width()-10,
                      screen.get_height()-10))

    pygame.display.flip()

def update_status(screen,Evil_Hero):
    text_print(screen,Evil_Hero.name,410,70,
                                  (0,0,0),(255,255,255))
    text_print(screen,'HP:'+str(Evil_Hero.hp)+'/'+str(Evil_Hero.maxhp),410,90,
                                          (0,0,0),(255,255,255))
    text_print(screen,'MP:'+str(Evil_Hero.mp)+'/'+str(Evil_Hero.maxmp),410,110,
                                          (0,0,0),(255,255,255))
    text_print(screen,'SP:'+str(Evil_Hero.sp)+'/'+str(Evil_Hero.maxsp),410,130,
                                          (0,0,0),(255,255,255))


def update_textbox(screen,c_1,index,f):
    screen.fill((1,30,1))
    index+=f
    text_print(screen,c_1[index%len(c_1)],10,10,
                                  (0,0,0),(255,255,255))
    text_print(screen,c_1[(index+1)%len(c_1)],10,30,
                                  (0,0,0),(255,255,255))
    text_print(screen,c_1[(index+2)%len(c_1)],10,50,
                                  (0,0,0),(255,255,255))
    return index

