import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('DELETE FROM Users WHERE id = ?', (6,))
print("Запись с id = 6 удалена.")

cursor.execute('SELECT COUNT(*) FROM Users')
total_records = cursor.fetchone()[0]
print(f"Общее количество записей: {total_records}")

cursor.execute('SELECT SUM(balance) FROM Users')
total_balance = cursor.fetchone()[0]
print(f"Сумма всех балансов: {total_balance}")

if total_records > 0:
    average_balance = total_balance / total_records
    print(f"Средний баланс всех пользователей: {average_balance:.2f}")
else:
    print("Нет записей для вычисления среднего баланса.")

connection.commit()
connection.close()
