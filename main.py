import random
from time import perf_counter
from matplotlib import pyplot as plt
from math import ceil as ceil

def setDistinctList(distinctElementList, n):

    if n < 3:
        return

    sizeOfList = random.randint(3, 100000)
    lowerbound = -sizeOfList

    while len(distinctElementList) !=n :
        randomNewInt = random.randint(lowerbound, sizeOfList)
        if randomNewInt not in distinctElementList:
            distinctElementList.append(randomNewInt)
        else:
            continue

def distinctLst(n):
    lst = []
    i=0
    while i<n:
        #print(i)
        e = random.randint(1,1000000)
        if e in lst:
            continue
        else:
            lst.append(e)
        i=i+1
    return lst

def incrementalAlg(lst):
    if len(lst)==3:
        if lst[1]<lst[0]:
            lst[1], lst[0] = lst[0], lst[1]
        if lst[2]<lst[1]:
            lst[2], lst[1] = lst[1], lst[2]
            if lst[1]<lst[0]:
                lst[1], lst[0] = lst[0], lst[1]
        return (lst[0],lst[1],lst[2])

    tup = list(incrementalAlg(lst[:-1]))
    tmp = lst[-1]

    i = 2
    while i>=0:
        if tup[i]<tmp:
            break
        else:
            if i==2:
                tup[i]=tmp
            else:
                tup[i+1]=tup[i]
                tup[i]=tmp
        i=i-1
    return (tup[0],tup[1],tup[2])


def divideAndConquerAlg(lst):
    if len(lst)==3:
        if lst[1]<lst[0]:
            lst[1], lst[0] = lst[0], lst[1]
        if lst[2]<lst[1]:
            lst[2], lst[1] = lst[1], lst[2]
            if lst[1]<lst[0]:
                lst[1], lst[0] = lst[0], lst[1]
        return tuple(lst)

    #Devide/Conqure
    tup1 = divideAndConquerAlg(lst[len(lst)//2:])
    tup2 = divideAndConquerAlg(lst[:len(lst)//2])
    newtup = []

    i=0 #index tup1
    j=0 #index tup2

    #Combine
    while i+j<3:
        if tup1[i]<tup2[j]:
            newtup.append(tup1[i])
            i=i+1
        else:
            newtup.append(tup2[j])
            j=j+1


    return tuple(newtup)

def max_subarray(lst):
    return max_subarray_rec(lst)[0]

def max_subarray_rec(lst):
    if len(lst)==1:
        #print(lst, (lst[0],lst[0],lst[0],lst[0]))
        return (lst[0],lst[0],lst[0],lst[0])

    left_tup = max_subarray_rec(lst[:len(lst)//2])
    right_tup = max_subarray_rec(lst[len(lst)//2:])

    left_max = max(left_tup[2],left_tup[1]+right_tup[2])
    right_max = max(right_tup[3],right_tup[1]+left_tup[3])
    tot_sum = left_tup[1]+right_tup[1]
    max_sum = max(left_tup[0],right_tup[0],left_tup[3]+right_tup[2])

    #print(lst, (max_sum, tot_sum, left_max, right_max))
    return (max_sum, tot_sum, left_max, right_max)

def verifyDistinctList(lst):
    for i in range(0,len(lst)):
        restOfList = lst[i+1:]
        if lst[i] in restOfList:
            return False
    return True

def graph(function,max):
    i=3
    times = []
    index = []
    while i<max:
        print(i)
        lst = CreateArrayA(i)
        index.append(i)
        start = perf_counter()
        function(lst)
        stop = perf_counter()
        times.append(stop-start)
        i=ceil(i*1.2)
    plt.plot(index, times)
    plt.ylabel('Runtime')
    plt.xlabel('Input size')
    plt.show()

def CreateArrayA(length):
    lst=[]
    while len(lst)< length:
        randomInt = random.randint(-10000,10000)
        if randomInt != 0:
            lst.append(randomInt)
    return lst


def main(alg: int):

    # List size
    #n = 50000
    lst = [1,2,-6,7,9,3,-5,-1]
    print(max_subarray(lst))

    # List for holding the distinct elements #argument - 'n' must be >=3
    distinctElementList = distinctLst(4)


    #print("list done")
    #print(verifyDistinctList(distinctElementList))

    if alg == 1:
        print(distinctElementList)
        print(incrementalAlg(distinctElementList))
    elif alg == 2:
        print(distinctElementList)
        print(divideAndConquerAlg(distinctElementList))
    elif alg == 3:
        print("TEst")
        graph(max_subarray,100000)
    elif alg == 4:
        #arrayA = createArrayA(1000)
        pass


if __name__ == '__main__':
    algorithm = 2

    main(algorithm)
