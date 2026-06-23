numbers = [3, 7, 2, 9, 1, 5, 8, 4, 6, 10]
even_sum = []
total = 0

for number in numbers:
    if number % 2==0:
        even_sum.append(number)
        total = total+number

print(f"Even Numbers: {number}")
print(f"Total even sum: {total}")


