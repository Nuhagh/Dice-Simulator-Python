import random


ledge="[-----------]"
dice=[ledge,"[]","[]","[]",ledge]
zero="[           ]"
one="[     0     ]"
two="[   0   0   ]"

repeat="y"
while (repeat == "y"):
    number=random.randint(1,6)
    if number == 1:
        dice[1]=zero
        dice[2]=one
        dice[3]=zero
    elif number ==2:
        dice[1]=zero
        dice[2]=two
        dice[3]=zero
    elif number==3:
        dice[1]=one
        dice[2]=one
        dice[3]=one
    elif number==4:
        dice[1]=two
        dice[2]=zero
        dice[3]=two
    elif number==5:
        dice[1]=two
        dice[2]=one
        dice[3]=two
    else:
        dice[1]=two
        dice[2]=two
        dice[3]=two
    for item in dice:
        print(item)
    repeat=input("Repeat Rolling? Press y")
