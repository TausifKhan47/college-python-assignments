file = open("example.txt",'w')
file.write("""Python is a simple yet powerful programming language.  
Mitesh Solanki Sir teaches us Python with clear and practical examples.  
Learning Python makes problem-solving easier and more interesting.
""")

file.close()

with open("example.txt", 'r') as f1:
    lines_list = f1.readlines()

print(lines_list)
