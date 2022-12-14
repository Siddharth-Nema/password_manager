def search(a, b, c):
    ct1, ct2, ct3 = 0, 0, 0
    for item in c:
        if item == (a, b):
            ct1 += 1
            break
        if item[0] == a:
            ct2 += 1
            break
        if item[0] != a:
            l = list(item)
            l[0] = a
            item = tuple(l)
            if item == (a, b):
                ct3 += 1
                break

    if ct1 != 0:
        return 'a'
    elif ct2 != 0:
        return 'b'
    elif ct3 != 0:
        return 'c'
    else:
        return 'd'
