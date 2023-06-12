import random
print("\tWelcome to 'Guess My Number'!")
print("\nI'm thinking of a number between 1 and 100.")
print("Try to guess it with in five attempts.\n")

the_number = random.randint(1,100)
guess = int(input("Take a guess: "))
tries = 1

while tries != 6:
   if guess == the_number:
      print("You guessed it! The numder was", the_number)
      input("\n\nPress the enter key to exit")
      break
   elif tries == 5:
      print("Looks like someone can't count. It was", the_number)
      input("\n\nPress the enter key to exit")
      break
   elif guess < the_number:
      print("Higher...")
   else:
      print("Lower...")
      
   guess = int(input("Take a guess: "))
   tries += 1