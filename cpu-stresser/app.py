import os

# ineffecient code to find primes - we're just trying to use CPU and time it (source: https://dev.to/xfbs/generating-prime-numbers-with-python-and-rust-4663)
primes = []
max_attempts = int(os.environ.get("MAX_ATTEMPTS", 1000000))

for candidate in range(max_attempts):
    #print(f"Testing if {candidate} is prime.")
    is_prime = True
    for divisor in range(2, candidate - 1):
        if candidate % divisor == 0:
            #print(f"{candidate} is not prime.")
            is_prime = False
            break
    if is_prime:
        print(f"{candidate} is prime.")
        primes.append(candidate)

print(primes)