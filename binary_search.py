def search(sent, w):
    word_list = sent[0].split()
    for i in range(len(word_list)):
        if w in word_list[i]:
            return True
            break
    else:
        return False


if __name__ == "__main__":
    sentence = ["hi all good morning"]
    word = "all"
    result = search(sentence, word)
    print(result)
