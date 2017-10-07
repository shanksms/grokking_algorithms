def count_element(x):
    if len(x) > 0:
        return 1 + count_element(x[1:])
    else:
        return 0


if __name__ == '__main__':
    print(count_element([1, 2, 3]))
