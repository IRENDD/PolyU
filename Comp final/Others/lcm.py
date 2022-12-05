# LCM
def lcm(n, m):
    rem = n % m
    if rem == 0:
        return n
    return int(n * lcm(m, rem) / rem)

n = int(input("Enter: "))
m = int(input("Enter: "))

print(lcm(n, m))
