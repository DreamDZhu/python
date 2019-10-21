class MyListIterator(object):

    def __init__(self, data):
        self.data = data
        self.now = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.now < self.data:
            self.now += 1
            return self.now - 1
        raise StopIteration


my_list = MyListIterator(5)
for i in my_list:
    print(i)
