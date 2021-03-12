hp = 100
fire = False

def start():
    print("You have found yourself at the entrance to a cave. A blizzard rages outside, but the cave gives you some much needed shelter. What do you do?")
    print (f"Health: {hp}")
    entrance_nofire()
    

def  entrance_nofire():
    entrance1 =  input("[1] Enter the cave, [2] Go out into the blizzard, [3] Start a fire, [4] Wait here a while. Choice:  ")
    global hp
    if entrance1 == "1":
        print("You enter the cave. The sound of howling wind fades away.")
    elif entrance1 == "2":
        print("You walk out into the blizzard. Snow whips your face and you feel the cold seeping into your bones")
        hp -= 10
        print(f"Health: {hp}")
    elif entrance1 == "3":
        global fire
        fire = True
        if hp < 100:
            print("You decide to light a fire. The warmth fills your bones and you feel your strength returning.")
            hp += 10
            print(hp)
        else:
            print("You decide to light a fire. The warmth fills your bones.")
    elif entrance1 == "4":
        print("You hang out in the shelter of the cave entrance for a while.")
        entrance_nofire()
    else:
        print("Not a valid input. Try again.")
        entrance_nofire()


#starting point
start()

                
            

