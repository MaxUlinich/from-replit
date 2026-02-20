import pygame, sys, random
from pygame.locals import QUIT
pygame.init()
pygame.mixer.init()
pink=(255, 79, 214)
red=(255,0,0)
orange=(247, 127, 7)
yellow=(243, 255, 23)
green=(0, 255, 0)
blue=(0,0,255)
purple=(180, 9, 237)
colors=[pink,red,orange,yellow,green,blue,purple]
boing=pygame.mixer.Sound("boing1.mp3")

a=pygame.mixer.Sound("A2.mp3")
b=pygame.mixer.Sound("B2.mp3")
c=pygame.mixer.Sound("C3.mp3")
d=pygame.mixer.Sound("D3.mp3")
e=pygame.mixer.Sound("E3.mp3")
f=pygame.mixer.Sound("F3.mp3")
g=pygame.mixer.Sound("G3.mp3")

music=[a,b,c,d,e,f,g]

channelsnum=1000
pygame.mixer.set_num_channels(channelsnum)


clock=pygame.time.Clock()

w=700
frameh=400
h=(14/15)*frameh
z=0

balls=[]

bounce=.75
gravity=.5
volume=.04
radius=25
force=0
maxforce=25
health=400
win = pygame.display.set_mode((w, frameh))
pygame.display.set_caption('Boing')

class Ball:
  def __init__(self,x,y,radius,color,force,maxforce,health,bounce,sound):
    self.x=x
    self.y=y
    self.radius=radius
    self.force=force
    self.color=color
    self.health=health
    self.maxforce=maxforce
    self.bounce=bounce
    self.sound=sound
    self.channel=pygame.mixer.find_channel(force=True)
    if self.x<w*1/7:
      self.sound=a
    elif self.x<w*2/7:
      self.sound=b
    elif self.x<w*3/7:
      self.sound=c
    elif self.x<w*4/7:
      self.sound=d 
    elif self.x<w*5/7:
      self.sound=e
    elif self.x<w*6/7:
      self.sound=f  
    else:
      self.sound=g
  def fall(self):
    
     
    if self.y + self.radius>=h:
      self.sound.set_volume(self.force*volume)
      self.channel=pygame.mixer.find_channel(force=True)         
      self.channel.play(self.sound)
      #self.channel=pygame.mixer.find_channel(force=True)
      self.channel.fadeout(2000)
      '''
      for i in range(channelsnum):
        if not pygame.mixer.Channel(i).get_busy():
          pygame.mixer.Channel(i).play(self.sound)
          break
      
        if i >= channelsnum-1:
          pygame.mixer.Channel(i).play(self.sound)
          break
          '''
      self.sound.play()
      self.force*=-1
      self.maxforce*=bounce
      self.y=h-self.radius-1
      #self.force=(self.maxforce)*-1
    if self.y+self.radius < h:
      if self.force< self.maxforce:
        self.force+=gravity
      self.y+=round(self.force)
    if self.y+self.radius>=h:
      self.y=h-self.radius 
    pygame.draw.circle(win,self.color,(self.x,self.y),self.radius)
    self.health-=1
    if self.health<=0 or self.maxforce<=1:
      balls.remove(self)
#balls.append(Ball(-200,0,radius,(random.randint(1,255),random.randint(1,255),random.randint(1,255)),force,maxforce,health,bounce,boing))
while True:
    x,y=pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN:
          if event.key==pygame.K_a:
            balls.append(Ball(w/14,0,radius,(pink),force,maxforce,40,bounce,random.choice(music)))
          if event.key==pygame.K_b:
            balls.append(Ball(3*w/14,0,radius,(red),force,maxforce,40,bounce,random.choice(music)))
          if event.key==pygame.K_c:
            balls.append(Ball(5*w/14,0,radius,(orange),force,maxforce,40,bounce,random.choice(music)))
          if event.key==pygame.K_d:
            balls.append(Ball(7*w/14,0,radius,(yellow),force,maxforce,40,bounce,random.choice(music)))  
          if event.key==pygame.K_e:
            balls.append(Ball(9*w/14,0,radius,(green),force,maxforce,40,bounce,random.choice(music))) 
          if event.key==pygame.K_f:
            balls.append(Ball(11*w/14,0,radius,(blue),force,maxforce,40,bounce,random.choice(music)))
          if event.key==pygame.K_g:
            balls.append(Ball(13*w/14,0,radius,(purple),force,maxforce,40,bounce,random.choice(music)))  

          if event.key==pygame.K_BACKSPACE:
            balls=[]
        '''
        if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE:
          bounce=int(input("Enter bounce (-500:500): "))

          if bounce<=-500:
            bounce=-499
          if bounce>=0:
            bounce=(bounce*(4/500))+1
            
          elif bounce<0:
            bounce=bounce*(8/5000)+1
          print(bounce)  
          '''
        if event.type==pygame.MOUSEBUTTONDOWN:
          
          z=1
        if event.type==pygame.MOUSEBUTTONUP:
          
          
          z=0
        #print(z)  
    if z==1:
          
          balls.append(Ball(x,y,radius,(random.randint(1,255),random.randint(1,255),random.randint(1,255)),force,maxforce,health,bounce,random.choice(music)))
          z=7
    elif z>1:
          z-=1
    win.fill((0,0,0))
    for i in range(7,0,-1):
      pygame.draw.polygon(win,colors[i-1],[(0,frameh),(0,h),(w*i/7,h),(w*i/7,frameh)],2)
    for i in balls:
      
      i.fall()
    
    clock.tick(60)      
    pygame.display.update()
