import random

class State:
    def __init__(self):
        self.w = "What do you do?: "
        self.causeofdeath = "test"
        self.fire = False
        self.torch = False
        self.seencave = False
        self.bearhp = 200
        self.punchcounter = 0
        self.hiding = "base"
        self.hp = 100

    def reset(self):
        self.w = "What do you do?: "
        self.causeofdeath = "test"
        self.fire = False
        self.torch = False
        self.seencave = False
        self.bearhp = 200
        self.punchcounter = 0
        self.hiding = "base"
        self.hp = 100

# Dialogue, inputs

class FrameOpts:
    def __init__(self, dialogue, choices, actOnState = None, modifyState = None):
        self.dialogue = dialogue
        self.choices = choices
        self.actOnState = actOnState
        self.modifyState = modifyState
    
    def getDialogue(self):
        return self.dialogue

    def getChoices(self):
        return self.choices

    def getActOnState(self):
        return self.actOnState

    def getModifyState(self):
        return self.modifyState


def frame(frameOpts, state):
    if frameOpts.modifyState != None:
        assert(state != None)
        frameOpts.modifyState(state)

    print('\n' + frameOpts.getDialogue())

    if frameOpts.actOnState != None:
        assert(state != None)
        frameOpts.actOnState(state)

    return handleOptions(frameOpts.getChoices())


def handleOptions(choices):
    keys = [key for key in choices.keys()]
    for i, c in enumerate(keys):
        print(f"[{i+1}] {c}")

    while(True):
        selection = int(input("What do you do?:"))
        if selection <= 0 or selection > len(keys):
            print("Invalid choice. Please choose again!")
        else:
            key = keys[selection-1]
            return choices[key]


def looseHealth(state):
    """ Subtract from player health """
    state.hp = state.hp - 10


def lostHealth(state):
    print(f"You done fucked up! {state.hp}")


