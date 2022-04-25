
def mergesort(self, data):
    if len(data) == 1 or len(data) == 0:
        return data
    else:
        middle = (len(data)-1)//2
        first = merge(data[:middle])
        second = merge(data[middle:])
        return merge(first,second)

def merge(self, left, right):
    