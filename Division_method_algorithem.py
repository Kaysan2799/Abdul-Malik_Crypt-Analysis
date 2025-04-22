import math

def find_factors(n):
    """Returns all factors of n using the division method."""
    factors = []
    for i in range(1, int(math.isqrt(n)) + 1):  # Check up to √n for efficiency
        if n % i == 0:
            factors.append(i)
            if i != n // i:  # Avoid duplicates (e.g., 5×5=25)
                factors.append(n // i)
    return sorted(factors)  # Return sorted list

def find_prime_factors(n):
    """Returns the prime factors of n using trial division."""
    prime_factors = []
    # Handle even numbers first
    while n % 2 == 0:
        prime_factors.append(2)
        n = n // 2
    # Check odd divisors up to √n
    for i in range(3, int(math.isqrt(n)) + 1, 2):
        while n % i == 0:
            prime_factors.append(i)
            n = n // i
    # If remaining n is a prime > 2
    if n > 2:
        prime_factors.append(n)
    return prime_factors

def main():
    print("=" * 120)
    print(" " * 40 + "Division Method to Find Factors")
    print("=" * 120 + "\n")

    print("[INFO] The division method checks divisibility from 1 to √n to find factors.")
    print("[INFO] Prime factors are determined by repeated division.\n")

    n = int(input("[Step 1] Enter a positive integer n: "))
    if n <= 0:
        print("[ERROR] n must be a positive integer!")
        return

    print(f"\n[Step 2] Calculating factors of {n}...")
    factors = find_factors(n)
    print(f"[Step 3] All factors of {n}: {', '.join(map(str, factors))}")

    prime_factors = find_prime_factors(n)
    print(f"[Step 4] Prime factors of {n}: {', '.join(map(str, prime_factors))}")

    print("\n" + "-" * 80)
    print(f"Factorization Summary:")
    print(f"n = {n} = {' × '.join(map(str, prime_factors)) if len(prime_factors) > 1 else 'prime'}")
    print("-" * 80 + "\n")

if __name__ == "__main__":
    main()
