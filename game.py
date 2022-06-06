# Description:

# The game that we have chosen to emulate is “Crossy Road”. Essentially a character can move side to side and up to down with arrow keys to cross roads of moving traffic. However, instead of doing a game that goes on indefinitely, we will make a set of levels. If the character gets hit, he will be able to restart to the beginning of the level and they will have a checkpoint for each level completed.
# HOW TO PLAY: To play the game use your arrow keys to navigate through oncoming traffic. There are five levels total, you are given five lives to complete each level, and a timer is set for each level. If you get hit by a car or the timer runs out, you will lose a life. If you lose a life you will be given an option to restart the level and an option to restart the game, if you lose all your lives, you will only be given the option to restart the game.

# Required features:
# User Input:
# Directional arrows, movement for character, can't move up to increase pace of game

# Game Over:
# Character gets hit

# Small Enough Window:
# Game window is 800 width, 600 height

# Graphics/Images:
# The characters are images
# The cars are images

# Optional Features:
# Restart:
# If the character gets hit by a car, they will have an option to restart the level and also restart the game

# Scrolling Level (THIS GOT CHANGED TO INTERSESSION PROGRESS)
# INTERSESSION PROGRESS: There is an option to restart a level if there are enough lives

# Timer:
# The character will have a certain amount of time to complete the level, and if the timer runs out, they will automatically die

# Levels:
# The game will be divided up into several different levels all which consist of increasingly harder difficulties. 
import pygame
import gamebox
import random

camera = gamebox.Camera(800, 600)

player_speed = 50
score = 0
levelcount = 0
scoretotal = 0
scorePrint = gamebox.from_text(400, 250, "Youre Score is " + str(scoretotal), 120, "green", bold=True)
instruction1 = gamebox.from_text(400, 350, "Press R to restart Level, Press O to restart game", 40, "green", bold=False)
instruction2 = gamebox.from_text(400, 350, "Press O to restart game", 40, "green", bold=False)
youLose = gamebox.from_text(400, 250, "Game Over", 120, "green", bold=True)
youWin = gamebox.from_text(400, 250, "You Win", 120, "green", bold=True)
restart = gamebox.from_text(400, 350, "Restart", 80, "black", bold=True)
restartBox = gamebox.from_color(400, 350, 'green', 275, 100)
nextLevel = gamebox.from_text(400, 300, "Next Level", 80, "black", bold=True)
nextLevelBox = gamebox.from_color(400, 300, 'green', 400, 100)

char = gamebox.from_image(400, 50, "meatboi.png")
char.scale_by(.3)
walls = [
    gamebox.from_color(0, 300, "black", 10, 600),
    gamebox.from_color(800, 300, "black", 10, 1000)
]
gamewalls = [
    gamebox.from_color(50, 300, "yellow", 100, 600),
    gamebox.from_color(750, 300, "yellow", 100, 600),
]
plat = gamebox.from_color(400, 0, "black", 800, 50)
safe = gamebox.from_color(400, 50, 'yellow', 800, 50)
plat1 = gamebox.from_color(400, 100, "black", 800, 50)
safe1 = gamebox.from_color(400, 150, 'yellow', 800, 50)
plat2 = gamebox.from_color(400, 200, "black", 800, 50)
safe2 = gamebox.from_color(400, 250, 'yellow', 800, 50)
plat3 = gamebox.from_color(400, 300, "black", 800, 50)
safe3 = gamebox.from_color(400, 350, 'yellow', 800, 50)
plat4 = gamebox.from_color(400, 400, "black", 800, 50)
safe4 = gamebox.from_color(400, 450, 'yellow', 800, 50)
plat5 = gamebox.from_color(400, 500, "black", 800, 50)
safe5 = gamebox.from_color(400, 550, 'yellow', 800, 50)
plat6 = gamebox.from_color(400, 600, "black", 800, 50)

