#!usr/bin/python3

import sys

def prime_fact(n):
    factors = []
    divisor = 2
    while divisor <= n:
        if n % divisor == 0:
            factors.append(divisor)
            n = n // divisor
        else:
            divisor += 1
    return factors

def main(filename):
    with open(filename, 'r') as file:
        numbers = file.readlines()
        
    for num in numbers:
        num = int(num)
        factor_pairs = prime_fact(num)
        if factor_pairs:
            for pair in factor_pairs:
                print(f"{num} = {pair}*{num//pair}")
        else:
            print(f"Error: prime_fact({num.strip()}) returned an empty list")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: factors filename")
        sys.exit(1)
    filename = sys.argv[1]
    main(filename)
