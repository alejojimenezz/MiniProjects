import random
import time

# BUBBLE FUNCTION
def bubble(inputList):

    n = len(inputList)
    bubbledList = inputList.copy()
    bubbleCompCount = 0
    bubbleSwapCount = 0
    
    for i in range(n-1):
        swapped = False
        for j in range(n-i-1):
            bubbleCompCount += 1
            if bubbledList[j] > bubbledList[j+1]:
                bubbledList[j], bubbledList[j+1] = bubbledList[j+1], bubbledList[j]
                bubbleSwapCount += 1
                swapped = True
        if not swapped:
            break

    return bubbledList, bubbleCompCount, bubbleSwapCount

# MERGE FUNCTIONS (2)
def mergeSort(inputList):
    
    mergedList = inputList.copy()

    if len(mergedList) <= 1:
        return mergedList, 0, 0

    mid = len(mergedList) // 2
    leftHalf = mergedList[:mid]
    rightHalf = mergedList[mid:]

    sortedLeft, compsLeft, swapsLeft = mergeSort(leftHalf)
    sortedRight, compsRight, swapsRight = mergeSort(rightHalf)

    merged, compsMerge, swapsMerge = merge(sortedLeft, sortedRight)

    return merged, compsLeft+compsRight+compsMerge, swapsLeft+swapsRight+swapsMerge

def merge(left, right):

    result = []
    i = j = 0
    mergeCompCount = 0
    mergeSwapCount = 0

    while i < len(left) and j < len(right):
        mergeCompCount += 1
        if left[i] < right[j]:
            result.append(left[i])
            mergeSwapCount += 1
            i += 1
        else:
            result.append(right[j])
            mergeSwapCount += 1
            j += 1

    result.extend(left[i:])
    mergeSwapCount += len(left[i:])
    result.extend(right[j:])
    mergeSwapCount += len(right[i:])

    return result, mergeCompCount, mergeSwapCount

seedNum = int(input("Ingrese valor de la semilla para generar la lista: "))
listLength = int(input("Ingrese cuantos numeros desea en la lista generada: "))

random.seed(seedNum)

myList = [random.randint(1, 100) for i in range(listLength)]

startBubble = time.time()
bubbledList, bubbleCompCount, bubbleSwapCount = bubble(myList)
endBubble = time.time()

startMerge = time.time()
mergedList, mergeCompCount, mergeSwapCount = mergeSort(myList)
endMerge = time.time()

bubbleMs = (endBubble - startBubble) * 1000
mergeMs = (endMerge - startMerge) * 1000

print("Bubble (O(n^2)), comps = ", bubbleCompCount, ", swaps = ", bubbleSwapCount, ", ms = ", bubbleMs)
print("Merge (O(n*log n)), comps = ", mergeCompCount, ", swaps = ", mergeSwapCount, ", ms = ", mergeMs)

'''
Prueba 1:

    Entrada:
        Semilla: 13
        Elementos en lista: 10
    Salida:
        Bubble (O(n^2)), comps =  45 , swaps =  28 , ms =  0.0
        Merge (O(n*log n)), comps =  23 , swaps =  39 , ms =  0.0

Prueba 2:

    Entrada:
        Semilla: 22
        Elementos en lista: 27
    Salida:
        Bubble (O(n^2)), comps =  351 , swaps =  158 , ms =  0.0
        Merge (O(n*log n)), comps =  95 , swaps =  131 , ms =  0.0

Prueba 3:

    Entrada:
        Semilla: 80
        Elementos en lista: 99
    Salida:
        Bubble (O(n^2)), comps =  4815 , swaps =  2434 , ms =  0.0
        Merge (O(n*log n)), comps =  548 , swaps =  680 , ms =  0.0
'''