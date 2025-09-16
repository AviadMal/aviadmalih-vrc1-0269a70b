def print_fibonacci(n):
    """
    Function to print the Fibonacci sequence up to n terms.
    """
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')  
        a, b = b, a + b
    print()  # for newline

if __name__ == '__main__':
    terms = int(input('Enter the number of Fibonacci terms to print: '))
    print_fibonacci(terms)