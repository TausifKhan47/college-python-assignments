file = open("file1.txt",'w')
file.write("""Python makes complex tasks simple.
Mitesh Solanki Sir teaches with good examples.
We learn by practicing every day.
""")
file.close()

file = open("file2.txt",'w')
file.write("""File handling is an important skill.
Merging files is a useful operation.
Keep experimenting and improving.
""")
file.close()

file = open("merged.txt",'w')
file.write("""
""")
file.close()

file1 = open("file1.txt", 'r')
content1 = file1.read()
file1.close()

file2 = open("file2.txt", 'r')
content2 = file2.read()
file2.close()

file = open("merged.txt", 'w')
file.write(content1 + "\n" + content2)
file.close()

with open("file1.txt",'r') as f1:  
    data = f1.read() 
print("The Text in File1 is:\n",data)

with open("file2.txt",'r') as f1:  
    data = f1.read() 
print("\nThe Text in File2 is:\n",data)


with open("merged.txt",'r') as f1:  
    data = f1.read() 
print("\nThe Text in merged file is:\n",data)