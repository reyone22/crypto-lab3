import random


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def generate_large_prime():
    while True:
        num = random.randint(1000, 10000)
        if is_prime(num):
            return num


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1

def generate_keys():
    p = generate_large_prime()
    q = generate_large_prime()
    while q == p:
        q = generate_large_prime()

    n = p * q
    phi = (p - 1) * (q - 1)

    e = random.randint(2, phi - 1)
    while gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)

    d = mod_inverse(e, phi)

    return ((n, e), (n, d))


def encrypt(public_key, plaintext):
    n, e = public_key
    ciphertext = [pow(ord(char), e, n) for char in plaintext]
    return ciphertext


def decrypt(private_key, ciphertext):
    n, d = private_key
    plaintext = ''.join([chr(pow(char, d, n)) for char in ciphertext])
    return plaintext


public_key, private_key = generate_keys()
print("Public Key:", public_key)
print("Private Key:", private_key)

message = "Hello, RSA!"
print("Original Message:", message)

encrypted_message = encrypt(public_key, message)
print("Encrypted Message:", encrypted_message)

decrypted_message = decrypt(private_key, encrypted_message)
print("Decrypted Message:", decrypted_message)
