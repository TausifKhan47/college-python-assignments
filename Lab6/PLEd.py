n=int(input("Enter the number:"))
ld=n%10
fd=n
while fd>=10:
    fd=fd//10

print("first digit:",fd)
print("Last digits:",ld)    