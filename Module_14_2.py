import sqlite3


connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')
cursor.execute('CREATE INDEX IF NOT EXISTS idx_email ON Users(email)')

for i in range(1, 11):
     cursor.execute('INSERT INTO Users(username, email, age, balance) VALUES(?, ?, ?, ?)',
                    (f"User{i}", f"example{i}@gmail.com", str(i * 10), "1000"))

for j in range(1, 11, 2):
    cursor.execute('UPDATE Users SET balance=? WHERE username=?', (500, f'User{j}'))

for k in range(1, 11, 3):
    cursor.execute('DELETE FROM Users WHERE id=?', (f'{k}',))

cursor.execute('SELECT username, email, age, balance FROM Users WHERE age != ?', (60, ))
users = cursor.fetchall()
for user in users:
    print(f'Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс: {user[3]}')

cursor.execute('DELETE FROM Users WHERE id=6') # удаления записи с id = 6

cursor.execute('SELECT COUNT(*) FROM Users')
cnt = cursor.fetchone()[0]
print(cnt) # общее количество записей в БД

cursor.execute('SELECT SUM(balance) FROM Users')
sum_balance = cursor.fetchone()[0]
print(sum_balance) # сумма балансов всех пользователей
print(sum_balance/cnt) # средний по БД (вариант 1)

cursor.execute('SELECT AVG(balance) FROM Users')
m_balance = cursor.fetchone()[0]
print(m_balance) # средний по БД (вариант 2)

connection.commit()
connection.close()
