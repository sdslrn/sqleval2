import sqlite3

# 连接到数据库（如果数据库不存在，则会创建一个新的）
conn = sqlite3.connect('../data/univdb-sqlite-tmp.db')

# 创建一个游标对象（用于执行SQL命令）
cursor = conn.cursor()


def update_operation(sql):
    # 执行sql语句并返回受影响的行数
    cursor.execute(sql)
    conn.commit()
    print("Number of rows that were updated: ", cursor.rowcount)


if __name__ == '__main__':
    # 所有教师的工资将增长5%
    # sql = "update instructor set salary = salary * 1.05;"

    # 只给那些工资低于70000美元的教师涨工资
    # sql = "update instructor set salary = salary * 1.05 where salary < 70000;"

    # 对工资低于平均数的教师涨5%的工资
    # sql = "update instructor set salary = salary * 1.05 where salary < (select avg(salary) from instructor);"

    # 给工资超过100000美元的教师涨3%的工资，其余教师涨5%的工资，使用case结构
    # sql = "update instructor set salary = case when salary > 100000 then salary * 1.03 else salary * 1.05 end;"

    # 我们把每个student元组的tot_cred属性值设为该生成功学完的课程学分的总和。假设如果一个学生在某门课程上的成绩既不是”F“，也不是空，那么他成功学完了这门课程。使用set子句。
    # sql = "update student set tot_cred = (select sum(credits) from takes natural join course where student.ID = takes.ID and takes.grade <> 'F' and takes.grade is not null);"

    # 如果一个学生没有成功学完任何课程，上述更新操作将使其tot_cred属性值为null。想把这些学生的tot_cred属性值设为0。
    # sql = "update student set tot_cred = (select case when sum(credits) is not null then sum(credits) else 0 end from takes natural join course where student.ID = takes.ID and takes.grade <> 'F' and takes.grade is not null);"

    update_operation(sql)