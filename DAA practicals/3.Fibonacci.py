def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


# Example usage
n = 35
fibonacci_number = fibonacci_recursive(n)
print(f"The {n}th Fibonacci number is {fibonacci_number}")
