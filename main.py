def toBool(text):
    if text.lower() == "y":
        return True
    else:
        return False
        
import random
import time

directions = ["Left","Right","Up","Down","Forward"]

sameVal = toBool(input("Duplicate directions? Y/N \n"))

sleepLenMin = int(input("\nEnter the min sleep length: \n")) #I will add validation soon, for now make sure your input is above 0.

sleepLenMax = int(input("\nEnter the max sleep length: \n")) #I will add validation soon, for now make sure your input is above 0 and is above the sleepLenMin value.

prevDirection = ""
while True: #infinitely loops through directions.
    ranTime = random.randint(sleepLenMin,sleepLenMax)
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