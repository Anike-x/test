x = [y + _ for y in range(100) for _ in range(1000)]
y = set(1000 * y for y in range(100))
print(y)
print(min(x))
print(max(x))
print(sum(x))