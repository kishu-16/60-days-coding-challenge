nums = list(map(int, input("Enter numbers separated by space: ").split()))

count = 0
for num in nums:
    if len(str(abs(num))) % 2 == 0:
        count += 1

print("Count of numbers with even digits:", count)
