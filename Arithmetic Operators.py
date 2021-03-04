def AddSubPro(a,b):
    return a+b, a-b, a*b


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    x,y,z=AddSubPro(a,b)
    print(x)
    print(y)
    print(z)
