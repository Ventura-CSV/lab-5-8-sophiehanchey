def myfunc(lst):
    print(id(lst), 'ID of lst in myfunc() as soon as the function starts')
    lst[0] = 999
    print(id(lst), 'ID of lst in myfunc() after changing value of the 1st element')
    return lst


def main():
    n = [1, 2, 3]
    print(id(n))
    ret = myfunc(n)
    print(id(ret))


if __name__ == '__main__':
    main()
