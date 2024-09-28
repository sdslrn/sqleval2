import sqlite3

# 连接到数据库（如果数据库不存在，则会创建一个新的）
conn = sqlite3.connect('../data/univdb-sqlite.db')

# 创建一个游标对象（用于执行SQL命令）
cursor = conn.cursor()

sql = "SELECT name FROM sqlite_master WHERE type = 'table';"
cursor.execute(sql)
rows = cursor.fetchall()
for row in rows:
    print(row)

sql = "SELECT * FROM instructor;"
cursor.execute(sql)
rows = cursor.fetchall()
for row in rows:
    print(row)
# 输出instructor表的列名
print([desc[0] for desc in cursor.description])

print(type(rows[0]))
print(type(rows))
