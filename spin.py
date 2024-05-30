import random
import time


def spin():
    prob = {'apple': 5, 'banana': 2, 'chikku': 4,
            'mango': 3, 'grapes': 2, 'orange': 6}

    chlst1 = []
    for key in prob:
        for i in range(prob[key]):
            chlst1.append(key)
    box1 = chlst1.copy()
    box2 = chlst1.copy()
    box3 = chlst1.copy()
    slot1 = []
    slot2 = []
    slot3 = []

    for i in range(5):
        ch1 = random.choice(box1)
        slot1.append(ch1)
        box1.remove(ch1)

        ch2 = random.choice(box2)
        slot2.append(ch2)
        box2.remove(ch2)

        ch3 = random.choice(box3)
        slot3.append(ch3)
        box3.remove(ch3)

    return(slot1, slot2, slot3)


def check(s1, s2, s3, bet, bal):
    points = {'apple': 2, 'banana': 10, 'chikku': 2,
              'mango': 4, 'grapes': 7, 'orange': 5}
    bal -= bet
    if s1[2] == s2[2] and s1[2] == s3[2]:
        p = points[s1[2]]*bet
        return(p, p+bal)
    else:
        return(0, bal)


def display(s1, s2, s3, points, bal):

    print("Results")
    time.sleep(1)
    print(s1)
    time.sleep(1)
    print(s2)
    time.sleep(1)
    print(s3)
    print(f"your points are: {points}")
    print(f"available balance: {bal}")

# check(['gotiya','pammi','rash','gotiya','chintu'],['gotiya','pammi','rash','gotiya','chintu'],['gotiya','pammi','rash','gotiya','chintu'])
