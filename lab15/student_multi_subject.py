import sqlite3

conn = sqlite3.connect('multi_subject_record.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS student_record (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Enrollment INTEGER NOT NULL,
        name TEXT NOT NULL,
        subject TEXT NOT NULL,
        Mark INTEGER NOT NULL
    )
''')
conn.commit()

student_record = [
    (92301733016, 'ASHUTOSH KUMAR SINGH', 'PWP', 95),
    (92301733016, 'ASHUTOSH KUMAR SINGH', 'Python', 89),
    (92301733017, 'HARSH TRIVEDI', 'PWP', 85),
    (92301733017, 'HARSH TRIVEDI', 'Maths', 88),
    (92301733027, 'VIRAJ VAGHASIYA', 'PWP', 90)
]

cursor.executemany('''
    INSERT INTO student_record (Enrollment, name, subject, Mark)
    VALUES (?, ?, ?, ?)
''', student_record)
conn.commit()

cursor.execute('SELECT * FROM student_record')
rows = cursor.fetchall()

print("All Student Records (Multiple Subjects):")
for row in rows:
    print(row)

enroll = 92301733016  # You can change this to test

cursor.execute('SELECT name, subject, Mark FROM student_record WHERE Enrollment = ?', (enroll,))
subjects = cursor.fetchall()

print(f"\nSubjects enrolled by student {enroll}:")
for sub in subjects:
    print(sub)

conn.close()
