'''array = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]
for i in range(0, 9):
    j = i
    while array[j] > array[j + 1]:
        temp = array[j + 1]
        array[j + 1] = array[j]
        array[j] = temp
        j= j - 1
        print(array)
    print(array)

'''


array = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]
for i in range(0, len(array) - 1):
    j = i
    while array[j] > array[j + 1]:
        array[j], array[j + 1] = array[j + 1], array[j]
        j = j - 1
        print(array)
