from random import randint
import os
import sys

def clearPage():
    if sys.platform.startswith('win'):
        os.system('cls')
    else:
        os.system('clear')



lists = ["", "Rock", "Paper", "Scissor"]

print(f"\n1 -  Rock   - 1\n2 -  Paper  - 2\n3 - Scissor - 3\n\n0 - Exit - 0\n")

sts = 0;
score = {"user": 0, "bot": 0}

def gameWon(user, bot):
    if user == bot:
        return "draw";
    elif user == 1:
        if bot == 2:
            return "bot"
        else:
            return "user"
    elif user == 2:
        if bot == 3:
            return "bot"
        else:
            return "user"
    elif user == 3:
        if bot == 1:
            return "bot"
        else:
            return "user"


def gameStart(new, user, bot):
    clearPage()
    print(f"1 -  Rock   - 1\n2 -  Paper  - 2\n3 - Scissor - 3\n\n0 - Exit - 0\n\n")
    print(f"(You: {lists[user]}) ....VS.... (Bot: {lists[bot]})")
    
    who = gameWon(user, bot)
    if who == "draw":
        print("\n....DRAW....")
    elif who == "user":
        score["user"] += 1
        print("\n....You Won This Round!....")
    elif who == "bot":
        score["bot"] += 1
        print("\n....You Lost This Round!....")

    print(f"\n ---------------\n| Your Score: {score["user"]} |\n| Bot Score : {score["bot"]} |\n ---------------\n")

def FinalScoreShowIssueFix(sw=404):
    if score["user"] == 10 or score["bot"] == 10:
        if sw == 0:
            print(f"\n ---------------\n| Your Score: {score["user"]} |\n| Bot Score : 0{score["bot"]} |\n ---------------\n")
        elif sw == 1:
            print(f"\n ---------------\n| Your Score: 0{score["user"]} |\n| Bot Score : {score["bot"]} |\n ---------------\n")
        else:
            print(f"\n ---------------\n| Your Score: {score["user"]} |\n| Bot Score : {score["bot"]} |\n ---------------\n")
    else:
            print(f"\n ---------------\n| Your Score: {score["user"]} |\n| Bot Score : {score["bot"]} |\n ---------------\n")
def endGame():
    clearPage()
    if score["user"] == 0 and score["bot"] == 0:
        FinalScoreShowIssueFix()
        print("YOU'RE A PU8SY")
    elif score["user"] > score["bot"]:
        FinalScoreShowIssueFix(0)
        print(f"\n.....!YOU WON!.....")
    elif score["user"] < score["bot"]:
        FinalScoreShowIssueFix(1)
        print(f"\n.....!YOU ARE A LOOSER!.....")
    elif score["user"] == score["bot"]:
        FinalScoreShowIssueFix()
        print(f"\n.....!WELL IT'S A DRAW!.....")

    input("\n\nPress Enter To Exit")


while True:
    try:
        
        if score["user"] == 10 or score["bot"] == 10:
            endGame();
            break;
            
        user = int(input(f"\n----------------\nYour Choice? "))
        bot = randint(1,3)
            
        if user < 0 or user > 3:
            print("Enter a Valid Option...")
        else:
            if sts==0:
                sts = 1;
                if user==0:
                    endGame();
                    break;
                else:
                    gameStart(1, user, bot);
            elif sts==1:
                if user==0:
                    endGame();
                    break;
                else:
                    gameStart(0, user, bot);
            else:
                break;
    except ValueError:
        print("What tf You Doing?...")
