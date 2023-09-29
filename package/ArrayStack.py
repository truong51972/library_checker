class ArrayStack:
    def __init__(self) -> None:
        self._data = []

    def __len__(self):
        return len(self._data)
    
    def isEmpty(self):
        return len(self._data) == 0

    def push(self, value):
        self._data.append(value)
    
    def top(self):
        if self.isEmpty():
            raise IndexError('Array is empty')
        return self._data[-1]
    
    def pop(self):
        if self.isEmpty():
            raise IndexError('Array is empty')
        return self._data.pop()

    def clear(self):
        self._data = []

    def traversal(self):
        print(self.data)
        
    def cvtBinary(self):
        try:
            self._data, oldData = [], self._data
            result = 0

            for index, element in enumerate(oldData):
                ara = element*(10**(len(oldData) - index - 1))
                result += ara

            result = str(bin(result))

            for i, e in enumerate(result):
                if not (i < 2):
                    self._data.append(e)
            return self._data
        except:
            print('Error!')

    def __str__(self):
        result = ""
        for k in range(len(self._data)):
            
            if str(type(self._data[k])) == "<class 'int'>":
                result += str(self._data[k])
            elif str(type(self._data[k])) == "<class 'str'>":
                result += "'"
                result += str(self._data[k])
                result += "'"
            else:
                result += "<{0} object at {1}>".format(str(type(self._data[k]))[7:-1], hex(id(self._data[k])))
            if k < len(self._data) -1:
                result += ', '

            
        return '[{}]'.format(result)


        return str(self._data)


if __name__ == '__main__':
    s = ArrayStack()
    s.push(5)
    s.push(1)
    s.push(9)
    s.push(7)
    s.push(2)
    
    print(s.cvtBinary())