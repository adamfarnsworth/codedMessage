def answer(l, t):

    broadcastList = l
    key = t
    messageLocation = []
    tempSum = 0
    endPosition = 0

    for i in range(len(broadcastList)):     # itterate through whole list
        if(i > 0):                          # removes checked start from the count
            tempSum -= broadcastList[i-1]
        for j in range(endPosition, len(broadcastList)):
            tempSum += broadcastList[j]
            if(tempSum > key):              # check next number is sum is to large
                tempSum -= broadcastList[j]
                endPosition = j
                break
            
            if(tempSum == key):             # return answer when found
              messageLocation = [i,j]
              return messageLocation

            if(j == len(broadcastList) -1): # no message is in this sequence
                messageLocation = [-1,-1]
                return messageLocation
            endPosition = j
    messageLocation = [-1,-1]               # no message is in this sequence
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
# answer(l,t) = [0, 2]
