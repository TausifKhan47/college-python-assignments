import sqlite3

# Connect or create database
conn = sqlite3.connect('student_record.db')
cursor = conn.cursor()

# Create the table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS student_record (
        Enrollment INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        subject TEXT NOT NULL,
        Mark INTEGER NOT NULL
    )
''')
conn.commit()

# Clear old data to avoid duplicate Enrollment errors
cursor.execute("DELETE FROM student_record")
conn.commit()


# Insert multiple student records
student_record = [
    (92301733016, 'ASHUTOSH KUMAR SINGH', 'PWP', 95),
    (92301733017, 'HARSH VISHALBHAI TRIVEDI', 'PWP', 85),
    (92301733027, 'VIRAJ PRAKASHBHAI VAGHASIYA', 'PWP', 90),
    (92301733046, 'SHIVAM ATULKUMAR BHATT', 'PWP', 93),
    (92301733058, 'DEVENDRASINH DOLATSINH JADEJA', 'PWP', 75)
]

cursor.executemany('''
    INSERT INTO student_record (Enrollment, name, subject, Mark)
    VALUES (?, ?, ?, ?)
''', student_record)
conn.commit()

# Fetch all student records
cursor.execute('SELECT * FROM student_record')
rows = cursor.fetchall()

print("All Student Records:")
for row in rows:
    print(row)

# Fetch students with marks > 90
cursor.execute('SELECT name, subject, Mark FROM student_record WHERE Mark > 90')
high_marks = cursor.fetchall()

print("\nStudents with Marks greater than 90:")
for student in high_marks:
    print(student)

# Update mark for ASHUTOSH KUMAR SINGH
cursor.execute('''
    UPDATE student_record
    SET Mark = 98
    WHERE name = 'ASHUTOSH KUMAR SINGH' AND subject = 'PWP'
''')
conn.commit()

# Confirm the update
cursor.execute('SELECT name, Mark FROM student_record WHERE name = "ASHUTOSH KUMAR SINGH"')
updated_mark = cursor.fetchone()
print(f"\nUpdated Mark for {updated_mark[0]}: {updated_mark[1]}")

# Delete a specific student
cursor.execute('''
    DELETE FROM student_record
    WHERE name = 'DEVENDRASINH DOLATSINH JADEJA'
''')
conn.commit()

# Confirm deletion
cursor.execute('SELECT * FROM student_record WHERE name = "DEVENDRASINH DOLATSINH JADEJA"')
deleted = cursor.fetchone()
if deleted is None:
    print("\nDEVENDRASINH DOLATSINH JADEJA has been successfully deleted.")

# Calculate average mark
cursor.execute('SELECT AVG(Mark) FROM student_record')
avg_mark = cursor.fetchone()[0]

print(f"\nThe average mark of students is: {avg_mark:.2f}")

# Always close connection
conn.close()
