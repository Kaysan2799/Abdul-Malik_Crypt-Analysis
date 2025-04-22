import math

def fermat_factorization(n):
    """Factorizes n using Fermat's factorization method."""
    a = math.isqrt(n) + 1  # Equivalent to ⌈√n⌉
    print(f"\nInitial a (⌈√{n}⌉): {a}")

    while True:
        b_squared = a * a - n
        b = math.isqrt(b_squared)  # Integer square root
        print(f"Trying a = {a}: b² = {b_squared}, b ≈ {b}")

        if b * b == b_squared:  # Check if b_squared is a perfect square
            break
        a += 1

    factor1 = a + b
    factor2 = a - b
    return factor1, factor2

def main():
    print("\n" + "=" * 100)
    print(" " * 30 + "Fermat's DOS Algorithm")
    print("=" * 100 + "\n")

    print("[INFO] Fermat's method factors an odd integer n = a² - b² = (a+b)(a-b).")
    print("[INFO] It works best when n has two close prime factors.\n")

    n = int(input("Enter an odd integer n to factorize: "))
    if n % 2 == 0:
        print("[ERROR] n must be odd for Fermat's method!")
        return

    factor1, factor2 = fermat_factorization(n)

    print("\n" + "-" * 50)
    print(f"Factorization Result:")
    print(f"n = {n} = {factor1} × {factor2}")
    print("-" * 50 + "\n")

if __name__ == "__main__":
    main()
