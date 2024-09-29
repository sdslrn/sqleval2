requirement_1 = "find which tracks were composed by composer's name contain Smith."
sql_1 = """SELECT name,albumid,composer FROM tracks WHERE composer LIKE '%Smith%' ORDER BY albumid;"""
graph_1 = """
    "nodes": [
        {"id" : 1, "sql statement" : "SELECT name,albumid,composer FROM tracks;"},
        {"id" : 2, "sql statement" : "SELECT name,albumid,composer FROM tracks WHERE composer LIKE '%Smith%';"},
        {"id" : 3, "sql statement" : "SELECT name,albumid,composer FROM tracks WHERE composer LIKE '%Smith%' ORDER BY albumid;"}
    ],
    "edges": [
        {"source": 1, "target": 2},
        {"source": 2, "target": 3}
    ]
"""
example_template_1 = (f"# Requirement:\n{requirement_1}\n"
                      f"# Sql:\n{sql_1}\n"
                      f"# Graph:\n{graph_1}")

requirement_2 = ("We set the tot_cred attribute value of each student tuple to the sum of the credits of the courses "
                 "that the student has successfully completed. Assume that if a student's grade in a course is neither"
                 " 'F' nor null, then he has successfully completed the course. Use the set clause.")
sql_2 = "update student set tot_cred = (select sum(credits) from takes natural join course where student.ID = takes.ID and takes.grade <> 'F' and takes.grade is not null);"
graph_2 = """
    "nodes": [
        {"id" : 1, "sql statement" : "select sum(credits) from takes;"},
        {"id" : 2, "sql statement" : "select sum(credits) from takes natural join course;"},
        {"id" : 3, "sql statement" : "select sum(credits) from takes natural join course where student.ID = takes.ID and takes.grade <> 'F' and takes.grade is not null;"}
        {"id" : 4, "sql statement" : "update student set tot_cred = (select sum(credits) from takes natural join course where student.ID = takes.ID and takes.grade <> 'F' and takes.grade is not null);"}
    ],
    "edges": [
        {"source": 1, "target": 2},
        {"source": 2, "target": 3},
        {"source": 2, "target": 4}
    ]
"""
example_template_2 = (f"# Requirement:\n{requirement_2}\n"
                      f"# Sql:\n{sql_2}\n"
                      f"# Graph:\n{graph_2}")

requirement_3 = ("What is the complete address of the school with the lowest excellence rate? Indicate the Street, City,"
                 " Zip and State.xecellence Rate = NumGE1500 / NumTstTakr; complete address has Street, City, Zip, State")
sql_3 = "SELECT T2.Street, T2.City, T2.Zip, T2.State FROM schools AS T2 INNER JOIN (SELECT cds, CAST(NumGE1500 AS REAL) / NumTstTakr AS rate FROM satscores WHERE NumGE1500 IS NOT NULL AND NumTstTakr IS NOT NULL AND NumTstTakr != 0) AS T1 ON T2.CDSCode = T1.cds WHERE T1.rate = (SELECT MIN(CAST(NumGE1500 AS REAL) / NumTstTakr) AS min_rate FROM satscores WHERE NumGE1500 IS NOT NULL AND NumTstTakr IS NOT NULL AND NumTstTakr != 0) ORDER BY T2.CDSCode;"
graph_3 = """
    "nodes": [
        {"id" : 1, "sql statement" : "SELECT cds, CAST(NumGE1500 AS REAL) / NumTstTakr AS rate FROM satscores WHERE NumGE1500 IS NOT NULL AND NumTstTakr IS NOT NULL AND NumTstTakr != 0;"},
        {"id" : 2, "sql statement" : "select sum(credits) from takes natural join course;"},
        {"id" : 3, "sql statement" : "select sum(credits) from takes natural join course where student.ID = takes.ID and takes.grade <> 'F' and takes.grade is not null;"}
        {"id" : 4, "sql statement" : "update student set tot_cred = (select sum(credits) from takes natural join course where student.ID = takes.ID and takes.grade <> 'F' and takes.grade is not null);"}
    ],
    "edges": [
        {"source": 1, "target": 2},
        {"source": 2, "target": 3},
        {"source": 2, "target": 4}
    ]
"""
example_template_3 = (f"# Requirement:\n{requirement_3}\n"
                      f"# Sql:\n{sql_3}\n"
                      f"# Graph:\n{graph_3}")

sql_3 = """SELECT T2.Street, T2.City, T2.Zip, T2.State FROM schools AS T2 INNER JOIN (SELECT cds, CAST(NumGE1500 AS REAL) / NumTstTakr AS rate FROM satscores WHERE NumGE1500 IS NOT NULL AND NumTstTakr IS NOT NULL AND NumTstTakr != 0) AS T1 ON T2.CDSCode = T1.cds WHERE T1.rate = (SELECT MIN(CAST(NumGE1500 AS REAL) / NumTstTakr) AS min_rate FROM satscores WHERE NumGE1500 IS NOT NULL AND NumTstTakr IS NOT NULL AND NumTstTakr != 0) ORDER BY T2.CDSCode"""
requirement_3 = "Execellence Rate = NumGE1500 / NumTstTakr; complete address has Street, City, Zip, State"

prompt = ("The goal is to construct a directed graph representation from a given sqlite statements(SQL). "
          "This graph should faithfully reflect the sequence of topological execution of the atomic SQL statements to achieve the requirements. "
          "The following includes three cases, including Requirement, Sql, and Graph.\n\n"
          "## Example 1\n"
          f"{example_template_1}\n\n"
          "## Example 2\n"
          f"{example_template_2}\n\n"
          "Please build the graph according to the following Requirement and Sql. Please note that just output the final linear graph. Do not include any other superfluous descriptions.\n\n"
          "# Requirements:\n"
          f"{requirement_3}\n"
          "# Sql:\n"
          f"{sql_3}\n"
          "# Graph:\n")

print(prompt)
