def fibonacci(number):
    # return 0 and 1 for first and second terms
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        # return the sum of two numbers
        return fibonacci(number - 1) + fibonacci(number - 2)

max_item_input = input("Enter the number of items in Fibonacci series\n")
max_item = int(max_item_input)

for count in range(max_item):
    print(fibonacci(count))
