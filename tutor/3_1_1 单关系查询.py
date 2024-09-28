import sqlite3

# 连接到数据库（如果数据库不存在，则会创建一个新的）
conn = sqlite3.connect('../data/univdb-sqlite.db')

# 创建一个游标对象（用于执行SQL命令）
cursor = conn.cursor()


def query_operation(sql):
    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows:
        print(row)


if __name__ == '__main__':
    # 找出所有教师的名字
    # sql = "select name from instructor;"

    # 找出所有教师所在的系名
    # sql = "select dept_name from instructor;"

    # 找出所有教师所在的系名（去重）
    # sql = "select distinct dept_name from instructor;"

    # 找出所有教师所在的系名（不去重）
    # sql = "select all dept_name from instructor;"

    # 找出所有教师的名字和所在的系名，并且对工资进行四则运算，给每位教师加薪10%
    # sql = "select ID, name, dept_name, salary * 1.1 from instructor;"

    # 找出所有在Comp. Sci.系并且工资大于70000美元的教师的姓名
    # sql = "select name from instructor where dept_name = 'Comp. Sci.' and salary > 70000;"

    query_operation(sql)
