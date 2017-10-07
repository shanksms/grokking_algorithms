def max_number_in_list(x, max_number):
    if len(x) <= 0:
        return max_number
    else:
        if max_number < x[0]:
            max_number = x[0]
        return max_number_in_list(x[1:], max_number)

if __name__ == '__main__':
    print(max_number_in_list([1, 3, 2, 9], -1000))
