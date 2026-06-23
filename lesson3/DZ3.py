import sqlite3
import pandas as pd

#данные посетителей магазина: id, пол, возраст, доход, рейтинг трат
 

# 1. Читаем CSV
df = pd.read_csv('Mall_Customers.csv')

# Учитываем, что в колонках есть пробелы — переименуем
df.columns = [
    'CustomerID',
    'Genre',
    'Age',
    'Annual_Income',
    'Spending_Score'
]

# 2. Создаём подключение к базе (файл создастся автоматически)
conn = sqlite3.connect('mall_customers.db')
cursor = conn.cursor()

# 3. Создаём таблицу
cursor.execute('''
CREATE TABLE IF NOT EXISTS customers (
    CustomerID TEXT PRIMARY KEY,
    Genre TEXT,
    Age INTEGER,
    Annual_Income INTEGER,
    Spending_Score INTEGER
)
''')

# 4. Загружаем данные
df.to_sql('customers', conn, if_exists='append', index=False)

# 5. Сохраняем изменения
conn.commit()
conn.close()

print("Данные успешно загружены в базу данных!")