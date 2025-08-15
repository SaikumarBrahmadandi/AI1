import pandas as pds
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}
# Add a 'Last Name' column and extend the dataset to 20 rows
data['Last Name'] = [
    'Smith', 'Steve', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis', 'Rodriguez', 'Martinez',
    'Hernandez', 'Lopez', 'Gonzalez', 'Wilson', 'Anderson', 'Thomas', 'Taylor', 'Moore', 'Jackson', 'Martin'
]
data['Name'] = [
    'Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hannah', 'Ian', 'Julia',
    'Kevin', 'Laudaa', 'Mike', 'Ninna', 'Oscar', 'Pauli', 'Quinn', 'Rachel', 'Steve', 'Tina'
]
data['Age'] = [
    25, 33, 35, 40, 28, 32, 27, 29, 31, 33,
    26, 34, 36, 38, 24, 39, 37, 23, 22, 21
]
data['City'] = [
    'New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose',
    'Austin', 'Jacksonville', 'Fort Worth', 'Columbus', 'Charlotte', 'San Francisco', 'Indianapolis', 'Seattle', 'Denver', 'Washington'
]
data['Experience'] = [
    2, 5, 8, 10, 3, 6, 4, 7, 9, 1,
    2, 5, 8, 10, 3, 6, 4, 7, 9, 1
]
data['Salary'] = [
    50000, 60000, 70000, 80000, 52000, 61000, 53000, 62000, 54000, 63000,
    55000, 64000, 56000, 65000, 57000, 66000, 58000, 67000, 59000, 68000
]

df = pds.DataFrame(data)
print(df)
