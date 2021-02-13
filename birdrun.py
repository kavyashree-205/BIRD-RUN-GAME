#importing required modules
import pygame
import os
import math
import tkinter as tk

#game is designed completely inside play function
def play():

    pygame.init() #initialising pygame module
    
    window=pygame.display.set_mode((600,300)) #setting the size of the display
    
    pygame.display.set_caption("BIRD RUN!!") #setting the caption or title of the game
    
    #loading background images
    sky=pygame.image.load("save balloon/hills.jpg") 
    sky1=pygame.image.load("save balloon/mountains.jpg")
    
    #loading the images of obstacles which are buildings in this game
    building1=pygame.image.load("save balloon/tall.png")
    build1x=470 # setting the initial position
    speed_build1=0.1 # setting the constant speed
    
    building2=pygame.image.load("save balloon/lighthouse.png")
    build2x=470
    speed_build2=0.2
    
    building3=pygame.image.load("save balloon/building.png")
    build3x=470
    speed_build3=0.3
    build1y=build2y=build3y=140
    
    #loaging bird image
    bird=pygame.image.load("save balloon/macaw.png")
    birdx=230
    birdy=50
    speed=0
    
    #setting the image of game icon
    icon=pygame.image.load("save balloon/small.png")
    pygame.display.set_icon(icon)
    
    #declaring the font for displaying score and out statement
    font=pygame.font.Font("freesansbold.ttf",40)
    font1=pygame.font.Font("freesansbold.ttf",41)
    #count variable for keeping track of score
    count=0
    #functions to draw image in pygame window
    def show_building1(x,y):
        window.blit(building1,(build1x,build1y))
    
    def show_building2(x,y):
        window.blit(building2,(build2x,build2y))
    
    def show_building3(x,y):
        window.blit(building3,(build3x,build3y))
        
    def show_bird(x,y):
        window.blit(bird,(birdx,birdy))
    #function to define collision
    def is_collision(a,b,c,d,e,f):
        distance1=math.sqrt(pow((build1x-birdx),2)+pow((build1y-birdy),2))
        distance2=math.sqrt(pow((build2x-birdx),2)+pow((build2y-birdy),2))
        distance3=math.sqrt(pow((build3x-birdx),2)+pow((build3y-birdy),2))
        if distance1<=45:
            return True
        elif distance2<=45:
            return True
        elif distance3<=40:
            return True
    
    while True:
        window.fill((0,0,0))
        window.blit(sky,(0,0))
        if count>=12:
            window.blit(sky1,(0,0))
                             
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.display.quit()
                os._exit(1)
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    speed=-0.5
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_SPACE:
                    speed=0.2
                    
        def show_out():
            i=0
            while i<10000:
                out=font.render("You Got Hit!!",True,(0,0,0))
                show_rect=out.get_rect()
                show_rect.center=(300,150)
                window.blit(out,show_rect)
                i=i+1
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.display.quit()
                    os._exit(1)
                
    
        birdy=birdy+speed
        show_bird(birdx,birdy)
        if birdy<10:
            birdy=10
            show_bird(birdx,birdy)
        
        build1x=build1x-speed_build1
        show_building1(build1x,build1y)
        
        if build1x<=-128:
            build1x=620
            count=count+1
       
        build2x=build2x-speed_build2
        show_building2(build2x,build2y)
        if build2x<=-128:
            build2x=560
            count=count+1
        
        build3x=build3x-speed_build3
        show_building3(build3x,build3y)
        if build3x<=-128:
            build3x=600
            count += 1
      
        collision=is_collision(build1x,build2x,build3x,build1y,build2y,build3y)
        score=font1.render("Score :"+str(count),True,(0,0,0))
        window.blit(score,(410,10))
        if collision==True:
            show_out()
        if birdy>=300:
            show_out()
    
        pygame.display.update()
        
def help():
    root1=tk.Tk()
    root1.geometry("600x300")
    root1.configure(bg="#53F6D1")
    root1.title("How To Play!")
    tk.Label(root1,text="How To Play The Game",font=("Forte",30),bg="#5786E5",padx=110).grid(row=0,column=0)
    tk.Label(root1,text="1.Press the Space Key to control the bird",font=("Forte",20),bg="#53F6D1",padx=10,pady=10).grid(row=1,column=0)
    tk.Label(root1,text="2.Control the bird from falling on buildings",font=("Forte",20),bg="#53F6D1",padx=10,pady=10).grid(row=2,column=0)
    tk.Label(root1,text="3.If the bird falls below the screen\nit is considered as out",font=("Forte",20),bg="#53F6D1",padx=10,pady=10).grid(row=3,column=0)
    

#interface or layout to access the game    
root=tk.Tk()
root.geometry("600x300")
root.configure(bg="#53F6D1")
root.title("BIRD RUN GAME")
heading=tk.Label(root,text="Welcome To Bird Run Game!!",font=("Forte",30),padx=50,pady=10,bg="#5786E5").grid(row=0,column=0)
space=tk.Label(root,text="",font=("Ariel Black",20),bg="#53F6D1").grid(row=1,column=0)
button1=tk.Button(root,text="Play",font=("Forte",20),width=30,bg="#5786E5",command=lambda:play(),activebackground="blue")
button1.grid(row=2,column=0)
space=tk.Label(root,text="",font=("Ariel Black",20),bg="#53F6D1").grid(row=3,column=0)
button2=tk.Button(root,text="How To Play",font=("Forte",20),width=30,bg="#5786E5",command=lambda:help(),activebackground="blue")
button2.grid(row=4,column=0)
root.mainloop()