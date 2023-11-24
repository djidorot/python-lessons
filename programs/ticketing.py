
total_price = 0

for i in range(5):
    age = int(input())
    if age < 3:
        continue
    total_price += 100

print("$" + str(total_price))
