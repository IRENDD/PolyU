# GCD
def gcd(n, m):
    if m == 0:
        return n
    return gcd(m, n % m)

#def lcm(n, m):
#    return (n * m) / gcd(n, m)
   
n = int(input("Enter: "))
m = int(input("Enter: "))

print(gcd(n, m))