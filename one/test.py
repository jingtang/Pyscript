def doubleNum (num):
    i = num * 2
    return i

def oddNum(num):
    return num * 4

def myCall(num, fnc):
    return 1 + fnc(num)

if __name__ == "__main__":
    print("start")
    print(myCall(2, doubleNum))

