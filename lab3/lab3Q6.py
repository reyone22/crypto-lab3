import random

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def modinv(a, p):
    m0, x0, x1 = p, 0, 1
    if p == 1:
        return 0
    while a > 1:
        q = a // p
        m0, a, p = a, p, a % p
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1

def find_primitive_root(p):
    primitive_roots = []
    for g in range(2, p):
        is_primitive = True
        for i in range(1, p - 1):
            if pow(g, i, p) == 1:
                is_primitive = False
                break
        if is_primitive:
            primitive_roots.append(g)
    return primitive_roots

def generate_keys(p):
    g = random.choice(find_primitive_root(p))
    x = random.randint(2, p - 2)
    h = pow(g, x, p)
    return (p, g, h), x

def elgamal_encrypt(public_key, m):
    p, g, h = public_key
    y = random.randint(2, p - 2)
    k = pow(h, y, p)
    c1 = pow(g, y, p)
    c2 = (k * m) % p
    return c1, c2

def elgamal_decrypt(private_key, p, c1, c2):
    x = private_key
    k = pow(c1, x, p)
    k_inv = modinv(k, p)
    m = (c2 * k_inv) % p
    return m

if __name__ == "__main__":
    
    p = 503  
    public_key, private_key = generate_keys(p)
    print(f"Public Key: {public_key}")
    print(f"Private Key: {private_key}")
    
    message = 234  
    ciphertext = elgamal_encrypt(public_key, message)
    print(f"Encrypted Message: {ciphertext}")
    
    decrypted_message = elgamal_decrypt(private_key, public_key[0], ciphertext[0], ciphertext[1])
    print(f"Decrypted Message: {decrypted_message}")
