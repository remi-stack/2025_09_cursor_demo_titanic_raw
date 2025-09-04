def get_first_n_primes(n):
    def is_prime(num):
        """Check if a number is prime."""
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    
    return primes


def get_first_10_primes():
    return get_first_n_primes(10)


if __name__ == "__main__":
    # Get and display the first 10 prime numbers
    first_10_primes = get_first_10_primes()
    print(f"The first 10 prime numbers are: {first_10_primes}")