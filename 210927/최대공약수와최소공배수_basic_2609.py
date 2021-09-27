def gcd(a,b):
    return b if a%b ==0 else gcd(b,a%b)

a, b = map(int,input().split())

print(gcd(a,b), (a*b)//gcd(a,b),sep='\n')

# while b:
#     a,b =b,a%b