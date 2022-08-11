import random

correct_answer = 0
wrong_answer = 0
print("Welcome to my computer quiz!")

playing = input("Do you want to play Y/N? ")
if playing.lower() != "yes":
    quit()

print("Okay! Let's play :")

answer = input("What does Cpu stand for? ")
if answer.lower() == "central processing unit":
    print("Correct! ")
    correct_answer += 1
else:
    print("Incorrect! ")
    wrong_answer += 1

answer = input("What does GPU stands for? ")
if answer.lower() == "graphics processing unit":
    print("Correct! ")
    correct_answer += 1
else:
    print("Incorrect! ")
    wrong_answer += 1

answer = input("What does Ram stands for? ")
if answer.lower() == "random access memory":
    print("Correct! ")
    correct_answer += 1
else:
    print("Incorrect! ")
    wrong_answer += 1

answer = input("What does PSU stands for? ")
if answer.lower() == "power supply":
    print("Correct! ")
    correct_answer += 1
else:
    print("Incorrect! ")
    wrong_answer += 1

print("Great Game you got:", str(correct_answer), "Questions correct" " and", str(wrong_answer), " Questions Wrong")
print("you got", str((correct_answer / 4) * 100) + "%", " Correct")
