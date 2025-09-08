n = input("Enter a number: ")

if len(n) == 1:
    swapped = n
else:
    swapped = n[-1] + n[1:-1] + n[0]

print("Number after swapping first and last digits:", swapped)
