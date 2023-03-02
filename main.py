import random
import time

def toBool(text):
    if text.lower() == "y":
        return True
    else:
        return False

directions = ["Left","Right","Up","Down","Forward"]

sameVal = toBool(input("Duplicate directions? Y/N \n"))

prevDirection = ""
while True: #infinitely loops through directions.
    ranTime = random.randint(30,60)
    ranDirection = random.randint(0,len(directions)-1)
    if sameVal == False:
        if prevDirection == ranDirection:
            if prevDirection < len(directions)-1:
                ranDirection = random.randint(prevDirection+1,len(directions)-1)
            else:
                ranDirection = random.randint(0,prevDirection-1)
    prevDirection = ranDirection
    print("\n",directions[ranDirection])
    time.sleep(ranTime)