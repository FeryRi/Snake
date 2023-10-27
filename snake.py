from random import randrange
from turtle import *

from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

# Tamaño de la comida (aumentado)
food_size = 20

def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y

def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    rndomSnake = randrange (0,5)
    rndomFood = randrange (0,5)
    for body in snake:
        if rndomSnake != rndomFood:
            if (rndomFood ==0) or (rndomSnake==0): 
                square(body.x, body.y, 9, 'black')
                square(food.x, food.y, food_size, 'green')  # Aumenta el tamaño de la comida
            elif (rndomFood ==1) or (rndomSnake==1): 
                square(body.x, body.y, 9, 'blue')
                square(food.x, food.y, food_size, 'black')  # Aumenta el tamaño de la comida
            elif (rndomFood ==2) or (rndomSnake==2):
                square(body.x, body.y, 9, 'green')
                square(food.x, food.y, food_size, 'pink')  # Aumenta el tamaño de la comida
            elif (rndomFood ==3) or (rndomSnake==3): 
                square(body.x, body.y, 9, 'pink')
                square(food.x, food.y, food_size, 'blue')  # Aumenta el tamaño de la comida
            else:
                square(body.x, body.y, 9, 'yellow')
                square(food.x, food.y, food_size, 'orange')  # Aumenta el tamaño de la comida
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
