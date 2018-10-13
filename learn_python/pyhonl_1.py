l1 = [1,2,3]
l1.append(4)
def test1(*l):
    l2 = []
    for i in l:
        l2.append(i)
    l2.append(5)        
    return l2

# l2 = test1(*l1)

# print(l1)
# print(l2)

def test2(arg1,arg2):
    print(arg1)
    pass

test2(1,2)

print("wai ? Fei yuan zai ma?")

