import random
import time

directions = ["Left","Right","Up","Down","Forward"]

sameVal = input("Duplicate directions? Y/N \n")
if sameVal.lower() == "n":
    sameVal = False
else:
    sameVal = True

count = 0
prevDirection = ""
while True: #infinitely loops through directions.
    ranTime = random.randint(3,6)
    ranDirection = random.randint(0,len(directions)-1)
    if count > 0:
        if sameVal == False:
            if prevDirection == ranDirection:
                if prevDirection < len(directions)-1:
                    ranDirection = random.randint(prevDirection+1,len(directions)-1)
                else:
                    ranDirection = random.randint(0,prevDirection-1)
    prevDirection = ranDirection
    print("\n",directions[ranDirection])
    time.sleep(ranTime)
    count += 1