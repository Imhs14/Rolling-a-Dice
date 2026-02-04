import random
while True:
    choice = input("Roll dice!(y/n)").lower() 
    if choice == 'y':
        die = int(input("Enter how many dices you want to Roll:"))
        i = 1
        while i <= die :
            die1 = random.randint(1,6)
            print(die1)
            i+=1
    elif choice == 'n':
        print("Thanks for playing")
        break
    else:
        print("invalid input")