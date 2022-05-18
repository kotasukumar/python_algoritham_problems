def sort(array):
    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key

    return array


if __name__ == "__main__":
    list_to_sort = ["banana", "orange", "apple"]
    result = sort(list_to_sort)
    print(result)
