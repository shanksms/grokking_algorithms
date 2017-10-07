def quick_sort(ls):

    if len(ls) < 2:
        return ls
    else:
        pivot = ls[0]
        smaller_ones = [ x for x in ls[1:] if x <= pivot]
        bigger_ones = [ x for x in ls[1:] if x > pivot]
        return quick_sort(smaller_ones) + [pivot] + quick_sort(bigger_ones)
    '''return smaller_ones
    '''


if __name__ == '__main__':
    print(quick_sort([1, 1, 1]))
