import csv
with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Tosif", "Python", 95])
    writer.writerow(["Aansh", "PWP", 90])
    writer.writerow(["Ashutosh", "DBMS", 88])
    file.close()

import csv
with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
