def sort(word_list):
    for i in range(len(word_list)):
        for j in range(len(word_list)):
            if word_list[i] < word_list[j]:
                word_list[i], word_list[j] = word_list[j], word_list[i]

    return word_list


if __name__ == "__main__":
    list_to_sort = [5, 1, 12, 4]
    result = sort(list_to_sort)
    print(result)