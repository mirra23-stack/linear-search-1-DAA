def linear_search(arr, target):
    for index in range(len(arr)):
        if arr[index] == target:
            return index
    return -1

dataset = [23, 18, 10, 11]
target = 18
result = linear_search(dataset, target)
print(result)