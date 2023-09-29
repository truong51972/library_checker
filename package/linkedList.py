class LinkedList:
    class Node:

        def __init__(self, element, _next = None):
            self._element = element
            self.next = _next

        def get_element(self):
            return self._element

    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def __getitem__(self, index):
        currentNode = self._head
        if self.checkValidIndex(index):
            for i in range(self._size):
                if i == index:
                    return currentNode.get_element()
                currentNode = currentNode.next

    def getHeadId(self):
        return self._head
    
    def checkValidIndex(self, index):
        if (index > (self._size - 1)) or (index < 0):
            print('Invalid index!')
            return False
        return True
    
    def isNoneHead(self):
        if self._head == None:
            print("List is empty!")
            return True
        return False
    
    def pop(self):
        if self._size > 0:
            returnValue = self._head.get_element()
            self._head = self._head.next
            self._size -= 1
            return returnValue
        else:
            return None

    def push(self, obj):
        if self._head is None:
            self._head = self.Node(obj)
        else:
            self._head = self.Node(obj, self._head)
        self._size += 1

    def __str__(self):
        currentNode = self._head
        str_out = ''

        for i in range(self._size):
            str_out += f'{currentNode.get_element()}'
            # print(currentNode.get_element())
            currentNode = currentNode.next
            if i <= (self._size - 2):
                str_out += ', '
        return '[{}]'.format(str_out)

    def printList(self):
        currentNode = self._head
        str_out = ''

        for i in range(self._size):
            str_out += f'{currentNode.get_element()}'
            currentNode = currentNode.next
            if i <= (self._size - 2):
                str_out += ', '
        print('[{}]'.format(str_out))

    def addToHead(self, value):
        self.push(value)


    def addToTail(self, value):
        currentNode = self._head
        while True:
            if currentNode.next == None:
                currentNode.next = self.Node(value)
                break
            currentNode = currentNode.next
        self._size += 1

    def addAfter(self, index, value):
        currentNode = self._head
        if self.checkValidIndex(index):
            for i in range(self._size + 1):
                if i == index:
                    newNode = self.Node(value, currentNode.next)
                    currentNode.next = newNode
                    self._size += 1
                else:
                    currentNode = currentNode.next

    def traverse(self):
        currentNode = self._head
        for i in range(self._size):
            print(f'Value: {currentNode.get_element()}, Next address: {(currentNode.next)}')
            currentNode = currentNode.next

    def deleteFromHead(self):
        if not (self.isNoneHead()):
            self._head = self._head.next
            self._size -= 1

    def deleteFromTail(self):
        if not (self.isNoneHead()):
            currentNode = self._head
            for i in range(self._size):
                if i == (self._size - 1):
                    currentNode.next = None
                    self._size -= 1
                else:
                    currentNode = currentNode.next

    def deleteAfter(self, p):
        if not (self.isNoneHead()):
            currentNode = self._head
            for i in range(self._size):
                if i == p:
                    tempNode = currentNode.next
                    currentNode.next = tempNode.next
                    self._size -= 1
                else:
                    currentNode = currentNode.next

    def deleteByValue(self, value):
        if not (self.isNoneHead()):
            currentNode = self._head
            if (currentNode.get_element() == value): self.deleteFromHead()
            for i in range(self._size -1):
                if (currentNode.next).get_element() == value:
                    currentNode.next = (currentNode.next).next
                    self._size -= 1
                    return
                else:
                    currentNode = currentNode.next
            print(f'{value} is not in list!')


    def search(self, value):
        if not (self.isNoneHead()):
            currentNode = self._head
            for i in range(self._size):
                if a := currentNode.get_element() == value:
                    return i
                currentNode = currentNode.next

    def count(self):
        return self._size
    
    def deleteByIndex(self, index):
        if not (self.isNoneHead()):
            currentNode = self._head
            if(self.checkValidIndex(index)):
                if (index == 0):
                    self.deleteFromHead()
                else:
                    for i in range(self._size):
                        if i == (index - 1):
                            currentNode.next = (currentNode.next).next
                            self._size -= 1
                        else:
                            currentNode = currentNode.next

    def sort(self):
        if not (self.isNoneHead()):
            currentNode = self._head
            for i in range(self._size - 1):
                # self.printList()
                nextNode = currentNode.next
                if ((a := nextNode.get_element()) < currentNode.get_element()):
                    currentNode.next = nextNode.next
                    if (a < (self._head.get_element())):
                        nextNode.next = self._head
                        self._head = nextNode
                    else:
                        currentNode_j = self._head
                        for j in range(i):
                            nextNode_j = currentNode_j.next
                            if (nextNode_j.get_element() > a):
                                currentNode_j.next = nextNode
                                nextNode.next = nextNode_j
                            else:
                                currentNode_j = nextNode_j
                else:
                    currentNode = nextNode
                    # nextNode = currentNode.next

    def toArray(self):
        if not (self.isNoneHead()):
            returnValue = []
            currentNode = self._head
            for i in range(self._size):
                returnValue.append(currentNode.get_element())
                currentNode = currentNode.next
            return returnValue

    def isSorted(self):
        currentNode = self._head
        for i in range(self._size - 1):
            if currentNode.get_element() > (currentNode.next).get_element():
                return False
            currentNode = currentNode.next
        return True

    def mergeList(self, linkedList):
        if (linkedList.isSorted() and self.isSorted()):
            indexB = 0
            currentNode = self._head
            if linkedList[indexB] < currentNode.get_element():
                newNode = self.Node(linkedList[indexB])
                # print(linkedList[indexB])
                indexB += 1
            else:
                newNode = self.Node(currentNode.get_element())
                # print(currentNode.get_element())
                currentNode = currentNode.next
            newSize = 1
            currentNewNode = newNode
            while True:
                if (currentNode != None) and (indexB != len(linkedList)):
                    if linkedList[indexB] < currentNode.get_element():
                        currentNewNode.next = self.Node(linkedList[indexB])
                        currentNewNode = currentNewNode.next
                        indexB += 1
                    else:
                        currentNewNode.next = self.Node(currentNode.get_element())
                        currentNewNode = currentNewNode.next
                        currentNode = currentNode.next
                    newSize += 1
                elif (currentNode == None) and (indexB != len(linkedList)):
                    currentNewNode.next = self.Node(linkedList[indexB])
                    currentNewNode = currentNewNode.next
                    indexB += 1
                    newSize += 1
                elif (currentNode != None) and (indexB == len(linkedList)):
                    currentNewNode.next = self.Node(currentNode.get_element())
                    currentNewNode = currentNewNode.next
                    currentNode = currentNode.next
                    newSize += 1
                else:
                    break
                # print(newNode.get_element())

            self._head = newNode
            self._size = newSize

    def addBefore(self, index, value):
        currentNode = self._head
        if self.checkValidIndex(index):
            if index == 0:
                self.push(value)
            else:
                for i in range(self._size + 1):
                    if i == index -1:
                        newNode = self.Node(value, currentNode.next)
                        currentNode.next = newNode
                        self._size += 1
                    else:
                        currentNode = currentNode.next

    def attach(self, linkedList):
        # newNode = linkedList.getHeadId()
        currentNode = self._head
        while True:
            if currentNode.next == None:
                currentNode.next = linkedList.getHeadId()
                break
            currentNode = currentNode.next
        self._size += len(linkedList)

    def max(self):
        currentNode = self._head
        maxValue = currentNode.get_element()

        for i in range(self._size - 1):
            if (maxValue < (a:= currentNode.next.get_element())):
                maxValue = a
            currentNode = currentNode.next
        
        return maxValue

    def min(self):
        currentNode = self._head
        minValue = currentNode.get_element()

        for i in range(self._size - 1):
            if (minValue > (a:= currentNode.next.get_element())):
                minValue = a
            currentNode = currentNode.next
        
        return minValue
    
    def sum(self):
        currentNode = self._head
        total = currentNode.get_element()

        for i in range(self._size - 1):
            total += currentNode.next.get_element()
            currentNode = currentNode.next
        
        return total
    
    def average(self):
        return self.sum()/self._size

    def insert(self, value):
        currentNode = self._head
        if currentNode.get_element() > value:
            self.push(value)

        else:
            for i in range(self._size - 1):
                if(value <= currentNode.next.get_element()):
                    currentNode.next = self.Node(value, currentNode.next)
                    self._size += 1
                    return
                currentNode = currentNode.next
            currentNode.next = self.Node(value, currentNode.next)
            self._size += 1
    
    def reverse(self):
        currentNode = self._head
        newNode = self.Node(currentNode.get_element())

        for i in range(self._size - 1):
            newNode = self.Node(currentNode.next.get_element(), newNode)
            currentNode = currentNode.next
        
        self._head = newNode
    
    def isTheSame(self, linkedList):
        if (self._size == len(linkedList)):
            currentNode_a = self._head
            index_b = 0

            for i in range(self._size):
                if (linkedList[index_b] != currentNode_a.get_element()):
                    return False
                currentNode_a = currentNode_a.next
                index_b += 1
        else:
            return False
        return True
    
if __name__ == '__main__':
    listA = StackList()
    listB = StackList()

    for i in range(10):
        listA.push(i)
        listB.push(i)

    # listB.deleteFromTail()
    listA.push('hahaha')
    print(listA.pop())
    print(listB)
    print(listA.isTheSame(listB))
    listA.attach(listB)
    print(listA)