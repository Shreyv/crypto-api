def extended_euclidean_inverse(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        div = b // a
        rem = b % a
        n, r1, d1 = extended_euclidean_inverse(rem, a)
        return (n, d1 - div * r1, r1)

if  __name__ == '__main__':
    a,b = map(int,input("Enter two numbers a and b (seperated by space)\n").split())
    result = extended_euclidean_inverse(a,b)
    if result[0] != 1:
        print("Inverse of "+str(a)+" is not possible under modulus "+str(b))
    else:
        print("c= " + str(a)+" inv mod "+ str(b))
        print("c = "+str(result[1]%b))
    result = extended_euclidean_inverse(b, a)
    if result[0] != 1:
        print("Inverse of " + str(b) + " is not possible under modulus " + str(a))
    else:
            print("d= " + str(b) + " inv mod " + str(a))
            print("d = " + str(result[1] % a))