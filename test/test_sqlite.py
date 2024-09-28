import sqlite3

# 连接到数据库（如果数据库不存在，则会创建一个新的）
conn = sqlite3.connect('example.db')

# 创建一个游标对象（用于执行SQL命令）
cursor = conn.cursor()

# 创建表
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
''')

# 提交事务
conn.commit()

# 插入数据
cursor.execute("INSERT INTO users (name) VALUES (?)", ("Alice",))
cursor.execute("INSERT INTO users (name) VALUES (?)", ("Bob",))

# 提交事务
conn.commit()

# 查询数据
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

# 输出查询结果
for row in rows:
    print(row)

# 更新数据
cursor.execute("UPDATE users SET name = ? WHERE id = ?", ("Charlie", 1))

# 提交事务
conn.commit()

# 删除数据
cursor.execute("DELETE FROM users WHERE id = ?", (2,))

# 提交事务
conn.commit()

# 关闭游标和连接
cursor.close()
conn.close()
