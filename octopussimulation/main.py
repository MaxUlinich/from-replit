import pygame, sys
from pygame.locals import QUIT

import random,time,pygame.freetype
pygame.init()


c=pygame.time.Clock()
bh=200
bw=400
w=600
h=400
lh=30
ls=10
win=pygame.display.set_mode((w+bw,h+bh))
pygame.display.set_caption("OCTOPUSES")
bottomborder=pygame.Rect(0,h,w,bh)
rightborder=pygame.Rect(w,0,bw,h)
bottomrightborder=pygame.Rect(w,h,bw,bh)
font=pygame.freetype.Font("Archivo-Regular.ttf",lh-ls)
smallfont=pygame.freetype.Font("Archivo-Regular.ttf",10)
tinyfont=pygame.freetype.Font("Archivo-Regular.ttf",10)
title=pygame.freetype.Font("Archivo-Regular.ttf",20)
titlerect=title.get_rect("OCTOPUSES HAVE TAKEN OVER THE WORLD")
background=pygame.image.load("backgroundwater.jpeg")
octo1image=pygame.image.load("octo1.png")
octo2image=pygame.image.load("octo2.png")

tree=pygame.image.load("evolutiontree.jpg")

treerect=tree.get_rect()
smalltree=pygame.transform.scale(tree,(bw,(treerect.height*bw)/treerect.width))
smalltreerect=smalltree.get_rect()
smalltreerect.x=w
smalltreerect.y=h-smalltreerect.height
tree=pygame.transform.scale(tree,(treerect.width,h))

treerect=tree.get_rect()
otterimage=pygame.image.load("shark.png")

octo1image=pygame.transform.scale(octo1image,(30,30))
octo2image=pygame.transform.scale(octo2image,(30,30))
otterimageright=pygame.transform.scale(otterimage,(80,35))
otterimageleft=pygame.transform.flip(otterimageright,True,False)

background=pygame.transform.scale(background,(w,h))

#all variables are in seconds

birthwait1=10
birthwait2=7

life=30 

killwait=1

octospeed=3
predspeed=2


class octo1():
    def __init__(self,genotype,x,y,generation,image=octo1image,xspeed=1,yspeed=1):
        self.x=x
        self.y=y
        self.image=image
        self.xspeed=xspeed
        self.yspeed=yspeed
        self.birthcount=0
        self.rect=image.get_rect()
        self.generation=generation
        self.health=20*30
        self.lastbirth=time.time()
        self.birtht=time.time()
        self.genotype=genotype
        self.gender=random.choice(["m","f"])
        self.birthwait=birthwait1
    def draw(self):
        self.rect.x=self.x
        self.rect.y=self.y
        win.blit(self.image,(self.rect.x,self.rect.y))
        
class octom():
    def __init__(self,genotype,x,y,generation,image=octo2image,xspeed=1,yspeed=1):
        self.x=x
        self.y=y
        self.image=image
        self.xspeed=xspeed
        self.yspeed=yspeed
        self.birthcount=0
        self.rect=image.get_rect()
        self.generation=generation
        self.health=10*30
        self.genotype=genotype
        self.gender=random.choice(["m","f"])
        self.birthwait=birthwait2
        self.lastbirth=time.time()
        self.birtht=time.time()
    def draw(self,win=win):
        self.rect.x=self.x
        self.rect.y=self.y
        win.blit(self.image,(self.rect.x,self.rect.y)) 

class predator():
    def __init__(self,x,y,imageright=otterimageright,imageleft=otterimageleft):
        self.killtimer=0
        
        self.x=x
        self.y=y
        self.imageright=imageright
        self.imageleft=imageleft
        self.image=self.imageright
        self.rect=self.image.get_rect()
        self.xspeed=1
        self.yspeed=1
        self.lastkill=time.time()
        
    def draw(self,win=win):
        self.rect.x=self.x
        self.rect.y=self.y
        win.blit(self.image,(self.rect.x,self.rect.y))
        

