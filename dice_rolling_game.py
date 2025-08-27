import random

history = []
# Loop
while True:
    # Ask: roll the dice?
    choice = input("Roll the dice? (y/n): ").lower()
    # If users enters y 
    if choice == "y":
        # ask user how many times they want to roll
        try:
            rolls = int(input("How many times do you want to roll the dice? "))
        except ValueError:
            print("Please enter a valid number!")
            continue
        for i in range (rolls):
    # Generate two random numbers
            die1 = random.randint(1, 6)
            die2 = random.randint(1, 6)
            result = (die1, die2)
            history.append(result)
            print(f"Roll {i+1}:{result}")
    # If user enters n
    elif choice == "n":
        # Print thank you message
        print("Thanks for playing!")
        if history:
            print("Here's your dice roll history:")
            for i, roll in enumerate(history, start=1):
                print(f"Roll {i}: {roll}")
        else:
            print("No rolls recorded.")
         # Terminate
        break
    else:
        print("Invalid choice!")
