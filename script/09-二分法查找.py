def search(data, item):
    left, right = 0, len(data) - 1

    while left <= right:
        middle = (left + right) // 2

        if item < data[middle]:
            right = middle - 1
        elif item > data[middle]:
            left = middle + 1
        else:
            return middle

    return  -1

firstSearch = search([2, 3, 4, 8, 10], 0)
print(firstSearch)
secondSearch = search([2, 3, 4, 8, 10], 8)
print(secondSearch)