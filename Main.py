import random

#user choice and menu
print("1: Rock\n2: Paper\n3: Scissors\n4: Exit")
player = int(input("Enter your choice or Exit: "))

while player != 4:

    if player == 1:
        player_option = "Rock"
    elif player == 2:
        player_option = "Paper"
    elif player == 3:
        player_option = "Scissors"

    # cpu choice
    li = [1,2,3]
    cpu = random.choice(li)

    if cpu == 1 :
        cpu_option = "Rock"
    elif cpu == 2 :
        cpu_option = "Paper"
    elif cpu == 3 :
        cpu_option = "Scissors"

    #compare
    print("Player choice", player_option,  "CPU choice", cpu_option)

    if player == 1 and cpu == 2 or player == 2 and cpu == 3 or player == 3 and cpu == 1:
        print("You Lose\n")
    elif player == 1 and cpu == 3 or player == 2 and cpu == 1 or player == 3 and cpu == 2:
        print("You win\n")
    else:
        print("Draw\n")
    
    print("1:Rock  2:Paper  3:Scissors  4:Exit")
    player = int(input("Enter your choice or Exit: "))
    
#exit
print("Exiting. . .")
quit()
