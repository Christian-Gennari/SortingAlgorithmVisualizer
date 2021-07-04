import time

# BUBBLE SORT ALGORITHM
def bubble_sort(data, drawData, timeTick):
    for each in range(len(data)-1):
        for j in range(len(data)-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data [j]
                drawData(data, ["lightgreen" if x == j or x == j+1 else "lightblue" for x in range(len(data))])
                time.sleep(timeTick)
    drawData(data, ["lightgreen" for x in range(len(data))])


# QUICK SORT ALGORITHM
def quick_sort_partition(data, head, tail, drawData, timeTick):
    border = head
    pivot = data[tail]

    drawData(data, getColorArray(len(data), head, tail, border, border))
    time.sleep(timeTick)

    for j in range(head, tail):
        if data [j] < pivot:
            drawData(data, getColorArray(len(data), head, tail, border, j, True))
            time.sleep(timeTick)

            data[border], data [j] = data[j], data[border]
            border += 1

            drawData(data, getColorArray(len(data), head, tail, border, j))
            time.sleep(timeTick)
        
    # Swap pivot with border value
    drawData(data, getColorArray(len(data), head, tail, border, tail, True))
    time.sleep(timeTick)
    data[border], data[tail] = data[tail], data[border]

    return border
def quick_sort(data, head, tail, drawData, timeTick):
    if head < tail:
        # Getting split index
        partitionIndex = quick_sort_partition(data, head, tail, drawData, timeTick)
        
        # Left partition
        quick_sort(data, head, partitionIndex-1, drawData, timeTick)

        # Right partition
        quick_sort(data, partitionIndex+1, tail, drawData, timeTick)
def getColorArray(dataLen, head, tail, border, currentIndex, isSwapping = False):
    colorArray = []
    for i in range(dataLen):
        # Base coloring
        if i > head and i < tail:
            colorArray.append("lightblue")
        else:
            colorArray.append("lightblue")
        if i == tail:
            colorArray[i] = "blue"
        elif i == border:
            colorArray[i] = "red"
        elif i == currentIndex:
            colorArray[i] = "yellow"

        if isSwapping:
            if i == border or i == currentIndex:
                colorArray[i] = "lightgreen"
    return colorArray

# MERGE SORT ALGORITHM
def merge_sort(data, drawData, timeTick):
    merge_sort_Algorithm(data, 0, len(data)-1, drawData, timeTick)

def merge_sort_Algorithm(data, left, right, drawData, timeTick):
    if left < right:
        # Getting the middle value
        middle = (left + right) // 2
        # Dividing further
        merge_sort_Algorithm(data, left, middle, drawData, timeTick)
        merge_sort_Algorithm(data, middle+1, right, drawData, timeTick)

        merge(data, left, middle, right, drawData, timeTick)

def merge(data, left, middle, right, drawData, timeTick):
    drawData(data, getColorArrayMergeSort(len(data), left, middle, right))
    time.sleep(timeTick)

    leftPart = data[left:middle+1]
    rightPart = data[middle+1: right+1]

    leftIndex = rightIndex = 0

    for dataIndex in range(left, right+1):
        if leftIndex < len(leftPart) and rightIndex < len(rightPart):
            if leftPart[leftIndex] <= rightPart[rightIndex]:
                data[dataIndex] = leftPart[leftIndex]
                leftIndex += 1
            else:
                data[dataIndex] = rightPart[rightIndex]
                rightIndex += 1

        elif leftIndex < len(leftPart):
            data[dataIndex] = leftPart[leftIndex]
            leftIndex += 1
        else:
            data[dataIndex] = rightPart[rightIndex]
            rightIndex += 1

    drawData(data, ["lightgreen" if x >= left and x <= right else "white" for x in range(len(data))])
    time.sleep(timeTick)

def getColorArrayMergeSort(length, left, middle, right):
    colorArray = []

    for i in range(length):
        if i >= left and i <= right:
            if i >= left and i <= middle:
                colorArray.append("yellow")
            else:
                colorArray.append("pink")
        else:
            colorArray.append("white")
    return colorArray