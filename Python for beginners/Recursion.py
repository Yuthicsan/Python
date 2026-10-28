#Recursion is when a function calls itself to solve a smaller version of the same problem.

def say_hello(n):
    if n == 0:
        return

    print("Hello")
    say_hello(n - 1) # calling itself


say_hello(3)

# factorial


def say_hello(n):
    if n == 0:
        return

    print("Hello")
    say_hello(n - 1)


say_hello(3)