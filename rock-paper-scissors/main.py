import pygame, sys, random

from pygame.locals import QUIT

pygame.init()
c=pygame.time.Clock()
w=1005
h=466

rockpic="rock.png"
paperpic="paper.png"
scissorspic="scissors.png"

speed=3

numofrock=10
numofpaper=10
numofscissors=10

rect=pygame.Rect(w,h,38,38)

win = pygame.display.set_mode((w, h))
pygame.display.set_caption('Rock Paper Scissors')

rock=pygame.image.load(rockpic)
paper=pygame.image.load(paperpic)
scissors=pygame.image.load( scissorspic)

rock=pygame.transform.scale(rock, (30,30))
paper=pygame.transform.scale(paper, (30,30))
scissors=pygame.transform.scale(scissors, (30,30))

pairs={"rock":rock,"paper":paper, "scissors":scissors}
time=0
class rps():
  def __init__(self,rps,image,x,y,velx,vely):
    self.rps=rps
    self.image=image
    self.rect=self.image.get_rect()
    self.rect.x=x
    self.rect.y=y
    self.velx=velx
    self.vely=vely

  def move(self):
    self.rect.x+=self.velx
    self.rect.y+=self.vely
    if self.rect.x+self.rect.width>=w:
      self.rect.x=w-self.rect.width
      self.velx*=-1
    if self.rect.x<=0:
      self.rect.x=0
      self.velx*=-1
    if self.rect.y+self.rect.height>=h:
      self.vely*=-1  
      self.rect.y=h-self.rect.height
    if self.rect.y<=0:
      self.vely*=-1  
      self.rect.y=0
    
    win.blit(self.image,(self.rect.x,self.rect.y))

objects=[]

movable=rps("paper",paper,w/2,h/2,0,0)    
objects.append(movable)
for i in range(numofpaper):
  objects.append(rps("paper",paper,random.randint(0,w/3-50),random.randint(0,h/2),random.randint(-2,2),random.randint(-2,2)))
for i in range(numofscissors):  
  objects.append(rps("scissors",scissors,random.randint(w/3,2*w/3-50),random.randint(h/2,h),random.randint(-2,2),random.randint(-2,2)))
for i in range(numofrock):
  objects.append(rps("rock",rock,random.randint(2*w/3,w),random.randint(0,h/2),random.randint(-2,2),random.randint(-2,2)))
  
while True:
    
      
    for item1 in objects:
      for item2 in objects:
        if item1.rect.colliderect(item2.rect):
          if item1.rps=="rock" and item2.rps=="scissors":
            item2.rps="rock"
            item2.image=rock
          if item1.rps=="paper" and item2.rps=="rock":
            item2.rps="paper"
            item2.image=paper
          if item1.rps=="scissors" and item2.rps=="paper":
            item2.rps="scissors"
            item2.image=scissors
            ("!")
    time+=c.get_time()
    
    for item in objects:
      item.move()
    rect.x=movable.rect.x-4
    rect.y=movable.rect.y-4
    pygame.draw.rect(win,(255,10,10),rect,3)  
    if time>=3000:
        time=0
        for item in objects:
          item.velx+=random.randint(-1,1)
          item.vely+=random.randint(-1,1)
          if item.velx>=3:
            item.velx=2
          if item.velx<=-3:
            item.velx=-2
          if item.vely>=3:
            item.vely=2
          if item.vely<=-3:
            item.vely=-2
    movable.velx=0
    movable.vely=0
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN:
          if event.key==pygame.K_EQUALS:
            speed+=1
          if event.key==pygame.K_MINUS:
            speed-=1
          if event.key==pygame.K_r:
            numofrock+=1
          if event.key==pygame.K_e:
            numofrock-=1
          if event.key==pygame.K_p:
            numofpaper+=1
          if event.key==pygame.K_o:
            numofpaper-=1
          if event.key==pygame.K_s:
            numofscissors+=1
          if event.key==pygame.K_a:
            numofscissors-=1  
          if numofrock<0:
              numofrock=0
          if numofpaper<0:
              numofpaper=0  
          if numofscissors<0:
              numofscissors=0 
        if event.type == pygame.KEYDOWN and event.key==pygame.K_SPACE:
          objects=[]

          movable=rps("paper",paper,w/2,h/2,0,0)    
          objects.append(movable)
          
          
          '''''
          for i in range(numofpaper):
           
          objects.append(rps("paper",paper,random.randint(0,w/3-50),random.randint(0,h/2),random.randint(-2,2),random.randint(-2,2)))
          for i in range(numofscissors):  
             objects.append(rps("scissors",scissors,random.randint(w/3,2*w/3-50),random.randint(h/2,h),random.randint(-2,2),random.randint(-2,2)))
          for i in range(numofrock):
            objects.append(rps("rock",rock,random.randint(2*w/3,w),random.randint(0,h/2),random.randint(-2,2),random.randint(-2,2)))
             '''                 
          for i in range(numofpaper):
           
                objects.append(rps("paper",paper,random.randint(0,w),random.randint(0,h),random.randint(-2,2),random.randint(-2,2)))
                #print("added")
          for i in range(numofscissors):  
               objects.append(rps("scissors",scissors,random.randint(0,w),random.randint(0,h),random.randint(-2,2),random.randint(-2,2)))
          for i in range(numofrock):
                objects.append(rps("rock",rock,random.randint(0,w),random.randint(0,h),random.randint(-2,2),random.randint(-2,2)))
    keys=pygame.key.get_pressed()
    if keys[pygame.K_UP]:
      movable.rect.y-=speed
    if keys[pygame.K_DOWN]:  
      movable.rect.y+=speed
    if keys[pygame.K_LEFT]:
      movable.rect.x-=speed
    if keys[pygame.K_RIGHT]:  
      movable.rect.x+=speed 
    
    pygame.display.flip()                          
    win.fill((0,0,0))
    #win.fill((100,200,100))
    c.tick(30)