car = gamebox.from_image(0, 100, "car1.png")
car.scale_by(0.1)
car1 = gamebox.from_image(0, 200, "car1.png")
car1.scale_by(0.1)
car2 = gamebox.from_image(0, 300, "car1.png")
car2.scale_by(0.1)
car3 = gamebox.from_image(0, 400, "car1.png")
car3.scale_by(0.1)
car4 = gamebox.from_image(0, 500, "car1.png")
car4.scale_by(0.1)
spd = random.randint(1, 5)
spd1 = random.randint(1, 5)
spd2 = random.randint(1, 5)
spd3 = random.randint(1, 5)
spd4 = random.randint(1, 5)
aspd = random.randint(1, 5)
aspd1 = random.randint(5, 12)
aspd2 = random.randint(5, 12)
aspd3 = random.randint(5, 12)
aspd4 = random.randint(5, 12)
bspd = random.randint(5, 15)
bspd1 = random.randint(3, 5)
bspd2 = random.randint(5, 15)
bspd3 = random.randint(3, 5)
bspd4 = random.randint(5, 15)
cspd = random.randint(10, 15)
cspd1 = random.randint(3, 10)
cspd2 = random.randint(10, 15)
cspd3 = random.randint(3, 10)
cspd4 = random.randint(10, 15)
cspd = random.randint(10, 20)
cspd1 = random.randint(3, 12)
cspd2 = random.randint(10, 10)
cspd3 = random.randint(3, 12)
cspd4 = random.randint(10, 20)
size = random.randint(40, 200)
size1 = random.randint(40, 200)
size2 = random.randint(40, 200)
size3 = random.randint(40, 200)
size4 = random.randint(40, 200)
game_on = False
level1 = False
level2 = False
level3 = False
level4 = False
timerStatus = False
restarts = False
timer = 500
lives = 0
reallives = 5 - lives
count = 0


