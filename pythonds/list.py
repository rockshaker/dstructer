class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

    @property
    def data(self):
        return self.data

    @data.setter
    def data(self, new_data):
        self.data = new_data

    @property
    def next(self):
        return self.next

    @next.setter
    def next(self, new_next):
        self.next = new_next


class UnorderedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        temp = ListNode(data)
        temp.next(self.head)
        self.head = temp

    def find(self, data):
        current = self.head
        found = False
        while current and not found:
            if current.data() == data:
                found = True
            else:
                current = current.next()
        return found

    def remove(self, data):
        prev = None
        current = self.head
        found = False
        while current and not found:
            if current.data() == data:
                found = True
            else:
                prev = current
                current = current.next()
        # FIXME: Not a complete situation
        prev.next(current.next())
