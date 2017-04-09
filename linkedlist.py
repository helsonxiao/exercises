class Node(object):
    '''
    data:节点的数据
    _next:保存下个节点对象（包含下个节点数据和下下个节点对象）
    '''
    def __init__(self, data, _next=None):
        self.data = data
        self._next = _next

    def __repr__(self):
        '''
        定义Node的字符输出
        print(Node)时输出data
        '''
        return str(self.data)


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.length = 0

    def isEmpty(self):
        return (self.length == 0)

    def append(self, dataOrNode):
        item = None # item用于存放待添加的数据
        if isinstance(dataOrNode, Node):
            item = dataOrNode
        else:
            item = Node(dataOrNode)

        if not self.head:
            self.head = item
            self.length += 1
        else: # 使用node来指向链表的最后一个元素，给它后头再加元素。
            node = self.head
            while node._next:
                node = node._next
            node._next = item
            self.length += 1

    def delete(self, index):
        if self.isEmpty():
            print("This linked list is empty.")
            return
        if index < 0 or index >= self.length:
            print("error: out of index")
            return

        j = 0
        prev = self.head
        node = self.head
        while node._next and j < index:
            prev = node
            node = node._next
            j += 1
        if j == index:
            prev._next = node._next
            self.length -= 1

    def update(self, data, index):
        if self.isEmpty() or index<0 or index>self.length:
            print("error: out of index")
            return

        j = 0
        node = self.head
        while node._next and j < index:
            node = node._next
            j += 1
        if j == index:
            node.data = data

    def insert(self, dataOrNode, index):
        if self.isEmpty():
            print("This linked list is empty")
        if index < 0 or index >= self.length:
            print("error: out of index")
            return

        item = None
        if isinstance(dataOrNode, Node):
            item = dataOrNode
        else:
            item = Node(dataOrNode)

        if index == 0:
            item._next = self.head
            self.head = item
            self.length += 1
            return

        j = 0
        prev = self.head
        node = self.head
        while node._next and j < index:
            prev = node
            node = node._next
            j += 1
        if j == index:
            item._next = prev._next
            prev._next = item
            self.length += 1

    def getElem(self, index):
        if self.isEmpty():
            print("This linked list is empty")
        if index < 0 or index >= self.length:
            print("error: out of index")
            return

        j = 0
        node = self.head
        while node._next and j < index:
            node = node._next
            j += 1
        if j == index:
            return node.data

    def getIndex(self, data):
        if self.isEmpty():
            print("This linked list is empty")

        j = 0
        node = self.head
        while node:
            node = node._next
            j += 1
            if node.data == data:
                return j

        if j == self.length:
            print("%s not found.", data)
            return

    def clear(self):
        self.head = None
        self.length = 0

    def __repr__(self):
        if self.isEmpty():
            return "This linked list is empty."
        node = self.head
        nlist = ""
        while node:
            nlist += str(node.data) + ' '
            node = node._next
        return nlist


ll = LinkedList()
for i in range(10):
    ll.append(i)

print(ll)
print(ll.getIndex(5))
ll.update(10, 0)
print(ll)
ll.delete(10)
ll.delete(0)
print(ll)
ll.insert(100, 0)
print(ll)
print(ll.getElem(5))