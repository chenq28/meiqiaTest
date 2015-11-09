# -*- coding=utf-8 -*-
#DP思路求解，f(x, y) = min(f(xv, yv) + 1)
#易判断靠近方向，减少了一些计算量

BrandMin = 1
BrandMax = 8
MoveOffset = ((1,2), (2,1), (1, -2), (2, -1), (-1, -2), (-2,-1), (-1, 2), (-2, 1))
ResultMap = {}

def checkLegal(x, y):
    if x < BrandMin or x > BrandMax or y < BrandMin or y > BrandMax:
        return False
    return True

def checkPass(oldX, oldY, endX, endY, newX, newY):
    global ResultMap
    if not checkLegal(newX, newY):
        return False
    #check toward the right direct
    if abs(newX - endX) > abs(oldX - endX) and \
       abs(newY - endY) > abs(oldY - endY):
        return False
    return True
    
def initStart(startX, startY):
    global ResultMap
    ResultMap[(startX, startY)] = 0
    

def getPotentials(startX, startY, endX, endY):
    global ResultMap
    global MoveOffset
    ret = []
    startCoordinate = (startX, startY)
    assert ResultMap.has_key(startCoordinate)
    stepTemp = ResultMap[startCoordinate] + 1
    for offsetIter in MoveOffset:
        tempCoordinate = (startCoordinate[0] + offsetIter[0], startCoordinate[1] + offsetIter[1])
        if not checkPass(startX, startY, endX, endY, tempCoordinate[0], tempCoordinate[1]):
            continue
        if ResultMap.has_key(tempCoordinate):
            continue
        ResultMap[tempCoordinate] = stepTemp
        ret.append(tempCoordinate)
        #find
        if tempCoordinate[0] == endX and tempCoordinate[1] == endY:
            break
    return ret 
            
def searchBFS(startX, startY, endX, endY):
    global ResultMap
    if not checkLegal(startX, startY) or \
       not checkLegal(endX, endY):
        print 'params error'
        return -1
    initStart(startX, startY)
    endCoordinate = (endX, endY)
    potentials = getPotentials(startX, startY, endX, endY)
    if ResultMap.has_key(endCoordinate):
        print '%d steps' %(ResultMap[endCoordinate])
        return ResultMap[endCoordinate]
    for potentialIter in potentials:
        potentials += getPotentials(potentialIter[0], potentialIter[1], endX, endY)
        if ResultMap.has_key(endCoordinate):
            print '%d steps' %(ResultMap[endCoordinate])
            return ResultMap[endCoordinate]

    print 'can not reach that point'
    return -1

if __name__ == '__main__':
    searchBFS(1, 1, 4, 4)
