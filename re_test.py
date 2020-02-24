class Man:
    height = 0
    name = ''

def manKey(man):
    return (-man.height, man.name)

n = int(input())
peopleList = []
for i in range(n):
    tempManData = input().split()
    man = Man()
    man.height = int(tempManData[0])
    man.name = tempManData[1]
    peopleList.append(man)
peopleList.sort(key=manKey)
for man in peopleList:
    print(man.height, man.name)
