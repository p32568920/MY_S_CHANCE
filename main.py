import pygame
import sys
import gf
from evil_hero import Evil_Hero

def game_over():
    pygame.quit()# 退出pygame
    sys.exit()# 退出系统

def game_run():
    #初始化
    pygame.init()
    screen = pygame.display.set_mode((1024,768))
    screen.fill((1,30,99))
    pygame.display.flip()
    #标题
    caption = 'My_S_Chance'
    pygame.display.set_caption(caption)

    c_1=[]
    with open('c_1.txt') as f_obj:
        for line in f_obj: 
            c_1.append(line.rstrip())

    #c_1=['a','b所示','sad','asdasd','23213','dsd']
    index =0

    gf.text_print(screen,c_1[index%6],10,10,
                                  (0,0,0),(255,255,255))
    gf.text_print(screen,c_1[(index+1)%6],10,30,
                                  (0,0,0),(255,255,255))
    gf.text_print(screen,c_1[(index+2)%6],10,50,
                                  (0,0,0),(255,255,255))

    hero = Evil_Hero()


    while True:
        #事件读取
        #pygame.draw.rect(screen,(255,255,255),(0,0,640,60))
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                game_over()
            if e.type == pygame.MOUSEBUTTONDOWN:
                if e.dict['button']==5:
                    index = gf.update_textbox(screen,c_1,index,1)
                elif e.dict['button']==4:
                    index = gf.update_textbox(screen,c_1,index,-1)
                            
            elif e.type == pygame.KEYDOWN:
                ek = e.key
                if ek == pygame.K_SPACE or ek == pygame.K_s or ek == pygame.K_DOWN:
                    index = gf.update_textbox(screen,c_1,index,1)  
                elif ek == pygame.K_ESCAPE:
                    game_over()
                elif ek == pygame.K_w or ek == pygame.K_UP:
                    index = gf.update_textbox(screen,c_1,index,-1) 
                elif ek == pygame.K_b:
                    screen.fill((99,30,1))
                    pygame.display.flip()

            #gf.update_textbox(screen,c_1,index,0)
                
            #状态栏更新
            gf.update_status(screen,hero)

                
        #画边框
                    
        gf.line_writer(screen)

        pygame.display.flip()
                                 
        
if __name__ == '__main__':
    game_run()
    
    
