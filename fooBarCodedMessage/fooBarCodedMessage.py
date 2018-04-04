def answer(l, t):

    broadcastList = l
    key = t
    messageLocation = []
    tempSum = 0

    for i in range(len(broadcastList)):
        tempSum = 0
        for j in range(i, len(broadcastList)):
            tempSum += broadcastList[j]
            if(tempSum > key):
                break
            
            if(tempSum == key):
              messageLocation = [i,j]
              return messageLocation
    messageLocation = [-1,-1]
    return messageLocation

l = [1, 2, 3, 4]
t = 15
print (answer(l, t))
# answer(l,t) = [-1, -1]

l = [4, 3, 10, 2, 8]
t = 12
print (answer(l, t))
# answer(l,t) = [2, 3]

l = [4, 3, 5, 7, 8]
t = 12
print (answer(l, t))
# answer(l,t) = [-1, -1]
