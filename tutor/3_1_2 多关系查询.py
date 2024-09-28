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
    # 从 instructor 和 department 表中选择了教师的姓名、教师所在的系名以及建筑物的信息。通过 instructor.dept_name = department.dept_name条件将两个表连接起来，确保只返回那些在相同系里的教师和对应部门信息的结果。
    # sql = "select name, instructor.dept_name, building from instructor, department where instructor.dept_name = department.dept_name;"

    # 从 instructor 和 teaches 表中选择了教师的姓名和教授的课程号。通过 instructor.ID = teaches.ID 条件将两个表连接起来，确保只返回那些在 teaches表中有对应记录的教师和课程信息的结果。
    # sql = "select name, course_id from instructor, teaches where instructor.ID = teaches.ID;"

    # 从 instructor 和 teaches 表中选择了教师的姓名和教授的课程号。通过 instructor.ID = teaches.ID 和 instructor.dept_name = 'Comp. Sci.' 条件将两个表连接起来，确保只返回那些在 teaches表中有对应记录的教师和课程信息的结果，并且这些教师所在的系名是 Comp. Sci.。
    # sql = "select name, course_id from instructor, teaches where instructor.ID = teaches.ID and instructor.dept_name = 'Comp. Sci.';"

    query_operation(sql)
