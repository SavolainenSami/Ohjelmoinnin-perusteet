# print("Welcome to the temp app!")
# 
#temp = int(input("What is the temperature of CPU? "))

# if temp > 80:
#     print("Warning! CPU temperature is too high!")
# else:
#     print("All good, keep on going!")



# num = int(input("Enter a number: "))
# if num % 2 == 0:
#     print(f"{num} is an even number")
# else:
#     print(f"{num} is an odd number")


# if(temp > 80):
#     if(temp > 90):
#         print("You are toast!")
#     else:
#         print("Warning!")
# else:
#     print("You are ok")

# if(temp > 90):
#     print("You are toast!")
# elif(temp > 80):
#     print("Warning!")
# else:
#     print("You are ok")

# tee ohjelma joka kysyy kahta nimeä, testaa nimistä on pidempi vai onko se saman mittainen
# name1 = input("Enter first name: ")
# name2 = input("Enter second name: ")
# if(len(name1) > len(name2)):
#     print(f"{name1} is longer than {name2}")
# elif(len(name1) < len(name2)):
#     print(f"{name2} is longer than {name1}")

# Town = "Lahti"
# Street = "Mukkulankatu"
# Building = 19

# if(Town == "Lahti" and Street == "Mukkulankatu" and Building == 19):
#     print(" You are at LAB")
# elif(Town == "Lahti" and (Street != "Mukkulankatu" or Building != 19)):
#     print("You are in correct town, but check steet adress again")
# elif not(Town == "Lahti" and Street == "Mukkulankatu" and Building == 19):
#     print("You are lost...")


# import random

# # print(random.random())
# print(random.randint(1, 6))

# # tee yksinkertainen kivi, paperi, sakset peli
# user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
# computer_choice = random.choice(["rock", "paper", "scissors"])
# print(f"Computer chose: {computer_choice}")
# if user_choice == computer_choice:
#     print("It's a tie!")
# elif (user_choice == "rock" and computer_choice == "scissors") or \
#      (user_choice == "paper" and computer_choice == "rock") or \
#      (user_choice == "scissors" and computer_choice == "paper"):
#     print("You win!")
# else:
#     print("Computer wins!")