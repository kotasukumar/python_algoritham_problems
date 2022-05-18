def iterator(list1):
    if len(list1) == 0:
        return []
    if len(list1) == 1:
        return [list1]
    iterator_list = []
    for i in range(len(list1)):
        m = list1[i]
        rem_list1 = list1[:i] + list1[i + 1:]
        for p in iterator(rem_list1):
            iterator_list.append([m] + p)

    return iterator_list


def recursion(word):
    if len(word) > 1:
        recursion_list = []
        for i in range(0, len(word)):
            for variation in recursion(word[:i] + word[i + 1:]):
                variation.append(word[i])
                recursion_list.append(variation)
        return recursion_list
    else:
        return [word]


if __name__ == "__main__":
    string = list(input("Enter a word: "))
    iterator_result = iterator(string)
    recursion_result = recursion(string)
    print(iterator_result)
    print(recursion_result)
