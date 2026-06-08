import math
print("\nThe Prime numbers between 1 to 500 are: \n")
primes_using_loop = []
for i in range(2, 501):
    for j in range(2, int(math.sqrt(i)+2)):
        if(i==j):
            break
        if i%j == 0:
            i = None
            break
    if(i!=None):
        primes_using_loop.append(i)
print(primes_using_loop)

#primes_using_list_c = [i for i in range(2, 501) if i=None and break if(i%j == 0) for j in range(2, int(math.sqrt(i)+2)))]