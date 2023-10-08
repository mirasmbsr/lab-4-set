sequence = input().split()
seen_numbers = set()

for number in sequence:
    number = int(number)
    if number in seen_numbers:
        print("YES")
    else:
        seen_numbers.add(number)
        print("NO")