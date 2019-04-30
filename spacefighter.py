from gamelib import*

game = Game(800,600,"Space Fighter")
bk = Image("worldspace.png",game)
spacestory = Image("spacestory.png",game)
spacestory.resizeTo(800,600)

title = Image("title.png",game)
title.resizeTo(500,200)
title.y-=150

play = Image("play.png",game)
play.resizeTo(200,100)
play.y+=20

story = Image("story.png",game)
story.resizeTo(200,100)
story.y+=150

heroship = Image("heroship.png",game)
heroship.resizeBy(-50)
heroship.ammo = 0
heroship.health = 100

pods = Animation("healthpods.png",8,game,396/4,308/2)
pods.resizeBy(-50)

enemyship = Image("enemyship.png",game)
enemyship.resizeBy(-50)
enemyship.health = 200

greenboss = Image("greenboss.png",game)
greenboss.resizeBy(-60)
greenboss.health = 400

explosion = Animation("explosion1.png",20,game,1254/20,64)
explosion.visible = False
explosion.resizeBy(30)

minion = Animation("minion.png",1,game,150,102)
minion.resizeTo(60,50)
minion.health = 20
end = Image("end.jpg",game)
end.resizeTo(800,600)
end.visible=False

items = 0
score = 0
    
#Minion Setup
minion = []
for index in range(25):
    minion.append(Animation("minion.png",1,game,150,102))

for index in range(25):
    speed = randint(2,8)
    minion[index].setSpeed(speed,180)
    x = randint(100,700)
    y = -randint(100,1400)
    minion[index].moveTo(x,y)


#Ammo Setup
ammo = []
for index in range(20):
    ammo.append(Animation("ammo.png",11,game,352/11,32))

for index in range(20):
    speed = randint(2,8)
    x = randint(100,700)
    y = randint(100,1400)
    ammo[index].moveTo(x,y)
    ammo[index].setSpeed(speed,180)
game.setBackground(bk)

#title screen
while not game.over:
    game.processInput()
    
    game.scrollBackground("down",5)
    title.draw()
    play.draw()
    story.draw()
    spacestory.draw()
    spacestory.visible = False

    if mouse.collidedWith(story,"rectangle")and mouse.LeftButton:
        spacestory.visible = True

    if mouse.collidedWith(play,"rectangle")and mouse.LeftButton:
        game.over = False
                
    game.update(30)

game.over = True
#Level 1
heroship.ammo = 0
minionPassed = 0
while not game.over:
    game.processInput()
    
    game.drawText("Level 1",25,25)
    game.scrollBackground("down",5)
    heroship.draw()
    explosion.draw(False)
    enemyship.draw()
    enemyship.moveTo(x,y)
    #Minion
    for index in range(25):
        minion[index].move()
        if heroship.collidedWith(minion[index]):
            heroship.health -=10
            explosion.moveTo(heroship.x,heroship.y-10)
            explosion.visible = True
            explosion.moveTo(heroship.x,heroship.y-40)
        if minion[index].isOffScreen("bottom") and minion.visible:
            minionPassed +=1
            minion[index].visible = False
        if minionPassed >=50:
            game.over = True
       
    #Ammo
    for index in range(20):
        ammo[index].move()
        if heroship.collidedWith(ammo[index]):
            ammo[index].visible = False
            heroship.ammo +=2

    #heroship control
    if keys.Pressed[K_LEFT]:
        heroship.x-=10
    if keys.Pressed[K_RIGHT]:
        heroship.x+=10
    if keys.Pressed[K_UP]:
        heroship.y-=10
    if keys.Pressed[K_DOWN]:
        heroship.y+=10
        
    if keys.Pressed[K_SPACE]:
        ammo[index].moveTo(heroship.x,heroship.y)
        ammo[index].setSpeed(24,0)
        ammo[index].visible = True

    if heroship.health < 0:
        game.over = True

    if enemyship.health < 40:
        game.over = True

    if minion[index].health<0:
        minion[index].visible = False

    game.drawText("Ammo:"+str(heroship.ammo),heroship.x -20,heroship.y +50)
    game.drawText("Health:"+str(heroship.health),heroship.x -10,heroship.y +70)
    game.update(30)
game.over = False


#Level 2
while not game.over and heroship.health>0:
    game.processInput()
    
    game.scrollBackground("down",5)
    game.drawText("Level 2",25,25)
    heroship.draw()
    explosion.draw(False)
    for index in range(25):
        minion[index].move()
        if minion[index].collidedWith(heroship):
            heroship.health -=10
            minion[index].visible = False
    for index in range(20):
        ammo[index].move()
        if ammo[index].collidedWith(greenboss):
            greenboss.health -=50

    for index in range(20):
        ammo[index].move()
        if heroship.collidedWith(ammo[index]):
            ammo[index].visible = False
            heroship.ammo +=2

    #heroship control
    if keys.Pressed[K_LEFT]:
        heroship.x-=10
    if keys.Pressed[K_RIGHT]:
        heroship.x+=10
    if keys.Pressed[K_UP]:
        heroship.y-=10
    if keys.Pressed[K_DOWN]:
        heroship.y+=10
        
    if keys.Pressed[K_SPACE]:
        ammo[index].moveTo(heroship.x,heroship.y)
        ammo[index].setSpeed(24,0)
        ammo[index].visible = True
        heroship.ammo -=2

    greenboss.draw()
    greenboss.moveTo(x,y)
    greenboss.visible = False
        
    game.drawText("Ammo:"+str(heroship.ammo),heroship.x -20,heroship.y +50)
    game.drawText("Health:"+str(heroship.health),heroship.x -10,heroship.y +70)
    game.update(30)
game.over=True

#End Screen
while not game.over:
    game.processInput
    end.visible = True
    if heroship.health>0:
        game.over = True
   


    game.update(60)

game.over = False
