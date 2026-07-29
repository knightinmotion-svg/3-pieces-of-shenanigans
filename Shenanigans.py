diameter = int(input("enter your ideal diameter"))
radius = diameter/2
circumference = 2*( 3.14159256* radius)
print("your circumference is", circumference)

correct = 1
guess = float(input("Guess the number I'm thinking of"))
while guess > 1 or guess < 1:
    print("NNNOPE, try again")
    guess = float(input("Go on,give it another shot"))
    
    if guess == 1:
        print("HOW DID YOU KNOWW")
        break
        
print("As you wander through the woods you come upon a cave, a loud voice eminates from the cavern")
Name=input("WHO GOES THERE")
Where_from = input("from which direction did you emerge: east or west")
WF = Where_from
if WF == "west":
    print("You should be glad I'm in a good mood today")
    print("Suddenly an ace of spades card emerges out of the cave with so much speed that there is no time for you to dodge neither is there anything above your neck after impact")
else:
    print("The Fuga Clan? Then you're not completely useless")
    CT = input("Well that depends on whether your technique is fire or water related: fire or water")
    if CT == "water":
        print("The birds will eat well today 'you see a silhoette appear in the cave, lifting its arm and then...nothing. The birds did eat well that day")
    else:
        CT = input("Good, GOOD and what IS your cursed technique: explosion or Fuga")
        if CT == "Fuga":
            print("Preparation is necessary, swirls appear on the ground before chains slither towards you, knot your ankles and drag you under")
        else: CT == "explosion"
     
