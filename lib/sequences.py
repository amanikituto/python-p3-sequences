def print_fibonacci(n):
    """
    Prints the Fibonacci sequence up to the length provided in the function's parameters.

    Args:
        n: The length of the Fibonacci sequence to print.
    """

    # Initialize the first two Fibonacci numbers
    a, b = 0, 1

    # Initialize the list to store the Fibonacci sequence
    fib_sequence = []

    # Add the first two Fibonacci numbers to the list
    if n > 0:
        fib_sequence.append(a)
    if n > 1:
        fib_sequence.append(b)

    # Calculate and add the remaining Fibonacci numbers to the list
    for _ in range(2, n):
        c = a + b
        fib_sequence.append(c)
        a, b = b, c

    # Print the Fibonacci sequence
    print(fib_sequence)