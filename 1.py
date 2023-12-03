import pygame as py
import numpy as np
from math import *
from sys import exit

py.init()

def text(t,c,pos,s):
	font=py.font.Font(None,s)
	text=font.render(t,True,c)
	sc.blit(text,pos)

class blitrect():
	def __init__(self,s,c):
		self.img=py.surface.Surface(s)
		self.img.fill(c)
	def show(self,p):
		self.rect=self.img.get_rect(topleft=p)
		sc.blit(self.img,self.rect)

sc=py.display.set_mode((1450,1450))
clock=py.time.Clock()
ground=blitrect((1470,100),(200,200,200))
ballposs=(10,510)
grav=98

angle=int(input("angle"))
v=300
vx=v*cos(angle*pi/180)
vy=v*sin(angle*pi/180)
bounce_coe=0.6
friction=500 #Actualy this friction is wrong.
i=120
points=[]
points1=[]
points2=[]

p=1
sec=0.1

while True:
	fps=clock.get_fps()
	if fps>=60:
		fps=60
	if fps==0:
		fps=10**100
	event=py.event.get()
	for e in event:
		if e==py.QUIT:
			py.quit()
			exit()
			
	sc.fill((0,0,0))
	ground.show((0,520))
	py.draw.circle(sc,(255,255,255),(ballposs),10)
	
	try:
		py.draw.lines(sc,(0,0,255),False,points,5)
	except:
		pass
	else:
		py.draw.lines(sc,(0,0,255),False,points,5)
	try:
		py.draw.lines(sc,(0,255,0),False,points1,5)
	except:
		pass
	else:
		py.draw.lines(sc,(0,255,0),False,points1,5)
	try:
		py.draw.lines(sc,(255,0,0),False,points2,5)
	except:
		pass
	else:
		py.draw.lines(sc,(255,0,0),False,points2,5)
	
	angular_velocity=sqrt(vx**2+vy**2)
	
	if p==1:
		if i>=fps:
			i=0
			points.append(ballposs)
		else:
			i+=fps/(60*sec)
		
		if angular_velocity<1:
			points.append(ballposs)
			ballposs=(10,510)
			angle+=22.5
			vx=v*cos(angle*pi/180)
			vy=v*sin(angle*pi/180)
			i=120
			p+=1
			angular_velocity=sqrt(vx**2+vy**2)
		ballposs=(ballposs[0]+vx/fps,ballposs[1]-vy/fps)
		vy=vy-grav/fps
		if ballposs[0]<10 or ballposs[0]>1410 or ballposs[1]<10 or ballposs[1]>510:
			points.append(ballposs)
			
	if p==2:
		if i>=fps:
			i=0
			points1.append(ballposs)
		else:
			i+=fps/(60*sec)
		
		if angular_velocity<1:
			points1.append(ballposs)
			ballposs=(10,510)
			angle+=22.5
			vx=v*cos(angle*pi/180)
			vy=v*sin(angle*pi/180)
			i=120
			p+=1
			angular_velocity=sqrt(vx**2+vy**2)
		ballposs=(ballposs[0]+vx/fps,ballposs[1]-vy/fps)
		vy=vy-grav/fps
		if ballposs[0]<10 or ballposs[0]>1410 or ballposs[1]<10 or ballposs[1]>510:
			points1.append(ballposs)
		
	if p==3:
		if i>=fps:
			i=0
			points2.append(ballposs)
		else:
			i+=fps/(60*sec)
		
		if angular_velocity<1:
			points2.append(ballposs)
			ballposs=(10,510)
			angle=22.5
			vx=v*cos(angle*pi/180)
			vy=v*sin(angle*pi/180)
			i=120
			p+=1
			angular_velocity=sqrt(vx**2+vy**2)
		ballposs=(ballposs[0]+vx/fps,ballposs[1]-vy/fps)
		vy=vy-grav/fps
		if ballposs[0]<10 or ballposs[0]>1410 or ballposs[1]<10 or ballposs[1]>510:
			points2.append(ballposs)
	
	if p==4:
		p=1
		points,points1,points2=[],[],[]
	
	if ballposs[0]>1410:
		ballposs=(1410,ballposs[1])
		vx=-vx*bounce_coe
	if ballposs[0]<10:
		ballposs=(10,ballposs[1])
		vx=-vx*bounce_coe
	if ballposs[1]>510:
		if abs(vx)<friction/fps:
			vx=0
		else:
			if vx<0:
				vx+=friction/fps
			else:
				vx-=friction/fps
		ballposs=(ballposs[0],510)
		vy=-vy*bounce_coe
	if ballposs[1]<10:
		if abs(vx)<friction/fps:
			vx=0
		else:
			if vx<0:
				vx+=friction/fps
			else:
				vx-=friction/fps
		ballposs=(ballposs[0],10)
		vy=-vy*bounce_coe
	
	text(f'Velocity={round(angular_velocity,ndigits=2)} pixels/sec',(255,255,255),(400,10),50)
	text(f'Angle={angle}° ',(255,255,255),(100,10),50)
	
	text(str(round(fps)),(0,255,0),(10,10),30)
	py.display.update()
	clock.tick(60)
