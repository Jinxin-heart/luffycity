import pymysql

conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='luffycity_user',
    password='luffycity',
    database='luffycity',
    charset='utf8mb4',
    ssl_disabled=True,
)

with open('test_data.sql', 'r', encoding='utf-8') as f:
    sql = f.read()

cursor = conn.cursor()
for stmt in sql.split(';'):
    stmt = stmt.strip()
    if stmt:
        cursor.execute(stmt)

conn.commit()
print('导入成功')
conn.close()
