num = [12,34,65,81,45,22,21,11,10]

even = 0
odd = 0

for n in num:
    if n % 2 == 0:
        even += 1
    else:
        odd +=1

print(f"Odd Numbers = {odd}")
print(f"Even Numbers = {even}")