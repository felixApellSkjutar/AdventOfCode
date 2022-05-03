class Bag:
    def __init__(self, innerBags):
        self.innerBags = innerBags


bool = True
inArr = []
while bool:
    try:
        inArr.append(input())
    except:
        bool = False
print(inArr)