# Task 1: Code Correction

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross the river? ")
    if action == "climb a tree":
        print("You found a bird's nest!") 
    elif action == "cross the river": 
        print("You found a boat!")
    # Task 3: Using Pass
    else: action != "climb a tree" or "cross a river"
    pass
elif place == "cave":
    torch = input("Do you light a torch or proceed in the dark? (light a torch/proceed in the dark): ")
    if torch == "light a torch":    
        # Task 2: Setting the Scene
        print("You light a torch and see something ahead...") 
        print("You find a hidden treasure!")
             
    elif torch == "proceed in the dark":
        print("You stumble around in the dark until you loose your footing.")
        print("You fall into a stream that pulls you into the forest.") 
    else: torch != "light a torch" or "proceed in the dark" 
    pass
          
else:
    if place != "forest" or "cave":
        pass