alloctos=[]
preds=[]
for i in range(7):
    alloctos.append(octo1("OO",random.randint(100,w-100),random.randint(100,h-100),1))
    


running=True
timer=0
while running:
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_o:
              try:
                preds.pop(0)
              except:
                pass
            if event.key==pygame.K_t:
              win.blit(tree,(((w/2-treerect.width/2)),0))
              pygame.display.flip()
              paused=True
              start=time.time()
              while paused:
                for event2 in pygame.event.get():
                  if event2.type==pygame.KEYDOWN:
                    
                    if event2.key==pygame.K_t:
                      paused=False
                      end=time.time()
                      for octo in alloctos:
                        octo.birtht+=end-start
            if event.key==pygame.K_p:
                preds.append(predator(random.randint(100,w-100),random.randint(100,h-100)))
                
            if event.key==pygame.K_BACKSPACE:
                preds=[]
                alloctos=[]
                for i in range(7):
                    alloctos.append(octo1("OO",random.randint(100,w-100),random.randint(100,h-100),1))
            if event.key==pygame.K_n:
                alloctos.append(octo1("OO",random.randint(100,w-100),random.randint(100,h-100),1))
            if event.key==pygame.K_h:
                alloctos.append(octo1("Oo",random.randint(100,w-100),random.randint(100,h-100),1))
            if event.key==pygame.K_m:
                alloctos.append(octom("oo",random.randint(100,w-100),random.randint(100,h-100),1))
            if event.key==pygame.K_SPACE:
                paused=True
                start=time.time()
                while paused:
                    for event in pygame.event.get():
                        if event.type==pygame.KEYDOWN:
                            
                            if event.key==pygame.K_SPACE:
                                paused=False
                              
                        if event.type==pygame.MOUSEBUTTONDOWN:
                            stop=False
                            x,y=pygame.mouse.get_pos()
                            for octo in alloctos:
                                if octo.rect.collidepoint((x,y)):
                                    stop=True
                                    if octo.genotype=="oo":
                                        phenotype="blue"
                                        adaptation="camoflauge"
                                    else:
                                        phenotype="red"
                                        adaptation="None"
                            
                                  
                                    pygame.draw.rect(win,(0,0,0),rightborder)
                                    win.blit(smalltree,(w,h-smalltreerect.height))
                                    font.render_to(win,(w,0),("The genotype of this Octopus:"+str(octo.genotype)),(255,255,255))
                                    pygame.display.flip()               
                                    pygame.time.wait(500)
                                    font.render_to(win,(w,lh),("The Pheonotype of this Octopus:"+ str(phenotype)),(255,255,255))
                                    pygame.display.flip()
                                    pygame.time.wait(500)
                                    font.render_to(win,(w,lh*2),("The adaptation of this Octopus:"+str(adaptation)),(255,255,255))
                                    pygame.display.flip()
                                    pygame.time.wait(500)
                                    font.render_to(win,(w,lh*3),("The gender of this Octopus:"+str(octo.gender)),(255,255,255))
                                    pygame.display.flip()
                                    break
                            if not stop:
                              for pred in preds:
                                if pred.rect.collidepoint((x,y)):
                                  stop=True
                                  pygame.draw.rect(win,(0,0,0),rightborder)
                                  win.blit(smalltree,(w,h-smalltreerect.height))
                                  font.render_to(win,(w,0),"The main predators of octopuses are large",(255,255,255))
                                  font.render_to(win,(w,lh),"fish (including sharks), birds, whales, eels,",(255,255,255))
                                  font.render_to(win,(w,lh+lh),"otters, and dolphins.",(255,255,255))
                                  font.render_to(win,(w,lh+lh+lh),"https://octopusworlds.com/octopus-predators/",(255,255,255))                       
                                  pygame.display.flip()
                            if not stop:
                              pygame.draw.rect(win,(0,0,0),rightborder)
                              win.blit(smalltree,(w,h-smalltreerect.height))
                              smallfont.render_to(win,(w,0),"Octopuses can be found in coastal marine waters in every ocean around",(255,255,255))
                              smallfont.render_to(win,(w,11),"the world. In order to survive and avoid predators in this environment",(255,255,255))
                              smallfont.render_to(win,(w,22),"they have adapted to be able to eject ink, change colors, squeeze into",(255,255,255))
                              smallfont.render_to(win,(w,33),"small crevices, and propel themselves quickly. Octopuses eat crabs, clams, snails,",(255,255,255))
                              smallfont.render_to(win,(w,44),"fish, and other octopuses. In order to hunt all octopuses have adapted",(255,255,255))
                              smallfont.render_to(win,(w,55),"to have a toxin that the inject into their prey, using a beak.",(255,255,255))
                              smallfont.render_to(win,(w,66),"After ensnaring prey in the webbing between their arms,",(255,255,255))
                              smallfont.render_to(win,(w,77),"octopuses are able to use their beak to penetrate hard shells.",(255,255,255))
                              tinyfont.render_to(win,(w,88),"https://www.nwf.org/Educational-Resources/Wildlife",(255,255,255))
                              pygame.display.flip()
                            end=time.time()
                for octo in alloctos:
                    octo.birtht+=end-start
    win.blit(background,(0,0))
    for pred in preds:
        pred.x+=pred.xspeed
        pred.y+=pred.yspeed
        if pred.x<0 or pred.x+pred.rect.width>w:
            
                    
            pred.xspeed*=-1
            pred.x+=pred.xspeed*4
            if pred.xspeed>0:
                pred.image=pred.imageright
            else:
                pred.image=pred.imageleft
        if pred.y<0 or pred.y+pred.rect.height>h:
            pred.yspeed*=-1
            pred.y+=4*pred.yspeed 
        
        pred.killtimer+=1
            
    for octo in alloctos:
                if octo.genotype!="oo":
                    for pred in preds:
                        if time.time()-pred.lastkill>=killwait:
                            
                            if pygame.Rect.colliderect(octo.rect,pred.rect):
                                try:
                                    alloctos.remove(octo)
                                except:
                                    pass
                                pred.lastkill=time.time()
                                pred.killtimer=0
                else: 
                  
                    for pred in preds:
                        if time.time()-pred.lastkill>=killwait:
                            
                            if pygame.Rect.colliderect(octo.rect,pred.rect):
                              yn=random.randint(1,6)
                              if yn==1:
                                  try:
                                      alloctos.remove(octo)
                                  except:
                                      pass
                              pred.lastkill=time.time()
                              pred.killtimer=0
                octo.x+=octo.xspeed
                octo.y+=octo.yspeed
                if octo.x<0 or octo.x+octo.rect.width>w:
                    octo.xspeed*=-1
                    octo.x+=2*octo.xspeed
                if octo.y<0 or octo.y+octo.rect.height>h:
                    octo.yspeed*=-1
                    octo.y+=2*octo.yspeed
                octo.draw()
                octo.birthcount+=1
                octo.health-=1
                
                #if octo.health<=0:
                if time.time()-octo.birtht>=life:
                    #print("DIE")
                    try:
                        alloctos.remove(octo)
                    except:
                        pass
                if time.time()-octo.lastbirth>=octo.birthwait:
                    for octo2 in alloctos:
                        if time.time()-octo2.lastbirth>=octo2.birthwait:
                            if pygame.Rect.colliderect(octo.rect,octo2.rect):
                                #if octo.generation==octo2.generation:
                                    if octo.gender != octo2.gender:
                                        octo.lastbirth=time.time()
                                        octo2.lastbirth=time.time()
                                        num=random.randint(0,4)
                                        for i in range(num):
                                            octo.birthcount=0
                                            octo2.birthcount=0
                                            if octo.genotype=="OO":
                                                if octo2.genotype=="OO":
                                                
                                                    alloctos.append(octo1("OO",octo.x,octo.y,octo.generation+1))
                                                elif octo2.genotype=="Oo":
                                                    alloctos.append(octo1(random.choice(["OO","Oo"]),octo.x,octo.y,octo.generation+1))
                                                
                                                elif octo2.genotype=="oo":
                                                    alloctos.append(octo1("Oo",octo.x,octo.y,octo.generation+1))
                                            elif octo.genotype=="Oo":
                                                if octo2.genotype=="OO":
                                                
                                                    alloctos.append(octo1(random.choice(["OO","Oo"]),octo.x,octo.y,octo.generation+1))
                                                elif octo2.genotype=="Oo":
                                                    geno=random.randint(1,4)
                                                    if geno==1:
                                                        alloctos.append(octom("oo",octo.x,octo.y,octo.generation+1))
                                                    else:
                                                        alloctos.append(octo1(random.choice(["Oo","Oo","OO"]),octo.x,octo.y,octo.generation+1))
                                                elif octo2.genotype=="oo":
                                                    geno=random.randint(1,2)
                                                    if geno==1:
                                                        alloctos.append(octom("oo",octo.x,octo.y,octo.generation+1))
                                                    else:
                                                        alloctos.append(octo1("Oo",octo.x,octo.y,octo.generation+1))
                                            elif octo.genotype=="oo":
                                                if octo2.genotype=="OO":
                                                    alloctos.append(octo1("Oo",octo.x,octo.y,octo.generation+1))
                                                
                                                elif octo2.genotype=="Oo":
                                                      
                                                    geno=random.randint(1,2)
                                                    if geno==1:
                                                        alloctos.append(octom("oo",octo.x,octo.y,octo.generation+1))
                                                    else:
                                                        alloctos.append(octo1("Oo",octo.x,octo.y,octo.generation+1))
                                                elif octo2.genotype=="oo":
                                                    alloctos.append(octom("oo",octo.x,octo.y,octo.generation+1))
                        
    timer+=c.get_time()  
    if timer>=2000:
        timer=0
        for pred in preds:
            pred.xspeed=random.randint(predspeed*-1,predspeed)
            pred.yspeed=random.randint(predspeed*-1,predspeed) 
            if pred.xspeed>0:
                pred.image=pred.imageright
            else:
                pred.image=pred.imageleft
        for octo in alloctos:
            octo.xspeed=random.randint(octospeed*-1,octospeed)
            octo.yspeed=random.randint(octospeed*-1,octospeed)
    for pred in preds:
      pred.draw()
    if len(alloctos)>=300:
      #pygame.draw.rect(win,(0,0,0),titlerect)
      title.render_to(win,((w-titlerect.width)/2,h/2),"OCTOPUSES HAVE TAKEN OVER THE WORLD",(255,255,255))
      font.render_to(win,(w/2-100,h/2+50),"(backspace to restart)",(255,255,255))
    pygame.display.flip()  
    #win.blit(background,(0,0))
    pygame.draw.rect(win,(0,0,0),bottomborder)
    pygame.draw.rect(win,(0,0,0),bottomrightborder)
    #pygame.draw.rect(win,(0,0,0),border,1)
    win.blit(smalltree,(w,h-smalltreerect.height))
    font.render_to(win,(5,h),"Press 'M' to introduce a mutation into the population",(255,255,255))
    font.render_to(win,(5,h+20),"Press 'P' to introduce predators",(255,255,255))
    font.render_to(win,(5,h+40),"Press 'N' to introduce Octopuses with Homozygous dominant traits",(255,255,255))
    font.render_to(win,(5,h+80),"Press 'T' to show the evolutionary tree")
    font.render_to(win,(5,h+60),"Press 'H' to introduce Octopuses with 'Oo' genes",(255,255,255))
    font.render_to(win,(w,h+5),"Total Octopuses: "+str(len(alloctos)),(255,255,255))
    font.render_to(win,(w,h+25),"Octopuses with a Genetic Variation (Blue)",(255,255,255))
    font.render_to(win,(w,h+45),"have a higher chance of survival from sharks",(255,255,255))
    font.render_to(win,(w,h+65),"and can have offspring more frequently",(255,255,255))
    
    
    
    c.tick(30)
    