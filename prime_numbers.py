def is_prime(lower_limit, upper_limit):
    list = []
    count = 1
    for number in range(lower_limit, upper_limit):
        for j in range(2, number):
            if number % j == 0:
                break
        else:
            list.append(number)
    return list


if __name__ == "__main__":
    prime_list = is_prime(0, 1000)
    print(prime_list)
