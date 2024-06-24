import random


def generate_large_prime():
    primes = [101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]
    return random.choice(primes)


def is_primitive_root(g, p):
    required_set = set(num for num in range(1, p) if gcd(num, p) == 1)
    return required_set == set(pow(g, powers, p) for powers in range(1, p))


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def generate_primitive_root(p):
    for g in range(2, p):
        if is_primitive_root(g, p):
            return g
    raise ValueError(f"No primitive root found for {p}")


def diffie_hellman():
    p = generate_large_prime()
    g = generate_primitive_root(p)

    print(f"Chosen prime number (p): {p}")
    print(f"Chosen primitive root (g): {g}")

    a = random.randint(1, p - 1)
    b = random.randint(1, p - 1)

    A = pow(g, a, p)
    B = pow(g, b, p)

    print(f"Alice's public key (A): {A}")
    print(f"Bob's public key (B): {B}")

    shared_secret_alice = pow(B, a, p)
    shared_secret_bob = pow(A, b, p)

    print(f"Alice's shared secret: {shared_secret_alice}")
    print(f"Bob's shared secret: {shared_secret_bob}")

    assert shared_secret_alice == shared_secret_bob, "Shared secrets do not match!"

    return shared_secret_alice


if __name__ == "__main__":
    shared_secret = diffie_hellman()
    print(f"Shared secret: {shared_secret}")
