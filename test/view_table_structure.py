import sqlite3

# 连接到 SQLite 数据库
conn = sqlite3.connect('../data/chinook/chinook.db')

# 获取游标对象
cursor = conn.cursor()

# 查询数据库中的所有表
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

# 输出每个表的结构，包括主键和外键
for table_name in tables:
    table_name = table_name[0]  # 表名
    print(f"\nTable: {table_name}")

    # 获取表的列信息（包括主键）
    cursor.execute(f"PRAGMA table_info('{table_name}');")
    columns = cursor.fetchall()

    # 输出列的信息
    print("Columns:")
    for column in columns:
        col_id, col_name, col_type, not_null, default_value, is_primary_key = column
        print(
            f"  - Column: {col_name}, Type: {col_type}, Primary Key: {is_primary_key}, Not Null: {not_null}, Default: {default_value}")

    # 获取外键信息
    cursor.execute(f"PRAGMA foreign_key_list('{table_name}');")
    foreign_keys = cursor.fetchall()

    # 输出外键信息
    if foreign_keys:
        print("Foreign Keys:")
        for fk in foreign_keys:
            # fk的各个字段包括：id, seq, table, from, to, on_update, on_delete, match
            print(
                f"  - From Column: {fk[3]}, References Table: {fk[2]}, References Column: {fk[4]}, On Update: {fk[5]}, On Delete: {fk[6]}")
    else:
        print("  No Foreign Keys.")

# 关闭连接
conn.close()
