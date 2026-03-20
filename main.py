
import turtle
import random


screen = turtle.Screen()
t = turtle.Turtle()
t.hideturtle()

choices = ["rock", "paper", "scissors"]

def get_choice():
    while True:
        player = turtle.textinput(
            "Rock Paper Scissors",
            "Type: rock, paper, or scissors"
        )

        if player is None:
            return None 

        player = player.lower()

        if player in choices:
            return player
        else:
            turtle.clear()
            turtle.write(" Invalid! Type rock, paper, or scissors",
                         align="center", font=("Arial", 16, "bold"))


player = get_choice()

if player:
    computer = random.choice(choices)

    turtle.clear()
    turtle.write(f"You: {player}\nComputer: {computer}",
                 align="center", font=("Arial", 16, "bold"))

    
    if player == computer:
        turtle.goto(0, -40)
        turtle.write(" Tie!", align="center", font=("Arial", 16, "bold"))

    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):

        turtle.goto(0, -40)
        turtle.write("🎉 You Win!", align="center", font=("Arial", 16, "bold"))

    else:
        turtle.goto(0, -40)
        turtle.write(" You Lose!", align="center", font=("Arial", 16, "bold"))

turtle.done()

