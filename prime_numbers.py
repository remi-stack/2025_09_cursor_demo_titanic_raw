def get_first_n_primes(n):
    """
    Returns the first n prime numbers.
    
    Args:
        n (int): Number of prime numbers to return
        
    Returns:
        list: List of the first n prime numbers
    """
    if n <= 0:
        return []
    
    primes = []
    candidate = 2
    
    while len(primes) < n:
        is_prime = True
        
        # Check if candidate is divisible by any previously found prime
        for prime in primes:
            if prime * prime > candidate:
                break
            if candidate % prime == 0:
                is_prime = False
                break
        
        if is_prime:
            primes.append(candidate)
        
        candidate += 1
    
    return primes


def get_first_20_primes():
    """
    Returns the first 20 prime numbers.

    Returns:
        list: List of the first 20 prime numbers

    Example:
        >>> get_first_20_primes()
        [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
    """
    return get_first_n_primes(20)


if __name__ == "__main__":
    # Test the function
    first_20_primes = get_first_20_primes()
    print("The first 20 prime numbers are:")
    print(first_20_primes)
    print(f"\nTotal count: {len(first_20_primes)}")
