def test(i):
    if i==1:
        return i
    if i==2:
        return i
    return test(i-1)+test(i-2)

print(test(40))