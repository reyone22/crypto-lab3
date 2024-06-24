def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def euler_totient(n):
    count = 0
    for i in range(1, n):
        if gcd(n, i) == 1:
            count += 1
    return count


def is_primitive_root(g, n):
    if gcd(g, n) != 1:
        return False

    phi = euler_totient(n)
    powers = set()
    for i in range(1, phi + 1):
        powers.add(pow(g, i, n))

    return len(powers) == phi


def find_primitive_roots(n):
    primitive_roots = []
    for g in range(1, n):
        if is_primitive_root(g, n):
            primitive_roots.append(g)
    return primitive_roots


if __name__ == "__main__":
    n = int(input("Enter a modulus n to find its primitive roots: "))
    roots = find_primitive_roots(n)
    print(f"Primitive roots of {n} are: {roots}")
