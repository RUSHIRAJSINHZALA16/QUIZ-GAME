# this my first project in python
print("WELCOME to RUSHiRAJ's QUIZ!")

player=input("DO you want to play QUIZ?")
score = 0
if player.lower() !="yes":
    quit()
else:
    print("Okay Let'play :)")

answer=input("what is the full form of CPU? ")
if answer.lower() == "central processing unit":
    print("correct!")
    score +=1
else:
    print("incorrect")

answer=input("what is the full form of GPU? ")
if answer.lower() == "graphics processing unit":
    print("correct!")
    score +=1
else:
    print("incorrect")

answer=input("what is the full form of RAM? ")
if answer.lower() == "random access memory":
    print("correct!")
    score +=1
else:
    print("incorrect")

answer=input("what is the full form of ROM? ")
if answer.lower() == "read only memory":
    print("correct!")
    score+=1
else:
    print("incorrect")

answer=input("what is the full form of WiFi? ")
if answer.lower() == "wireless fidelity":
    print("correct!")
    score +=1
else:
    print("incorrect")
print("******************************************")
print("you got "+str(score)+ " questions correct!")
print("you scored "+str((score/5)*100 )+"%.")
print("******************************************")
print("thanks for playing made by rushirajsinh zala")