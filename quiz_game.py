print("welcome to my computer quiz")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()
else:
    print("ok let's play!")

score = 0

answer = input("what does CPU stands for? ")
if answer.lower() == "central processing unit":
    print("correct!")p
    score+=1
else:
    print("incorrect")

answer = input("what does GPU stands for? ")
if answer.lower() == "graphics processing unit":
    print("correct!")
    score+=1
else:
    print("incorrect")

answer = input("what does RAM stands for? ")
if answer.lower() == "Random access memory":
    print("correct!")
    score+=1
else:
    print("incorrect")

answer = input("what does rom stands for? ")
if answer.lower() == "read only memory":
    print("correct!")
    score+=1
else:
    print("incorrect")

answer = input("what does psu stands for? ")
if answer.lower() == "power supply":
    print("correct!")
    score+=1
else:
    print("incorrect")

print("you got " + str(score) + " question correct out of 5")
print("you got " + str((score/5)*100) +" percentage" )
