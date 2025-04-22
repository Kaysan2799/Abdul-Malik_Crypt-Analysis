# **Cryptanalysis Toolkit: Fermat's and Division Factorization Algorithms**  

## **Overview**  
This repository contains two fundamental integer factorization algorithms:  
1. **Fermat's Factorization Method** (for numbers with close prime factors).  
2. **Division Method** (for general factorization and prime extraction).  

These algorithms are useful in cryptanalysis, number theory, and cybersecurity (e.g., breaking RSA for small/modest keys).  

---

## **1. Fermat's Factorization Algorithm**  
**Purpose**: Efficiently factorize an odd integer `n` into two close primes using the difference of squares.  

### **Algorithm Steps**  
1. Express `n` as `n = a² - b² = (a + b)(a - b)`.  
2. Start with `a = ⌈√n⌉` and increment until `a² - n` is a perfect square (`b²`).  
3. The factors are `(a + b)` and `(a - b)`.  

### **Example**  
```python
n = 10403  
a = 102 → b² = 102² - 10403 = 1 → b = 1  
Factors: (102 + 1) × (102 - 1) = 103 × 101  
```  

### **Image Reference**  
![Fermat's Algorithm](ferments_DOS.jpg)  

### **When to Use**  
- `n` is odd.  
- The two prime factors are close (e.g., RSA semiprimes with small key differences).  

---

## **2. Division Factorization Method**  
**Purpose**: Find all factors and prime factors of any positive integer `n` via trial division.  

### **Algorithm Steps**  
1. Iterate from `1` to `√n`, checking divisibility.  
2. For prime factors, divide `n` repeatedly by primes ≤ `√n`.  

### **Example**  
```python
n = 60  
Factors: 1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60  
Prime Factors: 2 × 2 × 3 × 5  
```  

### **Image Reference**  
![Division Algorithm](division_method.jpg)  

### **When to Use**  
- General-purpose factorization.  
- Small to moderately large integers (not efficient for very large primes).  

---

## **Usage Instructions**  
1. Clone the repository:  
   ```bash
   git clone https://github.com/Abdul-Malik_Crypt-Analysis.git
   cd Abdul-Malik_Crypt-Analysis
   ```
2. Run the Python scripts:  
   ```bash
   python fermat_factorization.py  # For Fermat's method
   python division_method.py       # For trial division
   ```
3. Input an integer when prompted.  

---

## **Dependencies**  
- Python ≥ 3.8 (for `math.isqrt`).  
- No external libraries required.  

---

## **Contributing**  
Pull requests are welcome! For major changes, open an issue first.  

---

## **License**  
MIT License. See `LICENSE` for details.  

--- 

**Author**: Abdul-Malik  
**Repository Link**: [GitHub](https://github.com/Abdul-Malik_Crypt-Analysis)  

--- 

### **References**  
- [Fermat's Factorization (Wikipedia)](https://en.wikipedia.org/wiki/Fermat%27s_factorization_method)  
- [Trial Division (Wikipedia)](https://en.wikipedia.org/wiki/Trial_division)  

--- 

**Note**: For very large numbers (>100 digits), consider advanced methods like Pollard’s Rho or Quadratic Sieve.
