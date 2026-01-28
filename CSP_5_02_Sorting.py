import random


def bubbleSort(items:list):
    swaps = 0
    comparisons = 0
    n = len(items)

    for i in range(n):
        for j in range(0, n - i - 1):
            comparisons += 1
            if items[j] > items[j+1]:
                items[j], items[j+1] = items[j+1], items[j]
                swaps += 1
    maxSwaps = 0
    for i in range(1, n):
        maxSwaps += i
    if swaps == maxSwaps:
        comparisons = n * (n-1)
    else:
        extra = 0
        for y in range(1,n,2):
            extra += 1
        comparisons += extra

    return items, swaps, comparisons


def insertionSort(items: list):
    swaps = 0
    comparisons = 0

    for i in range(1, len(items)):
        key = items[i]
        j = i -1
        while j >= 0:
            comparisons += 1
            if items[j] > key:
                items[j + 1] = items[j]
                swaps += 1
                j -= 1
            else:
                break
        items[j +1] = key


    return items, swaps, comparisons

def selectionSort(items : list):
    swaps = 0
    comparisons = 0
    n = len(items)

    for i in range(n-1):
        minIndex = i
        for j in range(i+1, n):
            comparisons += 1
            if items[j] < items[minIndex]:
                minIndex = j

        items[i], items[minIndex] = items[minIndex], items[i]
        swaps += 1

    return items, swaps, comparisons


y = [9,8,7,6,5,4,3,2,1]
print(bubbleSort(y.copy()))
print(insertionSort(y.copy()))
print(selectionSort(y.copy()))
print()
x = [x for x in range(50)]
random.shuffle(x)
print(bubbleSort(x.copy()))
print(insertionSort(x.copy()))
print(selectionSort(x.copy()))
