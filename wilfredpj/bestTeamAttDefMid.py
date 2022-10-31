file = open("./Data/NationalTeamRating.txt", 'r')
f = file.readlines()
file.close()

bestAttackName = ""
attackRating  = 0
bestMidName = ""
midRating = 0
bestDefName = ""
defRating = 0

nationalTeamsStats = {}
for line in f:
    line = line.strip()
    parsedInfo = line.split(" ")
    if int(parsedInfo[1]) > attackRating:
        bestAttackName = parsedInfo[0]
        attackRating = int(parsedInfo[1])
    if int(parsedInfo[2])> midRating:
        bestMidName = parsedInfo[0]  
        midRating = int(parsedInfo[2]) 
    if int(parsedInfo[3]) > defRating:
        bestDefName = parsedInfo[0]
        defRating = int(parsedInfo[3])     

    
   # nationalTeamsStats.update({parsedInfo[0]: parsedInfo[1]})
   # print(parsedInfo)

print("The best attacking team rating is ", bestAttackName, "with ", attackRating )

print("The best middfields team rating is ", bestMidName, "with ", midRating )

print("The best defence team rating is ", bestDefName, "with ", defRating )