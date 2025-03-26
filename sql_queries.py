import sqlite3

conn = sqlite3.connect('Artistc.db')
cursor = conn.cursor()
cursor.execute('''SELECT * FROM artists''')
data = cursor.fetchall()
conn.commit()



# Запитання 1. Інформація про скількох художників представлена у базі даних?
cursor.execute('''SELECT COUNT(*) FROM artists;''')
data = cursor.fetchall()
conn.commit()
print(data)



# Запитання 2. Скільки жінок (Female) у базі?
cursor.execute('SELECT COUNT(*) FROM artists WHERE Gender = "Female";')
data = cursor.fetchall()
conn.commit()
print(data)



# Запитання 3. Скільки людей у базі даних народилися до 1900 року?
cursor.execute('SELECT COUNT(*) FROM artists WHERE "Birth Year" < 1900;')
data = cursor.fetchall()
conn.commit()


# Запитання 4*. Як звати найстаршого художника?
cursor.execute('''SELECT Name FROM artists ORDER BY "Birth Year"''')
data = cursor.fetchone()
conn.commit()
print(data)
