from random import randint
import turtle
import time


WIDTH=1200
HEIGHT=600
PLAYER_SPEED = 5
#def init_game ():



#Creating the game's play screen
screen = turtle.Screen()
screen.tracer(0)
screen.title("PONG GAME BY SIGAL")
screen.bgcolor("pink")
screen.setup(width=WIDTH, height=HEIGHT)
#Updating score in the scoreboard




# screen_rect = turtle.Turtle()
# screen_rect.speed(0)
# screen_rect.shape("square")
# SCREEN_RECT_WIDTH = WIDTH / 2 / 10
# SCREEN_RECT_HEIGHT = HEIGHT / 2 /10
# screen_rect.shapesize(SCREEN_RECT_HEIGHT ,SCREEN_RECT_WIDTH, 1)
# # screen_rect.color("grey")

# # screen_rect.shapesize(stretch_wid=6, stretch_len=2)
# screen_rect.penup()
# screen_rect.goto(0, 0)
# screen_rect.write("shit")
# screen_rect.write(arg='score:', move=True, align='center', font=("arial", 50, "normal"))



#Creating the paddles
#Right paddle
right_paddle = turtle.Turtle()
right_paddle.speed(0)
right_paddle.shape("square")
RIGHT_PADDLE_WIDTH = 10
RIGHT_PADDLE_HEIGHT = 40
right_paddle.shapesize(RIGHT_PADDLE_HEIGHT / 10 , RIGHT_PADDLE_WIDTH / 10,1)
right_paddle.color("white")
# right_paddle.shapesize(stretch_wid=6, stretch_len=2)
right_paddle.penup()
right_paddle.goto(WIDTH / 2 - RIGHT_PADDLE_WIDTH*3, 0)

#Left paddle
left_paddle = turtle.Turtle()
left_paddle.speed(0)
left_paddle.shape("square")
LEFT_PADDLE_WIDTH = 10
LEFT_PADDLE_HEIGHT = 40
left_paddle.shapesize(LEFT_PADDLE_HEIGHT / 10 ,LEFT_PADDLE_WIDTH / 10, 1)
left_paddle.color("white")
# left_paddle.shapesize(stretch_wid=6, stretch_len=2)
left_paddle.penup()
left_paddle.goto(-WIDTH / 2 + RIGHT_PADDLE_WIDTH*3, 0)


#Ball 
ball = turtle.Turtle()
#ball.speed(1)
ball.shape("circle")
BALL_RADIUS = 10
ball.shapesize(BALL_RADIUS/10, BALL_RADIUS/10,1)
ball.color("black")
ball.penup()
ball.goto(0, 0)
#ball.dx = 5
#ball.dy = -5
txt = turtle.Turtle()
txt.color("white")
txt.penup()
top_height = HEIGHT / 2  # positive height/2 is the top of the screen
y = top_height - top_height/4  # decreasing a little bit so text will be visible
txt.setposition(-150, y)
txt.write(arg='Player A:', move=True, align='left', font=("arial", 10, "bold"))
txt.setposition(100, y)
txt.write(arg='Player B:', move=True, align='center', font=("arial", 10, "bold"))


txt.setposition(0, y)
txt.write(arg= '|' ,move=True, align='center', font=("arial", 10, "bold"))
txt.setposition(0, y )
txt.write(arg= '|' ,move=True, align='center', font=("arial", 10, "bold"))
txt.setposition(0, y - 50)
txt.write(arg= '|' ,move=True, align='center', font=("arial", 10, "bold"))
txt.setposition(0, y - 100)
txt.write(arg= '|' ,move=True, align='center', font=("arial", 10, "bold"))
txt.setposition(0, y - 150)
txt.write(arg= '|' ,move=True, align='center', font=("arial", 10, "bold"))
txt.setposition(0, y - 200)
txt.write(arg= '|' ,move=True, align='center', font=("arial", 10, "bold"))
txt.setposition(0, y - 250)
txt.write(arg= '|' ,move=True, align='center', font=("arial", 10, "bold"))
txt.setposition(0, y - 300)
txt.write(arg= '|' ,move=True, align='center', font=("arial", 10, "bold"))
txt.setposition(0, y - 350)
txt.write(arg= '|' ,move=True, align='center', font=("arial", 10, "bold"))
txt.setposition(0, y - 400)
txt.write(arg= '|' ,move=True, align='center', font=("arial", 10, "bold"))
txt.setposition(0, y - 450)
txt.write(arg= '|' ,move=True, align='center', font=("arial", 10, "bold"))
txt.setposition(0, y - 500)
txt.write(arg= '|' ,move=True, align='center', font=("arial", 10, "bold"))

# def motion(event):
#     x, y = event.x, event.y
#     print('{}, {}'.format(x, y))

