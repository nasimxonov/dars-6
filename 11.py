import random

choices = ["Rock", "Paper", "Scissors"]
rock = 0
paper = 0
scissors = 0

for _ in range(1000):

    choice = random.choice(choices)
    if choice == "Rock":

        rock += 1
    elif choice == "Paper":
        
        paper += 1
    else:
        scissors += 1

print(f"Rocklar soni: {rock}ta, Paperlar soni: {paper}ta, Scissorlar soni: {scissors}ta")
