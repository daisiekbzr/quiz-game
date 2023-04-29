print("Welcome to my Makise Kurisu Quiz Game!")

playing = input("Do you want to play?(yes/no) ")

if playing !=  "yes":
    quit()

print("Ok! Let's Play!")
score = 0

# Question 1

answer = input("What color is Makise's hair? ")

if answer == "red":
    print("Correct!")
    score += 1
else:
    print("Wrong...")

# Question 2

answer = input("What is her profession? ")

if answer == "scientist":
    print("Correct!")
    score += 1
else:
    print("Wrong...")

# Question 3

answer = input("Which number lab member is she? ")

if answer == "004":
    print("Correct!")
    score += 1
else:
    print("Wrong...")

# Question 4

answer = input("How old is she? ")

if answer == "18":
    print("Correct!")
    score += 1
else:
    print("Wrong...")

# Question 5

answer = input("What did she help invent? ")

if answer == "time machine":
    print("Correct!")
    print("Thank you for playing! :)")
    score += 1
else:
    print("Wrong...")

print("You got " + str(score) + " out of 5 points!")
print("You got " + str((score/5)*100) + "%.")