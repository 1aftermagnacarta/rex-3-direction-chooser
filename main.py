import random
import time

directions = ["Left","Right","Up","Down","Forward"]

while True: #infinitely loops through directions.
    ranTime = random.randint(30,60)
    ranDirection = random.choice(directions)
    print(ranDirection)
    time.sleep(ranTime)