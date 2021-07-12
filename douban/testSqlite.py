import sqlite3

conn = sqlite3.connect("test.db")    # open or create database file

print("Opened database successfully")
c = conn.cursor()

sql1 = '''
    SELECT id,name,address,salary from company;
'''

sql2 = '''
    INSERT INTO company(name, age, address, salary) 
    values ('李四', 32, 'chongqing', 15000);
'''
cursor = c.execute(sql1)
for row in cursor:
    print("id=", row[0], "name=", row[1], "address=", row[2], "salary=", row[3])
# c.execute(sql2)
# conn.commit()
conn.close()

print("create...")