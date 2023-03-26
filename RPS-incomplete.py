import random
import time

rock=1
paper=2
scissors=3

names={rock: "Rock" , paper: "Paper" , scissors: "Scissors"}
rules={rock: scissors , paper: rock, scissors: paper }
computer_score=0
player_score=0

def start():
    print("Hey,Lets play a game called Rock,paper,scissors!!")
    while game():
        pass
    scores()

def move():
   
    print
    player=input("Select a choice:\n1.Rock\n2.Paper\n3.Scissors\n")

    player=int(player)
    if player in (1,2,3):
        return player
    else:
        print("Oops,I didn't understand that.Please enter a choice of 1,2,3.")


def game():
    player=move()
    computer=random.randint(1,3)
    result(player,computer)
def result(player,computer):
    global player_score,computer_score
    print("Computer threw {0}!".format(names[computer]))
    if player==computer:
        print("Game Tie")
        
    else:
        if rules[player]==computer:
            print("Congrats!You Have Won")
            player_score+=1
        else:
            print("Computer laughs as you lost")
            computer_score+=1
def scores():
    global player_score,computer_score
    print("HIGH SCORES")
    print("player score: ",player_score)
    print("computer score: ", computer_score)
if __name__=='__main__':
    start()
