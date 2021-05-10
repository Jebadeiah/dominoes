nums = input().split()
numbers = nums[::-1]
ret = ""
for num in numbers:
    ret += num+' '
print(ret.strip())
