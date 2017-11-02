class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next


class UnorderedList:
    def __init__(self):
        self.head = None

    def add(self, item):
        temp = ListNode(item)
        temp.set_next(self.head)
        self.head = temp

    def find(self, item):
        current = self.head
        found = False
        while current and not found:
            if current.item() == item:
                found = True
            else:
                current = current.get_next()
        return found

    def remove(self, item):
        prev = None
        current = self.head
        found = False
        while current and not found:
            if current.item() == item:
                found = True
            else:
                prev = current
                current = current.get_next()

        if not prev:
            self.head = current.get_next()
        else:
            prev.set_next(current.get_next())

    def list_print(self):
        res = []
        current = self.head
        while current:
            res.append(current.get_data())
            current = current.get_next()

        print res


class OrderedList:
    def __init__(self):
        self.head = None

    def list_print(self):
        res = []
        current = self.head
        while current:
            res.append(current.get_data())
            current = current.get_next()

        print res

    def find(self, item):
        current = self.head
        stop = False
        found = False

        while current is not None and not stop and not found:
            print current
            if current.get_data() == item:
                found = True
            elif current.get_data() > item:
                stop = True
            else:
                current = current.get_next()

        return found

    def add(self, item):
        current = self.head
        previous = None
        stop = False

        while current is not None and not stop:
            if current.get_data() > item:
                stop = True
            else:
                previous = current
                current = current.get_next()

        temp = ListNode(item)
        if previous is None:
            temp.set_next(current)
            self.head = temp
        else:
            temp.set_next(current)
            previous.set_next(temp)

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        stop = False

        while current is not None and not found and not stop:
            if current.get_data() == item:
                found = True
            elif current.get_data() > item:
                stop = True
            else:
                previous = current
                current = current.get_next()

        if found:
            if previous is None:
                self.head = current.get_next()
            else:
                previous.set_next(current.get_next)


if __name__ == "__main__":
    ol = OrderedList()
    ol.add(1)
    ol.list_print()

    ol.add(0)
    ol.list_print()

    print "found" if ol.find(1) else "not found"

    ol.remove(1)
    print "found" if ol.find(1) else "not found"
