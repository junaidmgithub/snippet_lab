# This program is python version of code taken from https://github.com/kashish-jain/Tambola/blob/master/frontend/src/utils/utils.tsx
# Tambola Ticket Generation 
# 
import math
import random
import json
from functools import cmp_to_key
from pprint import pprint


def sort_fn(a, b):
    return a - b
sort_fn_cmp_key = cmp_to_key(sort_fn)

def getRandom(min, max):
    return math.floor(random.random() * (max - min + 1)) + min

def getNumberOfElementsInSet(_set):
    count = 0
    for i, _ in enumerate(_set):
        count = count + len(_set[i])
    return count

def getRowCount(house, rowIndex):
    count = 0
    for i in house[rowIndex]:
        if i != 0:
            count=+1
    return count

def getEmptyFullTicket():
    houses = [0, 0, 0, 0, 0, 0]
    for houseNo in range(6):
        house = []
        for rowNo in range(3):
            row = [0, 0, 0, 0, 0, 0, 0, 0, 0]
            house.append(row)
        houses[houseNo] = house
    return houses

def generate():

    col1 = []
    col2 = []
    col3 = []
    col4 = []
    col5 = []
    col6 = []
    col7 = []
    col8 = []
    col9 = []

    for i in range(1, 10):
        col1.append(i)
    for i in range(10, 20):
        col2.append(i)
    for i in range(20, 30):
        col3.append(i)
    for i in range(30, 40):
        col4.append(i)
    for i in range(40, 50):
        col5.append(i)
    for i in range(50, 60):
        col6.append(i)
    for i in range(60, 70):
        col7.append(i)
    for i in range(70, 80):
        col8.append(i)
    for i in range(80, 91):
        col9.append(i)

    columns = [
        col1, col2, col3,
        col4, col5, col6,
        col7, col8, col9,
    ]

    set1 = []
    set2 = []
    set3 = []
    set4 = []
    set5 = []
    set6 = []

    for i in range(9):
        set1.append([])
        set2.append([])
        set3.append([])
        set4.append([])
        set5.append([])
        set6.append([])

    sets = [set1, set2, set3, set4, set5, set6]

    # //   add 6 numbers from each column to each of the sets
    for i in range(9):
        col = columns[i]
        for j in range(6):
            randomNumIndex = getRandom(0, len(col) - 1)
            randomNum = col[randomNumIndex]
            _set = sets[j][i]
            _set.append(randomNum)
            del col[randomNumIndex]

    # // Assign 1 element of last col to a random set
    lastCol = columns[len(columns) - 1]
    randomNumIndex = getRandom(0, len(lastCol) - 1)
    randomNum = lastCol[randomNumIndex]
    randomSetIndex = getRandom(0, len(sets) - 1)
    randomSet = sets[randomSetIndex][8]
    randomSet.append(randomNum)
    del lastCol[randomNumIndex]

    # // 3 Passes over the columns
    for _pass in range(3):
        for j in range(9):
            col = columns[j]
            if len(col) == 0:
                continue
            randomNumIndex = getRandom(0, len(col) - 1)
            randomNum = col[randomNumIndex]
            vacantSetFound = False
            while (vacantSetFound == False):
                randomSetIndex = getRandom(0, len(sets) - 1)
                randomSet = sets[randomSetIndex]

                if (getNumberOfElementsInSet(randomSet) == 15
                        or len(randomSet[j]) == 2):
                    continue

                vacantSetFound = True
                randomSet[j].append(randomNum)
                del col[randomNumIndex]

    # // Last pass
    for j in range(9):
        col = columns[j]
        if (len(col) == 0):
            continue
        randomNumIndex = getRandom(0, len(col) - 1)
        randomNum = col[randomNumIndex]
        vacantSetFound = False
        while (vacantSetFound == False):
            randomSetIndex = getRandom(0, len(sets) - 1)
            randomSet = sets[randomSetIndex]
            if (getNumberOfElementsInSet(randomSet) == 15
                    or len(randomSet[j]) == 3):
                continue

            vacantSetFound = True
            randomSet[j].append(randomNum)
            del col[randomNumIndex]

    for i in range(6):
        for j in range(9):
            sets[i][j].sort(key=sort_fn_cmp_key)

    return sets

def putElements(_set, house):

    for i in range(9):
        # // Put the row which have three numbers
        if (len(_set[i]) == 3):
            for j in range(3):
                house[j][i] = _set[i][j]

    # // Now the cases where the column will have two numbers
    counter = 0
    columnIndicesWithTwoNums = []
    for i in range(9):
        if(len(_set[i]) == 2 ):
            columnIndicesWithTwoNums.append(i)

    lenColumnsWithTwoNums = len(columnIndicesWithTwoNums)
    for i in range(lenColumnsWithTwoNums):
        randomColumnIndexInArray = getRandom(0, len(columnIndicesWithTwoNums) - 1)
        actualRandomColumnIndex = columnIndicesWithTwoNums[randomColumnIndexInArray]
        preComp = [
            [0, 1],
            [0, 2],
            [1, 2],
        ]
        indices = preComp[counter % 3]
        house[indices[0]][actualRandomColumnIndex] = _set[actualRandomColumnIndex][0]
        house[indices[1]][actualRandomColumnIndex] = _set[actualRandomColumnIndex][1]
        del columnIndicesWithTwoNums[randomColumnIndexInArray]
        counter += 1

    # // Cases where column will have 1 number
    for i in range(9):
        if len(_set[i]) == 1:
            randomIndex = getRandom(0, 2)
            while (house[randomIndex][i] != 0 or
                   getRowCount(house, randomIndex) == 5):
                randomIndex = getRandom(0, 2)

            # // found the rowNo for this number
            house[randomIndex][i] = _set[i][0]

    return house

def generateTicket(numHouses):
    # // Full ticket of numbers get generated i.e. 6 houses
    sets = generate()
    fullTicket = getEmptyFullTicket()

    for i in range(numHouses):
        putElements(sets[i], fullTicket[i])

    finalTicket = [0] * numHouses
    for i in range(numHouses):
        house = [0] * 3
        for j in range(3):
            row = [0] * 9
            for k in range(9):
                row[k] = fullTicket[i][j][k]
            house[j] = row
        finalTicket[i] = house

    return finalTicket


# Test
t = generateTicket(3)
pprint(t)
