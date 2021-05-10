all_nums = input()
ret = []
for number in all_nums:
    if number is not all_nums[0]:
        ret.append((int(number) + first_num)/2)
        first_num = int(number)
    else:
        first_num = int(number)
print(ret)
