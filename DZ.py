import sqlite3
import random
conn=sqlite3.connect('table1')
cursor=conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS table1
(id INTEGER PRIMARY KEY AUTOINCREMENT,col1 INT,col2 INT) ''')
# a=random.randint(0,9)
# b=random.randint(0,9)
l=[(random.randint(0,9),random.randint(0,9)),
   (random.randint(0,9),random.randint(0,9)),
   (random.randint(0,9),random.randint(0,9)),
   (random.randint(0,9),random.randint(0,9))]
cursor.executemany('''INSERT INTO table1(col1,col2) VALUES (?,?)''',l)
#conn.commit()
cursor.execute('''SELECT col1,col2 FROM table1''')
k=cursor.fetchall()
print('Заполненная таблица')
for i in k:
   print(*i)
cursor.execute('''SELECT avg(col1),avg(col2) FROM table1''')
average_col=cursor.fetchall()
#print(average_col)
for i in average_col:
   sum_duple=sum(i)
   average_result=sum(i)/len(i)
print('Среднее арифмитическое всех значений из колонки один и два ',average_result)
if average_result>len(k):
   cursor.execute('''DELETE FROM table1 WHERE id=4''')
   cursor.execute('''SELECT col1,col2 FROM table1''')
   k1 = cursor.fetchall()
   print('Таблица после удаления четвертой записи ')
   for i in k1:
      print(*i)




