import  random
def miller_rabin(n):
    if n == 2:
        return 1
    elif n % 2 == 0:
        return  0
    else:
        m = n -1
        p = 1
        while m % (2 ** p) != 0:
            p += 1
        q = m // (2 ** p)
        rd = random.randrange(2,m)
        if pow(rd,q,n) == 0:
            return  1
        for i in range(1,51):
            r = pow(rd,(2**i)*q,n)
            if r == m or r == 1:
                return  1
        return 0

if  __name__ == '__main__':
    n =int(input("Enter the number to check its primality\n"))
    print("Output: "+str(miller_rabin(n)))