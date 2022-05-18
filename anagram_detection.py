def check_anagram(str1, str2):
    reverse = str2[::-1]

    if str1 == reverse:
        return True
    else:
        return False


if __name__ == "__main__":
    result = check_anagram("abcd", "dcba")
    print(result)
