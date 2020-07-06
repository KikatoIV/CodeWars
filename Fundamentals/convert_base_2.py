def binary(decimal):
    if decimal == 0:
        return 0
    else:
        new = bin(decimal)
        new = str(new)
        new = new[2:]
        int(new)
        return new

print(binary(1))

print(binary(5))

print(binary(10))
