n = int(input("n = "))
def f(n):
    if n == 3:
        return 1
    return f(n-1)+f(n-2)

print(f(n))