def tick(keys):
    '''
    Param: keys: Everytime keys are pressed it runs it through the code while the game is 'ticking' frame by frame 
    '''
    global plat
    global safe
    global car
    global car1
    global car2
    global car3
    global car4
    global spd
    global spd1
    global spd2
    global spd3
    global spd4
    global score
    global game_on
    global level1
    global level2
    global level3
    global level4
    global timer
    global timerStatus
    global restarts
    global levelcount
    global scoretotal
    global lives
    global count
    lives1 = gamebox.from_text(100, 50, 'Lives: ' + str(5 - lives), 50, "black", bold=True)
    count1 = gamebox.from_text(100, 100, 'Lives: ' + str(count), 50, "black", bold=True)
    scoretotal = 0
    scoreList = []
    reallevel = levelcount + 1
    levelStat = gamebox.from_text(700, 50, 'Level: ' + str(reallevel), 50, "green", bold=True)
    if restarts == False:
        timer = 500
        gametime = timer - score
        game_on = True
        score += 1
        gameScore = gamebox.from_text(675, 550, 'Time Left: ' + str(gametime), 40, "red", bold=True)
        size = random.randint(40, 200)
        size1 = random.randint(40, 200)
        size2 = random.randint(40, 200)
        size3 = random.randint(40, 200)
        size4 = random.randint(40, 200)
        car.x += spd
        car1.x += spd1
        car2.x += spd2
        car3.x += spd3
        car4.x += spd4
        '''
        Movement, no upward movement to increase pace
        '''
        if pygame.K_LEFT or pygame.K_RIGHT in keys:
            game_on = True
        if pygame.K_LEFT in keys:
            char.x -= player_speed
        if pygame.K_RIGHT in keys:
            char.x += player_speed
        if pygame.K_DOWN in keys:
            char.y += player_speed

        for each in gamewalls:
            if char.touches(each):
                char.move_to_stop_overlapping(each)
        '''
        This part of the code resets each car at a given speed
        '''
        if car.touches(walls[1]):
            spd = random.randint(1, 5)
            car.x += spd
            car = gamebox.from_image(0, 100, "car1.png")
            car.scale_by(0.1)
        if car1.touches(walls[1]):
            spd1 = random.randint(1, 5)
            car1.x += spd1
            car1 = gamebox.from_image(0, 200, "car1.png")
            car1.scale_by(0.1)
        if car2.touches(walls[1]):
            spd2 = random.randint(1, 5)
            car2.x += spd2
            car2 = gamebox.from_image(0, 300, "car1.png")
            car2.scale_by(0.1)
        if car3.touches(walls[1]):
            spd3 = random.randint(1, 5)
            car3.x += spd3
            car3 = gamebox.from_image(0, 400, "car1.png")
            car3.scale_by(0.1)
        if car4.touches(walls[1]):
            spd4 = random.randint(1, 5)
            car4.x += spd4
            car4 = gamebox.from_image(0, 500, "car1.png")
            car4.scale_by(0.1)

        camera.clear('black')
        camera.draw(plat)
        camera.draw(safe)
        camera.draw(plat1)
        camera.draw(safe1)
        camera.draw(plat2)
        camera.draw(safe2)
        camera.draw(plat3)
        camera.draw(safe3)
        camera.draw(plat4)
        camera.draw(safe4)
        camera.draw(plat5)
        camera.draw(safe5)
        camera.draw(plat6)
        camera.draw(car)
        camera.draw(car1)
        camera.draw(car2)
        camera.draw(car3)
        camera.draw(car4)
        camera.draw(char)
        '''
        This section outlines the level function based on a selection of boolean expressions
        '''
        if char.touches(plat6):
            count = count + 1
        if char.touches(plat6) and level1 == False and count == 1:
            level1 = True
            char.center = [400, 50]
            score = 0
            levelcount = 1
            scoreList.append(score)
        if char.touches(plat6) and level1 == True and count == 2:
            level2 = True
            char.center = [400, 50]
            score = 0
            levelcount = 2
            scoreList.append(score)
        if char.touches(plat6) and level2 == True and level1 == True and count == 3:
            level3 = True
            char.center = [400, 50]
            score = 0
            levelcount = 3
            scoreList.append(score)
        if char.touches(plat6) and level3 == True and level2 == True and level1 == True and count == 4:
            level4 = True
            char.center = [400, 50]
            score = 0
            levelcount = 4
            scoreList.append(score)
        if count >= 5:
            camera.draw(youWin)
            restarts = True
        '''
        This area draws the level counter for each level
        '''
        for each in gamewalls:
            camera.draw(each)
        if level1 == False:
            camera.draw(levelStat)
        if level1 == True:
            camera.draw(levelStat)
        if level2 == True:
            camera.draw(levelStat)
        if level3 == True:
            camera.draw(levelStat)
        '''
        This section determines how the character interacts with the timer and the cars: if the character gets hit or the timer runs out, the restarts boolean becomes true. Also it pushes the cars forward so they reset correctly
        '''
        if char.touches(car) or char.touches(car1) or char.touches(car2) or char.touches(car3) or char.touches(
                car4) or gametime <= 0:
            lives = lives + 1
            if lives < 5:
                camera.draw(instruction1)
            if lives >= 5:
                camera.draw(instruction2)
                camera.draw(youLose)
            restarts = True
            car = gamebox.from_image(700, 100, "car1.png")
            car.scale_by(0.1)
            car1 = gamebox.from_image(700, 200, "car1.png")
            car1.scale_by(0.1)
            car2 = gamebox.from_image(700, 300, "car1.png")
            car2.scale_by(0.1)
            car3 = gamebox.from_image(700, 400, "car1.png")
            car3.scale_by(0.1)
            car4 = gamebox.from_image(700, 500, "car1.png")
            car4.scale_by(0.1)
        camera.draw(gameScore)
        keys.clear()
        camera.draw(lives1)
        camera.display()
    '''
    This section outlines how each level will work in terms of car speed, it ascends upward so as the levels increase, the car speeds increase. There is also sections where the car speeds vary between platforms within the level for pacing reasons
    '''
    if level1 == False:

        car.x += spd
        car1.x += spd1
        car2.x += spd2
        car3.x += spd3
        car4.x += spd4

        if car.touches(walls[1]):
            spd = random.randint(1, 5)
            car.x += spd
            size = random.randint(40, 200)
            car = gamebox.from_image(0, 100, "car1.png")
            car.scale_by(0.1)
        if car1.touches(walls[1]):
            spd1 = random.randint(1, 5)
            car1.x += spd1
            size1 = random.randint(40, 200)
            car1 = gamebox.from_image(0, 200, "car1.png")
            car1.scale_by(0.1)
        if car2.touches(walls[1]):
            spd2 = random.randint(1, 5)
            car2.x += spd2
            size2 = random.randint(40, 200)
            car2 = gamebox.from_image(0, 300, "car1.png")
            car2.scale_by(0.1)
        if car3.touches(walls[1]):
            spd3 = random.randint(1, 5)
            car3.x += spd3
            size3 = random.randint(40, 200)
            car3 = gamebox.from_image(0, 400, "car1.png")
            car3.scale_by(0.1)
        if car4.touches(walls[1]):
            spd4 = random.randint(1, 5)
            car4.x += spd4
            size4 = random.randint(40, 200)
            car4 = gamebox.from_image(0, 500, "car1.png")
            car4.scale_by(0.1)
    if level1 == True:

        car.x += aspd
        car1.x += aspd1
        car2.x += aspd2
        car3.x += aspd3
        car4.x += aspd4

        if car.touches(walls[1]):
            spd = random.randint(5, 12)
            car.x += spd
            size = random.randint(40, 200)
            car = gamebox.from_image(0, 100, "car1.png")
            car.scale_by(0.1)
        if car1.touches(walls[1]):
            spd1 = random.randint(5, 12)
            car1.x += spd1
            size1 = random.randint(40, 200)
            car1 = gamebox.from_image(0, 200, "car1.png")
            car1.scale_by(0.1)
        if car2.touches(walls[1]):
            spd2 = random.randint(5, 12)
            car2.x += spd2
            size2 = random.randint(40, 200)
            car2 = gamebox.from_image(0, 300, "car1.png")
            car2.scale_by(0.1)
        if car3.touches(walls[1]):
            spd3 = random.randint(5, 12)
            car3.x += spd3
            size3 = random.randint(40, 200)
            car3 = gamebox.from_image(0, 400, "car1.png")
            car3.scale_by(0.1)
        if car4.touches(walls[1]):
            spd4 = random.randint(5, 12)
            car4.x += spd4
            size4 = random.randint(40, 200)
            car4 = gamebox.from_image(0, 500, "car1.png")
            car4.scale_by(0.1)
    if level1 == True and level2 == True:

        car.x += bspd
        car1.x += bspd1
        car2.x += bspd2
        car3.x += bspd3
        car4.x += bspd4

        if car.touches(walls[1]):
            spd = random.randint(5, 15)
            car.x += spd
            size = random.randint(40, 200)
            car = gamebox.from_image(0, 100, "car1.png")
            car.scale_by(0.1)
        if car1.touches(walls[1]):
            spd1 = random.randint(3, 5)
            car1.x += spd1
            size1 = random.randint(40, 200)
            car1 = gamebox.from_image(0, 200, "car1.png")
            car1.scale_by(0.1)
        if car2.touches(walls[1]):
            spd2 = random.randint(5, 15)
            car2.x += spd2
            size2 = random.randint(40, 200)
            car2 = gamebox.from_image(0, 300, "car1.png")
            car2.scale_by(0.1)
        if car3.touches(walls[1]):
            spd3 = random.randint(3, 5)
            car3.x += spd3
            size3 = random.randint(40, 200)
            car3 = gamebox.from_image(0, 400, "car1.png")
            car3.scale_by(0.1)
        if car4.touches(walls[1]):
            spd4 = random.randint(5, 15)
            car4.x += spd4
            size4 = random.randint(40, 200)
            car4 = gamebox.from_image(0, 500, "car1.png")
            car4.scale_by(0.1)
    if level1 == True and level2 == True and level3 == True:

        car.x += bspd
        car1.x += bspd1
        car2.x += bspd2
        car3.x += bspd3
        car4.x += bspd4

        if car.touches(walls[1]):
            spd = random.randint(10, 15)
            car.x += spd
            size = random.randint(100, 200)
            car = gamebox.from_image(0, 100, "car1.png")
            car.scale_by(0.1)
        if car1.touches(walls[1]):
            spd1 = random.randint(3, 10)
            car1.x += spd1
            size1 = random.randint(100, 200)
            car1 = gamebox.from_image(0, 200, "car1.png")
            car1.scale_by(0.1)
        if car2.touches(walls[1]):
            spd2 = random.randint(10, 15)
            car2.x += spd2
            size2 = random.randint(100, 200)
            car2 = gamebox.from_image(0, 300, "car1.png")
            car2.scale_by(0.1)
        if car3.touches(walls[1]):
            spd3 = random.randint(3, 10)
            car3.x += spd3
            size3 = random.randint(100, 200)
            car3 = gamebox.from_image(0, 400, "car1.png")
            car3.scale_by(0.1)
        if car4.touches(walls[1]):
            spd4 = random.randint(10, 15)
            car4.x += spd4
            size4 = random.randint(100, 200)
            car4 = gamebox.from_image(0, 500, "car1.png")
            car4.scale_by(0.1)
    if level1 == True and level2 == True and level3 == True and level4 == True:

        car.x += bspd
        car1.x += bspd1
        car2.x += bspd2
        car3.x += bspd3
        car4.x += bspd4

        if car.touches(walls[1]):
            spd = random.randint(10, 20)
            car.x += spd
            size = random.randint(100, 200)
            car = gamebox.from_image(0, 100, "car1.png")
            car.scale_by(0.1)
        if car1.touches(walls[1]):
            spd1 = random.randint(3, 12)
            car1.x += spd1
            size1 = random.randint(100, 200)
            car1 = gamebox.from_image(0, 200, "car1.png")
            car1.scale_by(0.1)
        if car2.touches(walls[1]):
            spd2 = random.randint(10, 20)
            car2.x += spd2
            size2 = random.randint(100, 200)
            car2 = gamebox.from_image(0, 300, "car1.png")
            car2.scale_by(0.1)
        if car3.touches(walls[1]):
            spd3 = random.randint(3, 12)
            car3.x += spd3
            size3 = random.randint(100, 200)
            car3 = gamebox.from_image(0, 400, "car1.png")
            car3.scale_by(0.1)
        if car4.touches(walls[1]):
            spd4 = random.randint(10, 20)
            car4.x += spd4
            size4 = random.randint(100, 200)
            car4 = gamebox.from_image(0, 500, "car1.png")
            car4.scale_by(0.1)
    '''
    This is the restarts section of the code, where everything happens when the character dies. It's a colleciton of if statements that tells the game what to do if the character loses all the lives, wins the game, etc
    '''
    if restarts == True:
        score = 0
        if lives < 5 and count <= 5:
            if (pygame.K_r in keys) and (restarts == True or timerStatus == True) and count <= 4:
                restarts = False
                char.center = [400, 50]
            if (pygame.K_o in keys) and (restarts == True or timerStatus == True) and count <= 4:
                levelcount = 0
                restarts = False
                level1 = False
                level2 = False
                char.center = [400, 50]
                lives = 0
                count = 0
        if lives < 5 and count >= 5:
            if (pygame.K_o in keys) and (restarts == True or timerStatus == True) and count >= 4:
                levelcount = 0
                restarts = False
                level1 = False
                level2 = False
                char.center = [400, 50]
                lives = 0
                count = 0
        else:
            if (pygame.K_o in keys) and (restarts == True or timerStatus == True):
                levelcount = 0
                restarts = False
                level1 = False
                level2 = False
                char.center = [400, 50]
                lives = 0
                count = 0
    if count >= 5 and lives < 5:
        camera.draw(instruction2)
    camera.display()


gamebox.timer_loop(60, tick)
