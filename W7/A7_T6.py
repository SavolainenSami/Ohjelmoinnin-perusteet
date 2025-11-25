import random

random.seed(1234)

rock_art = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper_art = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors_art = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

choices = {
    1: ("rock", rock_art),
    2: ("paper", paper_art),
    3: ("scissors", scissors_art),
}


def main():
    print("Program starting.")
    print("Welcome to the rock-paper-scissors game!")
    player_name = input("Insert player name: ")
    print(f"Welcome {player_name}!")
    print("Your opponent is RPS-3PO.")
    print("Game starts...\n")

    p_wins = 0
    p_losses = 0
    p_draws = 0

    print("Options:")
    print("1 - Rock")
    print("2 - Paper")
    print("3 - Scissors")
    print("0 - Quit game")

    while True:
        choice = input("Your choice: ")

        if not choice.isdigit():
            continue

        choice = int(choice)

        if choice == 0:
            print("\nResults:")
            print(
                f"{player_name} - wins ({p_wins}), losses ({p_losses}), draws ({p_draws})"
            )
            print(
                f"RPS-3PO - wins ({p_losses}), losses ({p_wins}), draws ({p_draws})\n"
            )
            print("Program ending.")
            break

        if choice not in [1, 2, 3]:
            continue

        bot_choice = random.randint(1, 3)

        print("Rock! Paper! Scissors! Shoot!\n")

        print("#########################")
        print(f"{player_name} chose {choices[choice][0]}.\n")
        print(choices[choice][1])
        print("#########################")
        print(f"RPS-3PO chose {choices[bot_choice][0]}.\n")
        print(choices[bot_choice][1])
        print("#########################\n")

        if choice == bot_choice:
            print(f"Draw! Both players chose {choices[choice][0]}.\n")
            p_draws += 1
        else:
            if (
                (choice == 1 and bot_choice == 3)
                or (choice == 2 and bot_choice == 1)
                or (choice == 3 and bot_choice == 2)
            ):
                print(
                    f"{player_name} {choices[choice][0]} beats RPS-3PO {choices[bot_choice][0]}.\n"
                )
                p_wins += 1
            else:
                print(
                    f"RPS-3PO {choices[bot_choice][0]} beats {player_name} {choices[choice][0]}.\n"
                )
                p_losses += 1

        print("Options:")
        print("1 - Rock")
        print("2 - Paper")
        print("3 - Scissors")
        print("0 - Quit game")


if __name__ == "__main__":
    main()
