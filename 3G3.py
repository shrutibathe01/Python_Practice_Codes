scores=[]
while True:
    choice=int(input("Do you want to enter player Score \n if Yes press 1 else press 0:"))
    if(choice==0):
        break
    else:    
        player=[]
        c=input("Enter the score: ")
        player=c.split(',')
        
        while len(player)>6:
            player.pop()
    scores.append(player)
print(scores)