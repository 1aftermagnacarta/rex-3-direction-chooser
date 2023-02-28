import random
import time
directions = ["Left","Right","Up","Down","Forward"]

while True:
    ranTime = random.randint(30,60)
    ranDirection = random.randint(0,len(directions)-1)
    time.sleep(ranTime)
    print(directions[ranDirection])