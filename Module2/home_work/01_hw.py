n = int(input())
m = int(input())
r = int(input())

if r < n * m and ((r % n == 0) or (r % m == 0)):
    print("YES")
else:
    print("NO")
