def fibonacci(x):

    List = []
    f = 1
    List.append(f)
    List.append(f)
    while f<=x:
        f = List[-1] + List[-2]
        List.append(f)
    else:
        List.remove(List[-1])
        for i in range(0, len(List)):
            print List[i]


def checkio(opacity):
    opacity_max = 10000
    question = False

    while question is False:
        for i in range(0, 5000):
            if opacity == opacity_max:
                question is True
            else:
                    if fibonacci(i) == i:
                        opacity_max -= fibonacci(i)
                    else:
                        opacity_max += 1
            age = i

    return age


if __name__ == '__main__':
    assert checkio(10000) == 0, "Newborn"
    assert checkio(9999) == 1, "1 year"
    assert checkio(9997) == 2, "2 years"
    assert checkio(9994) == 3, "3 years"
    assert checkio(9995) == 4, "4 years"
    assert checkio(9990) == 5, "5 years"
print ('ok')
