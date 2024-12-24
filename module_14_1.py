import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

# cursor.execute('''
# CREATE TABLE IF NOT EXISTS Users(
#     id INTEGER PRIMARY KEY,
#     username TEXT NOT NULL,
#     email TEXT NOT NULL,
#     age INTEGER,
#     balance INTEGER NOT NULL
# )
# ''')
#
# cursor.execute('CREATE INDEX IF NOT EXISTS idx_email ON Users(email)')

# for i in range(1, 11):
#     cursor.execute(f'''
#         INSERT INTO users (username, email, age, balance)
#         VALUES ('User{i}', 'example{i}@gmail.com', {i * 10}, 1000)
#     ''')

# cursor.execute('''
#     UPDATE Users
#     SET balance = 500
#     WHERE (id - 1) % 2 = 0
# ''')

# cursor.execute('''
#     DELETE FROM Users
#     WHERE (id - 1) % 3 = 0
# ''')

# cursor.execute('''
#     DELETE FROM Users
#     WHERE id = 6
# ''')

# cursor.execute('''
#     SELECT username, email, age, balance
#     FROM Users
#     WHERE age != 60
# ''')

results = cursor.fetchall()

# for result in results:
#     print(f'Имя: {result[0]} | Почта: {result[1]} | Возраст: {result[2]} | Баланс: {result[3]}')

cursor.execute('''
    SELECT COUNT(*)
    FROM Users
''')
total_users = cursor.fetchone()[0]

cursor.execute('''
    SELECT SUM(balance)
    FROM Users
''')
all_balances = cursor.fetchone()[0]

average_balance = all_balances / total_users if total_users > 0 else 0

print(average_balance)

connection.commit()
connection.close()
