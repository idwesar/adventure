import random

w = "What do you do?: "
fire = False
causeofdeath = "test"
torch = False
seencave = False
bearhp = 200
punchcounter = 0
hiding = 0

hp = 100

def start():
    print("\nYou have found yourself at the entrance to a cave. A blizzard rages outside, but the cave gives you some much needed shelter.")
    print (f"HP: {hp}")
    entrance()

def invalid():
    print("\nNot a valid input. Try again.")

def death():
    global causeofdeath
    print(f"\nYou died. Cause of death: {causeofdeath}")
    replay()

def replay():
    replay = input("\nPlay again? [1] Yes, [2] No")
    if replay == "1":
        start()
    elif replay == "2":
        print("\nThanks for playing!")
    else:
        invalid()
        replay()

def  entrance():
    global fire
    global torch
    global seencave
    if fire:
        entrance = input(f"{w}[1] Enter the cave, [2] Go out into the blizzard, [3] Sit by the fire for a while.")
    else:
        entrance =  input(f"{w}[1] Enter the cave, [2] Go out into the blizzard, [3] Start a fire, [4] Wait here a while.")
    if entrance == "1":
        if fire:
            if seencave:
                print("\nYou head back into the cave.")
            elif torch:
                print("\nYou enter the cave. The sound of howling wind fades away. The torch casts a flickering light across the cave - you see that it's much deeper than you thought. You see dark shapes near the back of the cave.")
        else:
            print("\nYou enter the cave. The sound of howling wind fades away as you head into the darkness. The light of the entrance fades too...if only you could bring some with you...")
        cave1()
    elif entrance == "2":
        print("\nYou walk into the blizzard, shielding your face from the stinging snow. You feel the cold seep into your bones.")
        blizzard()
    elif entrance == "3":
        if fire:
            print("\nYou decide to sit by the fire for a while.")
        else:
            fire = True
            print("\nYou decide to light a fire.")
        sitbyfire()
    elif entrance == "4":
        print("\nYou hang out in the shelter of the cave entrance for a while.")
        entrance()
    else:
        invalid()
        entrance()

def sitbyfire():
    global hp
    if hp < 100:
        hp = 100
        print("The warmth fills your bones and you feel your strength returning. \nHP returned to maximum.")
        print(f"HP: {hp}")
    else:
        print("\nThe warmth washes over you as you contemplate your next move.")
    entrance()
    
def blizzard():
    global hp
    hp -= 10
    print("HP -10")
    print(f"HP: {hp}")
    if hp <= 0:
        global causeofdeath
        causeofdeath = "Froze to death"
        death()
    else:
        blizzard_action()

def blizzard_action():
    action = input(f"{w}[1] Run back to the cave, [2] Walk further into the blizzard.")
    if action == "1":
        print("\nYou run back to the cave as fast as you can - that was a horrible idea. You collapse on the floor of the cave, shivering.")
        entrance()
    elif action == "2":
        blizzard()
    else:
        invalid()
        blizzard_action()

def cave1():
    global torch
    global seencave
    if torch:
        seencave = True
        action = input(f"{w}[1] Get closer to the shapes, [2] Go back")
        if action == "1":
            print("You approach the shapes as quietly as you can. As you get closer, you begin to see the small movements of their breathing, the texture of their fur - sleeping bears. From their sizes, it looks like a mother and three cubs. You'd better be careful.")
            cave2()
        elif action == "2":
            print("You decide to back away. You head back to the entrance of the cave and consider what to do next.")
            entrance()
    else:
        cave = input(f"{w}[1] Go back and try to make a torch, [2] Continue into the cave")
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
    nofire = input(f"{w}[1] Light a fire, [2] Go into the cave anyway")
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
    cave2 = input(f"{w}[1] Go back for a torch, [2] Keep going into the cave")
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
    cave3 = input(f"{w}[1] Go back and get a torch, [2] Carry on into the cave")
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
    else:
        invalid()
        cave3_nt()

def cave2():
    action = input(f"{w}[1] Back away, [2] Poke the bears")
    if action == "1":
        print("\nYou back away slightly, not wanting to wake the bears.")
        notice_opening()
    elif action == "2":
        print("\nYou get closer and poke the mother bear. She stirs, apparently not pleased about being woken up, or about someone being so close to her cubs.")
        print(f"Bear HP: {bearhp}")
        print(f"Your HP: {hp}")
        bearfight1()
    else:
        invalid()
        cave2()

def notice_opening():
    print("\nYou cast your eyes around the cave again and notice a small opening in the wall near the bears.")

def bearfight1():
    action = input(f"{w}[1] Run!, [2] Punch the bear")
    global punchcounter
    if action == "1":
        dilemma()
    elif action == "2":
        if punchcounter == 0:
            print("\nYou punch the bear as hard as you can. The mother bear does not look amused. She swipes a massive paw at you, catching your shoulder.")
        else:
            print("\nYou punch the bear again. She swipes at you again - I'm not sure what you were expecting.")
        bearpunch()
        punchcounter += 1
        bearfight1()
    else:
        invalid()
        bearfight1()

def bearpunch():
    global bearhp
    damage = random.randint(1, 5)
    bearhp -= damage
    print(f"\nYou do {damage} damage")
    print(f"Bear HP: {bearhp}")
    takedam_bear()

def takedam_bear():
    global hp
    damage = random.randint(60, 80)
    hp -= damage
    if hp <= 0:
            global causeofdeath
            causeofdeath = "Mauled by a bear"
            death()
    else:
        print(f"\nThe bear does {damage} damage")
        print(f"HP: {hp}")
            
def dilemma():
    global hp
    print("\nYou turn and run, hearing the angry mother bear close behind you. As you reach the mouth of the cave you hesitate. The blizzard is still raging outside.")
    action = input(f"{w}[1] Stay in the cave and face the bear, [2] Go into the blizzard")
    if action == "1":
        print("You stand your ground, unwilling to brave the raging blizzard outside. The mother bear approaches and swipes at you again.")
        takedam_bear()
    elif action == "2":
        print("You run into the blizzard and hide as best you can. The mother bear comes to the mouth of the cave, sniffs around suspiciously, then slowly turns around to return to her cubs.")
        blizzard()
        outside()

def outside():
    global hiding
    action = input(f"{w}[1] Wait for the mother bear to return to her cubs, [2] Go back into the cave")
    if action == "1":
        print("You decide to stay hidden for a bit longer, just in case the mother bear is still angry.")
        hiding += 1
        blizzard()
    
start()
