hp = 100
fire = False
causeofdeath = "test"

def start():
    print("\nYou have found yourself at the entrance to a cave. A blizzard rages outside, but the cave gives you some much needed shelter.")
    print (f"Health: {hp}")
    entrance_nofire()

def  entrance_nofire():
    entrance =  input("What do you do?: [1] Enter the cave, [2] Go out into the blizzard, [3] Start a fire, [4] Wait here a while. Choice:  ")
    global hp
    if entrance == "1":
        print("\nYou enter the cave. The sound of howling wind fades away as you head into the darkness. The light of the entrance fades too...if only you could bring some with you...")
        cave1()
    elif entrance == "2":
        blizzard()
    elif entrance == "3":
        global fire
        fire = True
        if hp < 100:
            print("\nYou decide to light a fire. The warmth fills your bones and you feel your strength returning.")
            hp += 10
            print(f"Health: {hp}")
        else:
            print("\nYou decide to light a fire. The warmth fills your bones.")
        entrance_fire()
    elif entrance == "4":
        print("\nYou hang out in the shelter of the cave entrance for a while.")
        entrance_nofire()
    else:
        invalid()
        entrance_nofire()

def entrance_fire():
    entrance =  input("What do you do?: [1] Enter the cave, [2] Go out into the blizzard, [3] Sit by the fire for a while. Choice:  ")
    global hp
    if entrance == "1":
        print("\nYou enter the cave. The sound of howling wind fades away.")
        cave1()
    elif entrance == "2":
        blizzard()
    elif entrance == "3":
        if hp < 100:
            hp += 10
            print("\nYou sit by the fire for a while. The warmth fills your bones and you feel your strength returning.")
            print(f"Health: {hp}")
        else:
            print("\nYou sit by the fire for a while, contemplating your next move.")
        entrance_nofire()
    else:
        invalid()
        entrance_fire()

def death():
    global causeofdeath
    print(f"\nYou died. Cause of death: {causeofdeath}")
    replay()

def replay():
    replay = input("\nPlay again? [1] Yes, [2] No")
    if replay == "1":
        start()
    elif replay == "2":
        print("Thanks for playing!")
    else:
        invalid()
        replay()

def blizzard():
    global hp
    global causeofdeath
    print("\nYou walk out into the blizzard, shielding your face from the stinging snow. You feel the cold seep into your bones. HP - 10. ")
    hp -= 10
    print(f"HP: {hp}")
    if hp == 0:
        causeofdeath = "Froze to death"
        death()
    else:
        blizzard_action()

def blizzard_action():
    blizzard = input("What do you do?: [1] Run back to the cave, [2] Walk further into the blizzard.")
    if blizzard == "1":
        print("\nYou run back to the cave as fast as you can - that was a horrible idea. You collapse on the floor of the cave, shivering.")
        if fire == True:
            entrance_fire()
        else:
            entrance_nofire()
    elif blizzard == "2":
        global causeofdeath
        causeofdeath = "Froze to death"
        death()
    else:
        invalid()
        blizzard()

def invalid():
    print("Not a valid input. Try again.")

def cave1():
    cave = input("What do you do?: [1] Go back and try to find a torch, [2] Continue into the cave")
    global fire
    if cave == "1" and fire == True
    

#starting point
start()
