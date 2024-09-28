import sqlite3

# 替换为您的数据库文件路径
database_path = "E:\PostGraduate\Project\sqleval\dev\dev_20240627\dev_databases\dev_databases\card_games\card_games.sqlite"

# 连接到数据库
conn = sqlite3.connect(database_path)
cursor = conn.cursor()

# 获取所有表名
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

# 遍历每个表，获取其主键
for table in tables:
    table_name = table[0]
    print(f"表名：{table_name}")

    # 获取表的列信息
    cursor.execute(f"PRAGMA table_info('{table_name}');")
    columns = cursor.fetchall()

    # 查找主键列
    primary_keys = [col[1] for col in columns if col[5] == 1]

    if primary_keys:
        print(f"主键：{', '.join(primary_keys)}\n")
    else:
        print("主键：无\n")

# 关闭游标和连接
cursor.close()
conn.close()
