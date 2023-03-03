# cook your dish here
T = int(input())
for i in range(T):
    num = input()
    if((num == 'b') or (num == 'B') or (num == 'c') or (num == 'C') or (num == 'd') or (num == 'D') or (num == 'f') or (num == 'F')):
        if((num == 'b') or (num == 'B')):
            print("BattleShip")
        elif((num == 'c') or (num == 'C')):
            print("Cruiser")
        elif((num == 'd') or (num == 'D')):
            print("Destroyer")
        else:
            print("Frigate")
    else:
        print("Invalid Input")