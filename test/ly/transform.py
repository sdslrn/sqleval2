import re

def format_sql_to_one_line(sql_query: str) -> str:
    # 使用空格替换换行符，并移除多余的空格
    one_line_sql = " ".join(sql_query.splitlines())
    # 使用正则表达式替换多个连续的空格为一个
    one_line_sql = re.sub(r'\s+', ' ', one_line_sql)
    return one_line_sql.strip()

# 示例输入的SQL字符串
sql_query = """
UPDATE tracks
SET UnitPrice = (
  SELECT AVG(UnitPrice)
  FROM tracks AS t2
  WHERE t2.GenreId = tracks.GenreId
)
WHERE GenreId IS NOT NULL;
"""

# 调用函数
one_line_sql = format_sql_to_one_line(sql_query)
print(one_line_sql)
