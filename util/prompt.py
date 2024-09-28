requirement_1 = "find which tracks were composed by composer's name contain Smith."
sql_1 = """SELECT name,albumid,composer FROM tracks WHERE composer LIKE '%Smith%' ORDER BY albumid;"""
graph_1 = """{"id" : 1, "sql statement" : "SELECT name,albumid,composer FROM tracks;"},
{"id" : 2, "sql statement" : "SELECT name,albumid,composer FROM tracks WHERE composer LIKE '%Smith%';"},
{"id" : 3, "sql statement" : "SELECT name,albumid,composer FROM tracks WHERE composer LIKE '%Smith%' ORDER BY albumid;"}"""
example_template_1 = (f"# Requirement:\n{requirement_1}\n"
                      f"# Sql:\n{sql_1}\n"
                      f"# Graph:\n{graph_1}")

requirement_2 = ("The sqlite sql statement can be split into several executable atomic sql statements, and a directed "
                 "graph will be constructed to represent it. This graph should truly reflect the topological "
                 "execution of the atomic sql statement to achieve the requirements in the demand analysis.")
sql_2 = "update student set tot_cred = (select sum(credits) from takes natural join course where student.ID = takes.ID and takes.grade <> 'F' and takes.grade is not null);"
graph_2 = """{"id" : 1, "sql statement" : "select sum(credits) from takes;"},
{"id" : 2, "sql statement" : "select sum(credits) from takes natural join course;"},
{"id" : 3, "sql statement" : "select sum(credits) from takes natural join course where student.ID = takes.ID and takes.grade <> 'F' and takes.grade is not null;"}
{"id" : 4, "sql statement" : "update student set tot_cred = (select sum(credits) from takes natural join course where student.ID = takes.ID and takes.grade <> 'F' and takes.grade is not null);"}"""
example_template_2 = (f"# Requirement:\n{requirement_2}\n"
                      f"# Sql:\n{sql_2}\n"
                      f"# Graph:\n{graph_2}")

sql_3 = """SELECT T2.Street, T2.City, T2.Zip, T2.State FROM schools AS T2 INNER JOIN (SELECT cds, CAST(NumGE1500 AS REAL) / NumTstTakr AS rate FROM satscores WHERE NumGE1500 IS NOT NULL AND NumTstTakr IS NOT NULL AND NumTstTakr != 0) AS T1 ON T2.CDSCode = T1.cds WHERE T1.rate = (SELECT MIN(CAST(NumGE1500 AS REAL) / NumTstTakr) AS min_rate FROM satscores WHERE NumGE1500 IS NOT NULL AND NumTstTakr IS NOT NULL AND NumTstTakr != 0) ORDER BY T2.CDSCode"""
requirement_3 = "Execellence Rate = NumGE1500 / NumTstTakr; complete address has Street, City, Zip, State"

prompt = ("The goal is to construct a linear graph representation from a given sqlite statements(SQL). "
          "This graph should faithfully reflect the sequence of execution of the atomic SQL statements to achieve the requirements. "
          "The following includes two cases, including Requirement, Sql, and Graph.\n\n"
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
