

# Factorial operation using recursive function


def factorial(n):

 if (n<=1):
    return n
 else:
    return n * factorial(n-1)

print("The result is: ", factorial(int(input("Enter a number: "))))
