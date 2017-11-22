import sqlite3 as sql

con = sql.connect('census.db')

cur = con.cursor()
cur.execute('''CREATE TABLE Density(Province TEXT, Population INTEGER, Area REAL)''')
con.commit()

table = [
    ('Newfoundland and Labrador',512930, 370501.69),
    ('Prince Edward Island', 135294, 5684.39),
    ('Nova Scotia', 908007, 52917.43),
    ('New Brunswick', 729498, 71355.67),
    ('Quebec', 7237479, 1357743.08),
    ('Ontario', 11410046, 907655.59),
    ('Manitoba', 1119583, 551937.87),
    ('Saskatchewan', 978933, 586561.35),
    ('Alberta', 2974807, 639987.12),
    ('British Columbia', 3907738, 926492.48),
    ('Yukon Territory', 28674, 474706.97),
    ('Northwest Territories', 37360, 1141108.37),
    ('Nunavut', 26745, 1925460.18),
    ]

for row in table:
    cur.execute('INSERT INTO Density VALUES (?, ?, ?)', row)
con.commit()

cur.execute('SELECT * FROM Density')
for row in cur.fetchall():
    print(row)

cur.execute('SELECT Population FROM Density')
for row in cur.fetchall():
    print(row)

cur.execute('''SELECT Province FROM Density WHERE Population < 1000000 OR Population
> 5000000''')
for row in cur.fethcall():
    print(row)

cur.execute('''SELECT Province FROM Density WHERE(Population < 1000000 OR Population >
5000000)''')
for row in cur.fetchall():
    print(row)

cur.execute('''SELECT Province FROM Density WHERE NOT(Population < 1000000 OR Population >
5000000)''')
for row in cur.fetchall():
    print(row)

cur.execute('''SELECT Population FROM Density WHERE Area > 200000''')
for row in cur.fetchall():
    print(row)

cur.execute('''SELECT Population FROM Density WHERE Area > 200000''')
for row in cur.fetchall():
    print(row)
