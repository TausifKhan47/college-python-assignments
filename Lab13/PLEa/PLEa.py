file = open("example.txt",'w')
file.write("""Python is a simple yet powerful programming language.  
Mitesh Solanki Sir teaches us Python with clear and practical examples.  
Learning Python makes problem-solving easier and more interesting.
""")

file.close()

with open("example.txt",'r') as f1:  
    data = f1.read() 
print(data)

with open("example.txt", 'r') as f1:  
    data = f1.readlines()  
print("Number of lines:", len(data))

with open("example.txt", 'r') as f1:  
    data = f1.read()  
print("Number of words:", len(data.split()))

with open("example.txt", 'r') as f1:  
    data = f1.read()  
print("Number of characters:", len(data))
