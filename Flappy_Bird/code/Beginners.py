# Baseline Beginners

# start modules
import pgzrun
import sys

# create constants
WIDTH = 800
HEIGHT = 600
score = 0

# print welcome
print("The game is about to start!")
print('Click the mouse to "flap" upwards')
print("Dodge the pipes and the floor")
print("Good luck and have fun!")

# make background 
background = Actor("bg")
background.x = 400
background.y = 300

# make bird
bird = Actor("bird")
bird.x = 160
bird.y = 300

# make pipes
topPipe1 = Actor("top")
topPipe1.x = 266
topPipe1.y = -10

bottomPipe1 = Actor("bottom")
bottomPipe1.x = 266
bottomPipe1.y = 800

topPipe2 = Actor("top")
topPipe2.x = 532
topPipe2.y = -200

bottomPipe2 = Actor("bottom")
bottomPipe2.x = 532
bottomPipe2.y = 560

topPipe3 = Actor("top")
topPipe3.x = 798
topPipe3.y = -120

bottomPipe3 = Actor("bottom")
bottomPipe3.x = 798
bottomPipe3.y = 710

# draw everything to screen
def draw():
    # draw background
    background.draw()
    # draw all characters
    bird.draw()
    topPipe1.draw()
    bottomPipe1.draw()
    topPipe2.draw()
    bottomPipe2.draw()
    topPipe3.draw()
    bottomPipe3.draw()

# updates everything
def update():
    global score
    # updating bird
    bird.y = bird.y + 1

    # updating pipes 
    topPipe1.x = topPipe1.x - 1
    if topPipe1.x < -44:
        topPipe1.x = WIDTH
        score = score + 1

    bottomPipe1.x = bottomPipe1.x - 1
    if bottomPipe1.x < -44:
        bottomPipe1.x = WIDTH

    topPipe2.x = topPipe2.x - 1
    if topPipe2.x < -44:
        topPipe2.x = WIDTH
        score = score + 1

    bottomPipe2.x = bottomPipe2.x - 1
    if bottomPipe2.x < -44:
        bottomPipe2.x = WIDTH

    topPipe3.x = topPipe3.x - 1
    if topPipe3.x < -44:
        topPipe3.x = WIDTH
        score = score + 1

    bottomPipe3.x = bottomPipe3.x - 1
    if bottomPipe3.x < -44:
        bottomPipe3.x = WIDTH

    # bird hits bottom of screen
    if bird.y > HEIGHT:
        print("Game Over!")
        print("Your score was:",str(score))
        sys.exit()

    # bird hits pipes
    if bird.colliderect(topPipe1):
        print("Game Over!")
        print("Your score was:",str(score))
        sys.exit()

    if bird.colliderect(bottomPipe1):
        print("Game Over!")
        print("Your score was:",str(score))
        sys.exit()

    if bird.colliderect(topPipe2):
        print("Game Over!")
        print("Your score was:",str(score))
        sys.exit()

    if bird.colliderect(bottomPipe2):
        print("Game Over!")
        print("Your score was:",str(score))
        sys.exit()

    if bird.colliderect(topPipe3):
        print("Game Over!")
        print("Your score was:",str(score))
        sys.exit()

    if bird.colliderect(bottomPipe3):
        print("Game Over!")
        print("Your score was:",str(score))
        sys.exit()

# moving
def on_mouse_down():
    bird.y = bird.y - 50

# runs everything
pgzrun.go() 
