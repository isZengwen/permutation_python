def pr(n):
    count = 0
    for i in range(10**(n-1),10**(n)):
        length = len(set(str(i)))
        if length == n and ('0' not in set(str(i))):
            count += 1
            print(i)
    print("The number is :{}".format(count))
if __name__ == '__main__':
    pr(2)