# canvas = turtle.getcanvas()
# canvas.bind('<Motion>', motion)

def handle_screen_collision(direction):
    if abs(ball.ycor())+ BALL_RADIUS >= HEIGHT/2 :
        direction = turtle.Vec2D(direction[0] ,-direction[1])
    return direction

class players:
    LEFT = 0
    RIGHT = 1

def check_who_won():
    who_won = -1 # 0 for left win ; 1 for right win
    if ball.xcor() + BALL_RADIUS >= WIDTH/2 :
        who_won = players.LEFT
    if ball.xcor() - BALL_RADIUS <= -WIDTH/2 :
        who_won = players.RIGHT
    return who_won

def handle_paddle_collision(direction):
    if ball.xcor()- BALL_RADIUS <= left_paddle.xcor() + LEFT_PADDLE_WIDTH/2:
        if ball.ycor() + BALL_RADIUS >= left_paddle.ycor() - LEFT_PADDLE_HEIGHT / 2 and ball.ycor() - BALL_RADIUS <= left_paddle.ycor() + LEFT_PADDLE_HEIGHT / 2:
            direction = turtle.Vec2D(-direction[0] ,direction[1])
    if ball.xcor() + BALL_RADIUS >= right_paddle.xcor() - RIGHT_PADDLE_WIDTH/2:
        if ball.ycor() + BALL_RADIUS >= right_paddle.ycor() - RIGHT_PADDLE_HEIGHT / 2 and ball.ycor() - BALL_RADIUS <= right_paddle.ycor() + RIGHT_PADDLE_HEIGHT /2 :
            direction = turtle.Vec2D(-direction[0] ,direction[1])
    return direction

def game_loop():
    gravity = -0.05   # pixels/(time of iteration)^2
    velocity = 4   # pixels/(time of iteration)
    right_score = 0
    left_score = 0
    
    direction = turtle.Vec2D(1,0).rotate(randint(1,360)) # initialized with a random direction
    
    while True:
        
        screen.update()
        # move ball
        ball.setx(ball.xcor() + velocity*direction[0])
        ball.sety(ball.ycor() + velocity*direction[1])
        
        direction = handle_paddle_collision(direction)
        direction = handle_screen_collision(direction)   
        
        who_won = check_who_won()
        if who_won != -1:
            if who_won == players.LEFT:
                left_score += 1   
                print("Left Scored a point!!!")  
            if who_won == players.RIGHT:
                right_score += 1
                print("Right Scored a point!!!")  
            ball.goto(0,0)
            direction = turtle.Vec2D(1,0).rotate(randint(1,360)) # initialized with a random direction
        
        time.sleep(10/1000)
        # right_paddle.ondrag(right_paddle_move)
        Keyboard_moves()

#turtle.write("Player A:  Player B: ", font=("Verdana",50, "normal"), align="left")


def move_left_paddle_up ():
    left_paddle.sety(left_paddle.ycor() + PLAYER_SPEED)
    if( left_paddle.ycor() + LEFT_PADDLE_HEIGHT >= HEIGHT / 2):
        left_paddle.sety(HEIGHT / 2 - LEFT_PADDLE_HEIGHT )
    
def move_left_paddle_down ():
    left_paddle.sety(left_paddle.ycor() - PLAYER_SPEED)
    if(left_paddle.ycor() - LEFT_PADDLE_HEIGHT <= -HEIGHT / 2):
        left_paddle.sety(-HEIGHT / 2 + LEFT_PADDLE_HEIGHT )

def move_right_paddle_up ():
    right_paddle.sety(right_paddle.ycor() + PLAYER_SPEED)
    if( right_paddle.ycor() + RIGHT_PADDLE_HEIGHT >= HEIGHT / 2):
        right_paddle.sety(HEIGHT / 2 - RIGHT_PADDLE_HEIGHT )
    
def move_right_paddle_down ():
    right_paddle.sety(right_paddle.ycor() - PLAYER_SPEED)
    if(right_paddle.ycor() - RIGHT_PADDLE_HEIGHT <= -HEIGHT / 2):
        right_paddle.sety(-HEIGHT / 2 + RIGHT_PADDLE_HEIGHT )



def Keyboard_moves():
    screen.listen()
    # left
    screen.onkeypress(move_left_paddle_up, "w")
    screen.onkeypress(move_left_paddle_down, "s")

    # right
    screen.onkeypress(move_right_paddle_up, "Up")
    screen.onkeypress(move_right_paddle_down, "Down")
 

def right_paddle_move(x,y):
   right_paddle.goto(right_paddle.xcor(), y)

def main():
    #init_game()
    game_loop()


if __name__ == "__main__":
    main()
    



 

