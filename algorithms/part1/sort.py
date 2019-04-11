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


a = [4, 3, 0, 9, 7, 5]
print(insert_sort(a))
