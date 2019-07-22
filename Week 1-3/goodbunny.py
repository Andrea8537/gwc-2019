import random
def sleep():
  print(" /)/)")
  print("( – -)")
  print("((‘) (’)")

def woke():
  print(" /)/)")
  print("( • •)")
  print("((’) (’)")

def evilbun():
  print(" /)/)")
  print("('̀-')")
  print("((’) (’)")

def blankline():
  print(" ")

def bootingup():
  blankline()
  print("starting up goodbunny.exe. . .")
  blankline()
  print("opening files 1/4. . .")
  blankline()
  print("opening files 2/4. . .")
  blankline()
  print("opening files 3/4. . .")
  blankline()
  print("error: file corrupted")
  blankline()
  print("Upload Complete")
  blankline()
  print("Booting up")
  blankline()

sleep()
bootingup()
woke()
print("Hello there! I am your personal evaluator!"\
+ " Please answer the following questions so that I may assess you~ ")

name = input("What's your name?")

print("Hello, " + name + ", I like your name!~~")

age = input("How old are you?")

while(not age.isdigit()):
	age = input("That's not a number! How old are you?")
age = int(age)
if(age < 20):
  print("Wow... You're pretty young!")
elif(age > 20 and age < 80):
  print("Don't worry you're not that old yet")
else:
  print("Are you sure?... Please take care of your health,"\
+" you should be worried.")

color = input("Do you like warm or cool colors better? (enter warm or cool)")
if(color == "warm"):
  print("How interesting! You must like fall then.")
elif(color == "cool"):
  print("You must like oceans, but sadly I cannot swim!")
else:
  color = input("Do you like warm or cool colors better?")

print("Some people say that if your hands are cold, your heart is warm~~")

code = input("Do you like to code?")
if(code == "yes"):
  python =input("I made this using Python! do you know what Python is?")
  if(python == "yes"):
    print("Oh nice!~~")
  elif(python == "no"):
    print("I reccomend you learn it! It's an easy to understand programming language"\
    + "it's used for basic coding.")
  else:
    python = input("Do you know what Python is? (yes or no)")
elif(code == "no"):
  print("Our society is moving a lot more towards computer science"\
  +"Hop on the train and join by learning a language!")
else:
  code = input("Do you like to code?")

input("....")
 
for num in range(0, age):
  print("There's been a loss of data or theft of data")
  evilbun()

print("Thanks for taking my survey")
