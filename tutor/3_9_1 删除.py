import sqlite3

# 连接到数据库（如果数据库不存在，则会创建一个新的）
conn = sqlite3.connect('../data/univdb-sqlite-tmp.db')

# 创建一个游标对象（用于执行SQL命令）
cursor = conn.cursor()


def delete_operation(sql):
    # 执行sql语句并返回受影响的行数
    cursor.execute(sql)
    conn.commit()
    print("Number of rows that were deleted: ", cursor.rowcount)


if __name__ == '__main__':
    # 从instrucotr关系中删除与Finance系教师相关的所有元组
    # sql = "delete from instructor where dept_name = 'Finance';"

    # 删除所有工资在13000美元到15000美元之间的教师
    # sql = "delete from instructor where salary between 13000 and 15000;"

    # 从instrucotr关系中删除所有这样的元组，他们在位于Waston大楼的系工作
    # sql = "delete from instructor where dept_name in (select dept_name from department where building = 'Watson');"

    # 删除工资低于大学平均工资的教师记录
    # sql = "delete from instructor where salary < (select avg(salary) from instructor);"

    delete_operation(sql)
