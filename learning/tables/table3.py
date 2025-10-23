start = int(input("Enter a number: "))
end = int(input("Enter a number: "))
i = start
while i <= end:
    print(f"\nMultiplication table of {i}")
    print("-" * 25)

    j = 1
    while j <= 10:
        print(f"{i} x {j} = {i * j}")
        j += 1
    i += 1