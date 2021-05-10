num = int(input())

if num in squares:
    print(squares.pop(num))
else:
    print("There is no such key")
print(squares)
