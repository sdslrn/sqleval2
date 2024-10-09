import sqlite3

# 连接到数据库（如果数据库不存在，则会创建一个新的）
conn = sqlite3.connect('../data/sds/univdb-sqlite-tmp.db')

# 创建一个游标对象（用于执行SQL命令）
cursor = conn.cursor()


def insert_operation(sql):
    # 执行sql语句并返回受影响的行数
    cursor.execute(sql)
    conn.commit()
    print("Number of rows that were inserted: ", cursor.rowcount)


if __name__ == '__main__':
    # 想要插入的信息是Computer Science系开设的名为"Data Systems"的课程CS-437，有4个学分。
    # sql = "insert into course values ('CS-437', 'Data Systems', 'Comp. Sci.', 4);"

    # 想让Music系每个修满144学分的学生成为Music系的教师，其工资为18000美元。
    # sql = "insert into instructor select ID, name, dept_name, 18000 from student where dept_name = 'Music' and tot_cred > 144;"

    # 待插入元组中只给出了模式中部分属性的值，那么其余属性将被赋空值，用null表示。
    # sql = "insert into student values ('3003', 'Green', 'Finance', null);"

    insert_operation(sql)
