#print questions
#print the answer to question
#prompt the user input answer
#check for conditions

print("question")
user_choice = input("Do you want to play the game: yes/no ")
if user_choice == "yes":
  answer = input("what is the capital of lagos")
  if answer == "ikeja":
    print("correct")
  else:
    print("wrong")
elif user_choice == "no":
  print("no game played")
else:
  print("wrong input")