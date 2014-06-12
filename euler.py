def gen_primes():
    """
        Prime Numbers Generator
    """
    D = {}
    q = 2
    while True:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1

def sum_squares(n):
    """
        sums a sequence of squares
        1^2 + 2^2 + ... + 10^2 = 385
    """
    sum = 0
    for i in range(1, n+1):
       sum += i*i
    return sum

def sum_sequence(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum

def fib(n, max=None):
    """
       Fibonnacci
    """
    ret = [1,2]
    for i in range(3, n+1):
        j = sum(ret[i-3:i-1])
        if max and j >= max:
            return ret
        ret.append(j)
    return ret

def mul_list(lst):
    """
        Multiply a List
    """
    n = 1
    for i in lst:
        n*=i
    return n

def is_prime(n):
    """
        Check if Number is Prime
    """
    for i in range(2, n):
        if n % i == 0:
            return False
    else:
        return True

def get_factors(n):
    """
        Return a list with a number's factors
    """
    factors = []
    for i in gen_primes():
       if (n % i == 0):
           factors.append(i)
       if mul_list(factors) == n:
           return factors


#----------------------------------
#      PROBLEM SOLUTIONS
#----------------------------------

def p1(n):
    """
        Euler Problem 1
    """
    sum = 0
    for i in range(1,n+1):
        if ((i%3)==0 or (i%5) == 0):
                sum+=i
    return sum

def p2(n):
    sum = 0
    for i in fib(n, max=n):
        if (i % 2 == 0):
            sum += i
    return sum


def p3(n):
    factors = get_factors(n)
    return factors[len(factors)-1]


def p6(n):
    i = sum_squares(n)
    tmp = sum_sequence(n)
    j = tmp*tmp
    return j-i

def p7(n):
    tmp = 0
    for i,j in zip(gen_primes(), range(n)):
        tmp = i
    return tmp

def p10(n):
    sum = 0
    for p in gen_primes():
       if p < n:
           sum+=p
       else:
           return sum


print(p1(999))
print(p2(4000000))
print(p3(600851475143))

print(p6(100))
print(p7(10001))

print(p10(2000000))
