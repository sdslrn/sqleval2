import sqlite3


def test_sql_query():
    """
    测试给定的 SQL 是否可以在 SQLite 数据库上运行，并回滚以防止修改。
    同时检测 SQL 语句是否会造成数据更新，并打印影响的行数。
    :return: True 如果 SQL 可以成功运行，否则返回 False
    """
    db_path = '../../data/chinook/chinook.db'

    sql_query = """
DELETE FROM invoices
WHERE CustomerId IN (
    SELECT CustomerId FROM (
        SELECT CustomerId, COUNT(InvoiceId) AS InvoiceCount
        FROM invoices
        GROUP BY CustomerId
        ORDER BY InvoiceCount DESC
        LIMIT 1
    )
);
    """
    conn = None
    try:
        # 连接数据库
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # 开始事务
        conn.execute('BEGIN')

        # 执行 SQL 查询并获取受影响的行数
        cursor.execute(sql_query)
        affected_rows = cursor.rowcount  # 获取更新的行数

        if affected_rows > 0:
            print(f"SQL query would update {affected_rows} rows.")
        else:
            print("No rows would be updated by the SQL query.")

        # 回滚事务以避免实际更改
        conn.rollback()

        print("SQL query executed successfully (no changes were made).")
        return True

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return False

    finally:
        # 关闭连接
        if conn:
            conn.close()


print(test_sql_query())
