def insert_sort(list_=None):
    if list_ is None:
        list_ = []
    for i in range(1, len(list_)):
        key = list_[i]
        j = i - 1
        while j >= 0 and list_[j] > key:
            list_[j+1] = list_[j]
            j -= 1
        list_[j+1] = key
    return list_


def select_sort(list_=None):
    if list_ is None:
        list_ = []
    for i in range(0, len(list_)-1):
        key = list_[i]
        index = i + 1
        for j in range(i+1, len(list_)):
            if list_[j] < key:
                key = list_[j]
                index = j
        if index != i+1:
            list_[index] = list_[i]
            list_[i] = key
    return list_


def merge_sort(list_=None):
    return list_


a = [4, 3, 0, 9, 7, 5]
#print(insert_sort(a))
print(select_sort(a))
