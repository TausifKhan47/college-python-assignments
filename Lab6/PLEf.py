n = int(input("Enter a number: "))
product = 1

while n > 0:
    digit = n % 10       
    product *= digit          
    n //= 10            

print("Product of digits:", product)
