import random

def miller_test(d, n):
    a = random.randint(2, n - 2)
    x = pow(a, d, n)
    if x == 1 or x == n - 1:
        return True
    while d != n - 1:
        x = (x * x) % n
        d *= 2
        if x == n - 1:
            return True
        if x == 1:
            return False
    return False

def miller_rabin(n, k=5):
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    r, d = 0, n - 1
    while d % 2 == 0:
        d //= 2
        r += 1
    for _ in range(k):
        if not miller_test(d, n):
            return False
    return True

def main():
    print("Miller-Rabin Primality Test")
    print("===========================")
    while True:
        try:
            number = int(input("Enter a number to test for primality (or '0' to exit): "))
            if number == 0:
                break
            k = int(input("Enter the number of iterations (recommended: 5-10): "))
            if k <= 0:
                print("Number of iterations must be positive. Using default value of 5.")
                k = 5
            is_probably_prime = miller_rabin(number, k)
            if is_probably_prime:
                print(f"{number} is probably prime.")
            else:
                print(f"{number} is composite.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
