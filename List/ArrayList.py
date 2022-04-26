from xml.dom import NotFoundErr

class ArrayList:
    def __init__(self):
        self.elements = []
        self.size = 0;

    def showList(self):
        return self.elements

    def add(self, t):
        self.size += 1
        self.elements.append(t)
        return True

    def insertByIndex(self, idx, t):
        self.elements.append(0)
        self.size += 1
        for i in reversed(range(idx, self.size-1)):
            self.elements[i+1] = self.elements[i]
        self.elements[idx] = t
        return True

    def clear(self):
        self.elements = []
        self.size = 0
        return True

    def deleteByItem(self, t):
        for i, word in enumerate(self.elements):
            if word == t:
                self.deleteByIndex(i)
                return True
        raise NotFoundErr

    def deleteByIndex(self, idx):
        if 0 <= idx < self.size:
            for i in range(idx, self.size-1):
                self.elements[i] = self.elements[i+1]
            self.elements = self.elements[:-1]
            self.size -= 1
            return True
        else:
            raise IndexError

    def getByIndex(self, idx):
        if 0 <= idx < self.size:
            return self.elements[idx]
        else:
            raise IndexError

    def indexOf(self, t):
        for i, k in enumerate(self.elements):
            if k == t:
                return i
        return -1

    def isEmpty(self):
        return not self.size

    def contains(self, t):
        for i in self.elements:
            if i == t:
                return True
        return False

    def size(self):
        return self.size