def main():
    state = State()

    frameMap = {
        "entrance": FrameOpts(
                "You have found yourself at the entrance to a cave. A blizzard rages outside, but the cave gives you some much needed shelter.",
                {"Enter the cave": "cave", "Go out into the blizzard": "blizzard", "Sit by the fire for a while (heal)": "fire"}
        ),

        "cave": FrameOpts(
            "You head back into the cave.",
            {"Remain hidden outside": None, "Go back into the cave": None},
        ),

        "blizzard": FrameOpts(
            "You walk into the blizzard, shielding your face from the stinging snow. You feel the cold seep into your bones.",
            {"Remain hidden outside": "blizzard", "Go back into the cave": "cave", "Head further into the blizzard": "blizzard"},
            actOnState=lostHealth,
            modifyState=looseHealth
        ),

        "fire": FrameOpts(
            "The warmth fills your bones and you feel your strength returning (HP returned to maximum).",
            {"Choice 1": None, "Choice 2": None}
        ),
    }

    currFrame = "entrance"
    while(True):
        print("currFrame: ", currFrame)
        if currFrame == None:
            break
        frameOpts = frameMap[currFrame]
        currFrame = frame(frameOpts, state)


    # def start(state):
    #     print("\nYou have found yourself at the entrance to a cave. A blizzard rages outside, but the cave gives you some much needed shelter.")
    #     print (f"HP: {state.hp}")
    #     entrance(state)

    # def invalid():
    #     print("\nNot a valid input. Try again.")

    # def death(state):
    #     print(f"\nYou died. Cause of death: {state.causeofdeath}")
    #     replay()

    # def replay(state):
    #     fallthrough = True
    #     while(fallthrough):
    #         replay = input("\nPlay again? [1] Yes, [2] No")
    #         if replay == "1":
    #             fallthrough = False
    #             state.reset()
    #             start(state)
    #         elif replay == "2":
    #             fallthrough = False
    #             print("\nThanks for playing!")
    #         else:
    #             invalid()

    # def entrance(state):
    #     if state.fire:
    #         action = input(f"{state.w}[1] Enter the cave, [2] Go out into the blizzard, [3] Sit by the fire for a while (heal).")
    #     else:
    #         action =  input(f"{state.w}[1] Enter the cave, [2] Go out into the blizzard, [3] Start a fire, [4] Wait here a while.")
    #     if action == "1":
    #         if state.fire:
    #             if state.seencave:
    #                 print("\nYou head back into the cave.")
    #             elif state.torch:
    #                 print("\nYou enter the cave. The sound of howling wind fades away. The torch casts a flickering light across the cave - you see that it's much deeper than you thought. You see dark shapes near the back of the cave.")
    #         else:
    #             print("\nYou enter the cave. The sound of howling wind fades away as you head into the darkness. The light of the entrance fades too...if only you could bring some with you...")
    #         cave1(state)
    #     elif action == "2":
    #         print("\nYou walk into the blizzard, shielding your face from the stinging snow. You feel the cold seep into your bones.")
    #         blizzard(state)
    #     elif action == "3":
    #         if state.fire:
    #             print("\nYou decide to sit by the fire for a while.")
    #         else:
    #             state.fire = True
    #             print("\nYou decide to light a fire.")
    #         sitbyfire(state)
    #     elif action == "4":
    #         print("\nYou hang out in the shelter of the cave entrance for a while.")
    #         entrance(state)
    #     else:
    #         invalid()
    #         entrance(state)

    # def sitbyfire(state):
    #     if state.hp < 100:
    #         state.hp = 100
    #         print("\nThe warmth fills your bones and you feel your strength returning. \nHP returned to maximum.")
    #         print(f"HP: {state.hp}")
    #     else:
    #         print("\nThe warmth washes over you as you contemplate your next move.")
    #     entrance(state)
        
    # def blizzard(state):
    #     state.hp -= 10
    #     print("HP -10")
    #     print(f"HP: {state.hp}")
    #     if hp <= 0:
    #         state.causeofdeath = "Froze to death"
    #         death(state)
    #     else:
    #         if state.hiding == "current":
    #             outside(state)
    #         else:
    #             blizzard_action(state)

    # def blizzard_action(state):
    #     action = input(f"{w}[1] Run back to the cave, [2] Walk further into the blizzard.")
    #     if action == "1":
    #         print("\nYou run back to the cave as fast as you can - that was a horrible idea. You collapse on the floor of the cave, shivering.")
    #         entrance()
    #     elif action == "2":
    #         print("\nYou head further into the blizzard.")
    #         blizzard()
    #     else:
    #         invalid()
    #         blizzard_action()

    # def cave1(state):
    #     if state.hiding == "past":
    #         print("\nYou cast your eyes around the cave again and notice a small opening in the wall near the bears.")
    #         notice_opening(state)
    #     if state.torch:
    #         state.seencave = True
    #         action = input(f"{w}[1] Get closer to the shapes, [2] Go back")
    #         if action == "1":
    #             print("\nYou approach the shapes as quietly as you can. As you get closer, you begin to see the small movements of their breathing, the texture of their fur - sleeping bears. From their sizes, it looks like a mother and three cubs. You'd better be careful.")
    #             cave2(state)
    #         elif action == "2":
    #             print("\nYou decide to back away. You head back to the entrance of the cave and consider what to do next.")
    #             entrance(state)
    #     else:
    #         action = input(f"{state.w}[1] Go back and try to make a torch, [2] Continue into the cave")
    #         if action == "1":
    #             print("\nYou head back to the entrance of the cave.")
    #             if fire:
    #                 light_torch(state)
    #             else:
    #                 nofire(state)
    #         elif action == "2":
    #             cave2_nt(state)
    #         else:
    #             invalid()
    #             cave1(state)
            
    # def light_torch(state):
    #     print("\nYou pick up a burning branch from your fire. This will do nicely as a torch.")
    #     state.torch = True
    #     entrance(state)

    # def nofire(state):
    #     print("\nIf you had a fire, you could make yourself a torch...")
    #     action = input(f"{w}[1] Light a fire, [2] Go into the cave anyway")
    #     if action == "1":
    #         print("\nYou light a fire.")
    #         state.fire = True
    #         light_torch(state)
    #     elif action == "2":
    #         state.cave2_nt()
    #     else:
    #         invalid()
    #         nofire(state)

    # def cave2_nt(state):
    #     print("\nYou decide to go into the cave anyway. You stumble through the darkness, trying to feel your way along the jagged cave walls and uneven floor.")
    #     action = input(f"{state.w}[1] Go back for a torch, [2] Keep going into the cave")
    #     if action == "1":
    #         print("You head back to the entrance of the cave.")
    #         if state.fire == True:
    #             light_torch(state)
    #         else:
    #             nofire(state)
    #     elif action == "2":
    #         print("\nYou head further into the cave, tripping over your own feet and the loose rocks which seem to litter the floor. You feel like you're starting to hear noises...but you aren't sure.")
    #         cave3_nt(state)
    #     else:
    #         invalid()
    #         cave2_nt(state)

    # def cave3_nt(state):
    #     action = input(f"{state.w}[1] Go back and get a torch, [2] Carry on into the cave")
    #     if action == "1":
    #         print("\nYou decide to go back and get a torch.")
    #         if fire == True:
    #             torch_fire(state)
    #         else:
    #             print("\nYou return to the light at the entrance of the cave. If you had a fire, you could light a torch...")
    #             torch_nofire(state)
    #     elif action == "2":
    #         print("\nYou decide to keep going into the darkness, ignoring the noises you hear. They seem to be getting louder though, perhaps they weren't just in your head...You're beginning to think this wasn't the best idea. You hear something coming towards you. Suddenly, a huge paw  swipes at you, knocking you full force into the cave wall.")
    #         causeofdeath = "Attacked by a monster...probably should have brought a torch."
    #         death()
    #     else:
    #         invalid()
    #         cave3_nt(state)

    # def cave2(state):
    #     action = input(f"{state.w}[1] Back away, [2] Poke the bears")
    #     if action == "1":
    #         print("\nYou back away slightly, not wanting to wake the bears. You cast your eyes around the cave again and notice a small opening in the wall near the bears.")
    #         notice_opening()
    #     elif action == "2":
    #         print("\nYou get closer and poke the mother bear. She stirs, apparently not pleased about being woken up, or about someone being so close to her cubs.")
    #         bearfight(state)
    #     else:
    #         invalid()
    #         cave2(state)

    # def bearfight(state):
    #     action = input(f"{state.w}[1] Run!, [2] Punch the bear")
    #     print(f"\nBear HP: {state.bearhp}")
    #     print(f"Your HP: {state.hp}")
    #     if action == "1":
    #         dilemma(state)
    #     elif action == "2":
    #         if punchcounter == 0:
    #             print("\nYou punch the bear as hard as you can. The mother bear does not look amused. She swipes a massive paw at you, catching your shoulder.")
    #         else:
    #             print("\nYou punch the bear again. She swipes at you again - I'm not sure what you were expecting.")
    #         bearpunch(state)
    #         punchcounter += 1
    #         bearfight(state)
    #     else:
    #         invalid()
    #         bearfight(state)

    # def bearpunch(state):
    #     damage = random.randint(1, 5)
    #     state.bearhp -= damage
    #     print(f"\nYou do {damage} damage")
    #     print(f"Bear HP: {state.bearhp}")
    #     takedam_bear(state)

    # def takedam_bear(state):
    #     damage = random.randint(50, 70)
    #     state.hp -= damage
    #     if hp <= 0:
    #             causeofdeath = "Mauled by a bear"
    #             death(state)
    #     else:
    #         print(f"\nThe bear does {state.damage} damage")
    #         print(f"HP: {state.hp}")
                
    # def dilemma(state):
    #     print("\nYou turn and run, hearing the angry mother bear close behind you. As you reach the mouth of the cave you hesitate. The blizzard is still raging outside.")
    #     action = input(f"{state.w}[1] Stay in the cave and face the bear, [2] Go into the blizzard")
    #     if action == "1":
    #         print("\nYou stand your ground, unwilling to brave the raging blizzard outside. The mother bear approaches and swipes at you again.")
    #         takedam_bear(state)
    #     elif action == "2":
    #         print("\nYou run into the blizzard and hide as best you can. The mother bear comes to the mouth of the cave, sniffs around suspiciously, then slowly turns around to return to her cubs.")
    #         state.hiding = "current"
    #         blizzard(state)
    #         outside(state)

    # def outside(state):
    #     action = input(f"{w}[1] Remain hidden outside, [2] Go back into the cave, [3] Head further into the blizzard")
    #     if action == "1":
    #         print("\nYou decide to stay hidden for a bit longer, just in case the mother bear is still angry.")
    #         state.hiding = "current"
    #         blizzard(state)
    #     elif action == "2":
    #         if hiding:
    #             print("\nYou head back into the cave. The bears seem to be asleep again. Phew. You pick up your torch from where you dropped it and relight it from the fire.")
    #             hiding = "past"
    #             entrance(state)
    #         else:
    #             print("\nYou head back into the cave, but the mother bear is not back to her cubs yet. She hears you and attacks once more.")
    #             takedam_bear
    #             if state.hp >= 0:
    #                 state.hiding = "past"
    #                 outside(state)
    #     elif action == "3":
    #         print("\nYou head further into the blizzard.")
    #         blizzard(state)
    #     else:
    #         invalid()
    #         outside(state)

    # def notice_opening(state):
    #     action = input(f"{state.w}[1] Go over to look closer at the opening, [2] Poke the bears, [3] Go back")
    #     if action == "1":
    #         print("\nYou approach the opening in the cave wall and peer inside. It looks like there's a second cave behind the wall. The hole looks like it might be big enough for you to squeeze through...")
    #         climb(state)
    #     elif action == "2":
    #         print("\nYou get closer and poke the mother bear. She stirs, apparently not pleased about being woken up, or about someone being so close to her cubs.")
    #         bearfight(state)
    #     elif action == "3":
    #         print("You decide to head back to the entrance.")
    #         entrance(state)
    #     else:
    #         invalid()
    #         notice_opening(state)
            
    # def climb(state):
    #     action = input(f"{state.w}[1] Climb through the hole, [2] Go back")
    #     if action == "1":
    #         print("\nYou clamber through the hole, dislodging a few rocks as you go. You pause on the other side and listen intently...doesn't look like you woke the bears. This cave is much bigger than the one you came from, and seems to have several tunnels leading from it.")
    #         print("\nThe end...for now")
    #         replay(state)
    #     elif action == "2":
    #         print("You move back a little.")
    #         notice_opening(state)


if __name__ == "__main__":
    main()
