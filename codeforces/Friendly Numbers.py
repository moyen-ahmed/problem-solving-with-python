import sys
input = sys.stdin.readline

def digit_sum(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

t = int(input())
for _ in range(t):
    x = int(input())
    count = 0
    for y in range(x + 1, x + 131):
        if y - digit_sum(y) == x:
            count += 1
    print(count)
