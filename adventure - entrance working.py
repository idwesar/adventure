hp = 100
fire = False
causeofdeath = "test"
torch = False

def start():
    print("\nYou have found yourself at the entrance to a cave. A blizzard rages outside, but the cave gives you some much needed shelter.")
    print (f"Health: {hp}")
    entrance()

def  entrance():
    global fire
    global hp
    global causeofdeath
    if fire:
        entrance = input("What do you do?: [1] Enter the cave, [2] Go out into the blizzard, [3] Sit by the fire for a while.")
        if entrance == "1":
            print("\nYou enter the cave. The sound of howling wind fades away.")
            cave1()
        elif entrance == "2":
            print("\nYou walk out into the blizzard, shielding your face from the stinging snow. You feel the cold seep into your bones. HP - 10. ")
            hp -= 10
            print(f"HP: {hp}")
            if hp == 0:
                causeofdeath = "Froze to death"
                death()
            else:
                blizzard()
        elif entrance == "3":
            if hp < 100:
                hp += 10
                print("\nYou sit by the fire for a while. The warmth fills your bones and you feel your strength returning.")
                print(f"Health: {hp}")
            else:
                print("\nYou sit by the fire for a while, contemplating your next move.")
            entrance()
        else:
            invalid()
            entrance()
    else:
        entrance =  input("What do you do?: [1] Enter the cave, [2] Go out into the blizzard, [3] Start a fire, [4] Wait here a while.")
        if entrance == "1":
            print("\nYou enter the cave. The sound of howling wind fades away as you head into the darkness. The light of the entrance fades too...if only you could bring some with you...")
            cave1()
        elif entrance == "2":
            blizzard()
        elif entrance == "3":
            fire = True
            if hp < 100:
                print("\nYou decide to light a fire. The warmth fills your bones and you feel your strength returning.")
                hp += 10
                print(f"Health: {hp}")
            else:
                print("\nYou decide to light a fire. The warmth fills your bones.")
            entrance()
        elif entrance == "4":
            print("\nYou hang out in the shelter of the cave entrance for a while.")
            entrance()
        else:
            invalid()
            entrance()

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
    blizzard = input("What do you do?: [1] Run back to the cave, [2] Walk further into the blizzard.")
    if blizzard == "1":
        print("\nYou run back to the cave as fast as you can - that was a horrible idea. You collapse on the floor of the cave, shivering.")
        entrance()
    elif blizzard == "2":
        global causeofdeath
        causeofdeath = "Froze to death"
        death()
    else:
        invalid()
        blizzard()

def invalid():
    print("\nNot a valid input. Try again.")

def cave1():
    global torch
    if torch:
        print("YOURE IN CAVE 1 AND YOU HAVE A TORCH")
    else:
        cave = input("What do you do?: [1] Go back and try to make a torch, [2] Continue into the cave")
        global fire
        if cave == "1":
            print("You head back to the entrance of the cave.")
            if fire:
                light_torch()
            else:
                nofire()
        elif cave == "2":
            cave2_nt()
        else:
            invalid()
            cave1()
        
def light_torch():
    global torch
    print("\nYou pick up a burning branch from your fire. This will do nicely as a torch.")
    torch = True
    entrance()

def nofire():
    print("\nIf you had a fire, you could make yourself a torch...")
    nofire = input("What do you do?: [1] Light a fire, [2] Go into the cave anyway")
    if nofire == "1":
        global fire
        print("\nYou light a fire.")
        fire = True
        light_torch()
    elif nofire == "2":
        cave2_nt()
    else:
        invalid()
        nofire()

def cave2_nt():
    global fire
    print("\nYou decide to go into the cave anyway. You stumble through the darkness, trying to feel your way along the jagged cave walls and uneven floor.")
    cave2 = input("What do you do?: [1] Go back for a torch, [2] Keep going into the cave")
    if cave2 == "1":
        print("You head back to the entrance of the cave.")
        if fire == True:
            light_torch()
        else:
            nofire()
    elif cave2 == "2":
        print("\nYou head further into the cave, tripping over your own feet and the loose rocks which seem to litter the floor. You feel like you're starting to hear noises...but you aren't sure.")
        cave3_nt()
    else:
        invalid()
        cave2_nt()

def cave3_nt():
    cave3 = input("What do you do? [1] Go back and get a torch, [2] Carry on into the cave")
    global fire
    if cave3 == "1":
        print("\nYou decide to go back and get a torch.")
        if fire == True:
            torch_fire()
        else:
            print("\nYou return to the light at the entrance of the cave. If you had a fire, you could light a torch...")
            torch_nofire()
    elif cave3 == "2":
        global causeofdeath
        print("\nYou decide to keep going into the darkness, ignoring the noises you hear. They seem to be getting louder though, perhaps they weren't just in your head...You're beginning to think this wasn't the best idea. You hear something coming towards you. Suddenly, a huge paw  swipes at you, knocking you full force into the cave wall.")
        causeofdeath = "Attacked by a monster...probably should have brought a torch."
        death()


start()
