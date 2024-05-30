l = [100,200,300,400,500]
key = 600

def linear_search(l, key):
    for value in l:
       if key == value:
            return True
    else:
        return False


result = linear_search(l,key)
print(result)

