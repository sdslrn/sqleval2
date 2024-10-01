# # requirement_1 = "Retrieve the name, album ID, and composer for all tracks where the composer's name includes 'Smith' sorted by the album ID."
# # sql_1 = """SELECT name,albumid,composer FROM tracks WHERE composer LIKE '%Smith%' ORDER BY albumid;"""
# # graph_1 = """
# #     "nodes": [
# #         {"id" : 1, "sql statement" : "SELECT name,albumid,composer FROM tracks;", "requirement":"Retrieve the name, album ID, and composer for all tracks in the database."},
# #         {"id" : 2, "sql statement" : "SELECT name,albumid,composer FROM tracks WHERE composer LIKE '%Smith%';", "requirement":"Retrieve the name, album ID, and composer for all tracks where the composer's name includes the substring 'Smith'."},
# #         {"id" : 3, "sql statement" : "SELECT name,albumid,composer FROM tracks WHERE composer LIKE '%Smith%' ORDER BY albumid;", "requirement":"Retrieve the name, album ID, and composer for all tracks where the composer's name includes 'Smith' sorted by the album ID."}
# #     ],
# #     "edges": [
# #         {"source": 1, "target": 2},
# #         {"source": 2, "target": 3}
# #     ]
# # """
# # example_template_1 = (f"# Requirement:\n{requirement_1}\n"
# #                       f"# Sql:\n{sql_1}\n"
# #                       f"# Graph:\n{graph_1}")
#
# requirement_2 = ("Update the 'tot_cred' attribute for each student to reflect the total sum of credits "
#                  "for courses they have successfully completed, where a successful completion is defined "
#                  "as receiving a grade other than 'F' and not null. This calculation uses a natural join between "
#                  "the 'takes' and 'course' tables, ensuring that the student IDs match between them. "
#                  "Use the SQL UPDATE and SET commands to apply this change.")
# sql_2 = "update student set tot_cred = (select sum(credits) from takes natural join course where student.ID = takes.ID and takes.grade <> 'F' and takes.grade is not null);"
# graph_2 = """
#     "nodes": [
#         {"id" : 1, "sql statement" : "select sum(credits) from takes;", "requirement":"Calculate the total sum of credits from the 'takes' table."},
#         {"id" : 2, "sql statement" : "select sum(credits) from takes natural join course;", "requirement":"Calculate the total sum of credits by joining the 'takes' table and the 'course' table using a natural join."},
#         {"id" : 3, "sql statement" : "select sum(credits) from takes natural join course where student.ID = takes.ID and takes.grade <> 'F' and takes.grade is not null;", "requirement":"Calculate the total sum of credits from courses where the student's grade is neither 'F' nor null, implying successful course completion. This involves a natural join between the 'takes' and 'course' tables and requires matching student IDs in both tables."},
#         {"id" : 4, "sql statement" : "update student set tot_cred = (select sum(credits) from takes natural join course where student.ID = takes.ID and takes.grade <> 'F' and takes.grade is not null);", "requirement":"Update the 'tot_cred' attribute for each student to reflect the total sum of credits for courses they have successfully completed, where a successful completion is defined as receiving a grade other than 'F' and not null. This calculation uses a natural join between the 'takes' and 'course' tables, ensuring that the student IDs match between them. Use the SQL UPDATE and SET commands to apply this change."}
#     ],
#     "edges": [
#         {"source": 1, "target": 2},
#         {"source": 2, "target": 3},
#         {"source": 3, "target": 4}
#     ]
# """
# example_template_2 = (f"# Requirement:\n{requirement_2}\n"
#                       f"# Sql:\n{sql_2}\n"
#                       f"# Graph:\n{graph_2}")
#
# requirement_3 = ("What is the complete address of the school with the lowest excellence rate? Indicate the Street, City,"
#                  " Zip and State.xecellence Rate = NumGE1500 / NumTstTakr; complete address has Street, City, Zip, State")
# sql_3 = "SELECT T2.Street, T2.City, T2.Zip, T2.State FROM schools AS T2 INNER JOIN (SELECT cds, CAST(NumGE1500 AS REAL) / NumTstTakr AS rate FROM satscores WHERE NumGE1500 IS NOT NULL AND NumTstTakr IS NOT NULL AND NumTstTakr != 0) AS T1 ON T2.CDSCode = T1.cds WHERE T1.rate = (SELECT MIN(CAST(NumGE1500 AS REAL) / NumTstTakr) AS min_rate FROM satscores WHERE NumGE1500 IS NOT NULL AND NumTstTakr IS NOT NULL AND NumTstTakr != 0) ORDER BY T2.CDSCode;"
# graph_3 = """
#     "nodes": [
#         {"id" : 1, "sql statement" : "SELECT cds, CAST(NumGE1500 AS REAL) / NumTstTakr AS rate FROM satscores WHERE NumGE1500 IS NOT NULL AND NumTstTakr IS NOT NULL AND NumTstTakr != 0;", "requirement":"What is the excellence rate (NumGE1500 / NumTstTakr) for each school where NumGE1500 and NumTstTakr are not null and NumTstTakr is not zero?"},
#         {"id" : 2, "sql statement" : "SELECT MIN(CAST(NumGE1500 AS REAL) / NumTstTakr) AS min_rate FROM satscores WHERE NumGE1500 IS NOT NULL AND NumTstTakr IS NOT NULL AND NumTstTakr != 0;", "requirement":"What is the minimum excellence rate (NumGE1500 / NumTstTakr) among schools where NumGE1500 and NumTstTakr are not null and NumTstTakr is not zero?"},
#         {"id" : 3, "sql statement" : "SELECT T2.Street, T2.City, T2.Zip, T2.State FROM schools AS T2 INNER JOIN (SELECT cds, CAST(NumGE1500 AS REAL) / NumTstTakr AS rate FROM satscores WHERE NumGE1500 IS NOT NULL AND NumTstTakr IS NOT NULL AND NumTstTakr != 0) AS T1 ON T2.CDSCode = T1.cds WHERE T1.rate = (SELECT MIN(CAST(NumGE1500 AS REAL) / NumTstTakr) AS min_rate FROM satscores WHERE NumGE1500 IS NOT NULL AND NumTstTakr IS NOT NULL AND NumTstTakr != 0) ORDER BY T2.CDSCode;", "requirement":"What is the complete address of the school with the lowest excellence rate? Indicate the Street, City, Zip and State.xecellence Rate = NumGE1500 / NumTstTakr; complete address has Street, City, Zip, State."}
#     ],
#     "edges": [
#         {"source": 1, "target": 3},
#         {"source": 2, "target": 3}
#     ]
# """
# example_template_3 = (f"# Requirement:\n{requirement_3}\n"
#                       f"# Sql:\n{sql_3}\n"
#                       f"# Graph:\n{graph_3}")
#
# #sql_4 = "update student set tot_cred = (select case when sum(credits) is not null then sum(credits) else 0 end from takes natural join course where student.ID = takes.ID and takes.grade <> 'F' and takes.grade is not null);"
# # sql_4 = """SELECT County FROM (SELECT County, COUNT(School) AS SchoolCount FROM schools WHERE strftime('%Y', ClosedDate) BETWEEN '1980' AND '1989' AND StatusType = 'Closed' AND SOC = 11 GROUP BY County) WHERE SchoolCount = (SELECT MAX(SchoolCount) FROM (SELECT COUNT(School) AS SchoolCount FROM schools WHERE strftime('%Y', ClosedDate) BETWEEN '1980' AND '1989' AND StatusType = 'Closed' AND SOC = 11 GROUP BY County));"""
# sql_4 = """ SELECT T3.account_id FROM client AS T1 INNER JOIN district AS T2 ON T1.district_id = T2.district_id INNER JOIN account AS T3 ON T2.district_id = T3.district_id WHERE T1.gender = 'F' AND T1.birth_date = (SELECT MIN(birth_date) FROM client WHERE gender = 'F') AND T2.A11 = (SELECT MIN(T2.A11) FROM client AS T1 INNER JOIN district AS T2 ON T1.district_id = T2.district_id WHERE T1.gender = 'F' AND T1.birth_date = (SELECT MIN(birth_date) FROM client WHERE gender = 'F')); """
# # requirement_4 = "If a student has not successfully completed any course, the above update operation will make its tot_cred attribute value null. I want to set the tot_cred attribute value of these students to 0."
# # requirement_4 = "Which county reported the most number of school closure in the 1980s with school wonership code belonging to Youth Authority Facilities (CEA)? Youth Authority Facilities (CEA) refers to SOC = 11; 1980s = years between 1980 and 1989."
# requirement_4 = "Name the account numbers of female clients who are oldest and have lowest average salary? Female refers to 'F' in the gender; A11 contains information about average salary."
# prompt = (
# "The goal is to build a directed graph representation from the given sqlite SQL statements and requirement text to represent the gradual advancement of functional implementation and eventually complete all requirements."
# "Each node in the graph represents a SQL statement, which is a subsequence of the given SQL statement, and the edge represents the execution order. The subsequent nodes are the progression of the previous node, and the last node should be the original given SQL statement."
# "At the same time, the SQL statement corresponding to each node should generate the corresponding requirement text, where the requirement text of the last node is the original requirement."
# "This graph should faithfully reflect the topological execution order of the SQL statement to achieve the requirements."
# "The following includes 2 cases: requirements, Sql and Graph.\n\n"
#           # "## Example 1\n"
#           # f"{example_template_1}\n\n"
#           "## Example 1\n"
#           f"{example_template_2}\n\n"
#           "## Example 2\n"
#           f"{example_template_3}\n\n"
#           "Please build the graph according to the following Requirement and Sql. Please note that just output the final linear graph. Do not include any other superfluous descriptions.\n\n"
#           "# Requirements:\n"
#           f"{requirement_4}\n"
#           "# Sql:\n"
#           f"{sql_4}\n"
#           "# Graph:\n")
#
# print(prompt)
# requirement_1 = "Retrieve the name, album ID, and composer for all tracks where the composer's name includes 'Smith' sorted by the album ID."
# sql_1 = """SELECT name,albumid,composer FROM tracks WHERE composer LIKE '%Smith%' ORDER BY albumid;"""

requirement_1 = "Name the account numbers of female clients who are oldest and have lowest average salary."
sql_1 = "SELECT T3.account_id FROM client AS T1 INNER JOIN district AS T2 ON T1.district_id = T2.district_id INNER JOIN account AS T3 ON T2.district_id = T3.district_id WHERE T1.gender = 'F' AND T1.birth_date = (SELECT MIN(birth_date) FROM client WHERE gender = 'F') AND T2.A11 = (SELECT MIN(T2.A11) FROM client AS T1 INNER JOIN district AS T2 ON T1.district_id = T2.district_id WHERE T1.gender = 'F' AND T1.birth_date = (SELECT MIN(birth_date) FROM client WHERE gender = 'F'));"

graph_1 = """
    "nodes": [
        {"id": 1, "sql statement": "SELECT MIN(birth_date) FROM client WHERE gender = 'F';", "requirement": "Identify the oldest female clients."},
        {"id": 2, "sql statement": "SELECT MIN(T2.A11) FROM client AS T1 INNER JOIN district AS T2 ON T1.district_id = T2.district_id WHERE T1.gender = 'F' AND T1.birth_date = (SELECT MIN(birth_date) FROM client WHERE gender = 'F');", "requirement": "Find the lowest average salary among the oldest female clients."},
        {"id": 3, "sql statement": "SELECT T3.account_id FROM client AS T1 INNER JOIN district AS T2 ON T1.district_id = T2.district_id INNER JOIN account AS T3 ON T2.district_id = T3.district_id WHERE T1.gender = 'F' AND T1.birth_date = (SELECT MIN(birth_date) FROM client WHERE gender = 'F') AND T2.A11 = (SELECT MIN(T2.A11) FROM client AS T1 INNER JOIN district AS T2 ON T1.district_id = T2.district_id WHERE T1.gender = 'F' AND T1.birth_date = (SELECT MIN(birth_date) FROM client WHERE gender = 'F'));", "requirement": "Name the account numbers of female clients who are oldest and have lowest average salary."}
    ],
    "edges": [
        {"source": 1, "target": 2},
        {"source": 2, "target": 3},
        {"source": 1, "target": 3}
    ]
"""
example_template_1 = (f"# Requirement:\n{requirement_1}\n"
                       f"# Sql:\n{sql_1}\n"
                       f"# Graph:\n{graph_1}")

requirement_2 = ("Update the 'tot_cred' attribute for each student to reflect the total sum of credits "
                 "for courses they have successfully completed, where a successful completion is defined "
                 "as receiving a grade other than 'F' and not null. This calculation uses a natural join between "
                 "the 'takes' and 'course' tables, ensuring that the student IDs match between them. "
                 "Use the SQL UPDATE and SET commands to apply this change.")
sql_2 = "update student set tot_cred = (select sum(credits) from takes natural join course where student.ID = takes.ID and takes.grade <> 'F' and takes.grade is not null);"
graph_2 = """
    "nodes": [
        {"id" : 1, "sql statement" : "select sum(credits) from takes;", "requirement":"Calculate the total sum of credits from the 'takes' table."},
        {"id" : 2, "sql statement" : "select sum(credits) from takes natural join course;", "requirement":"Calculate the total sum of credits by joining the 'takes' table and the 'course' table using a natural join."},
        {"id" : 3, "sql statement" : "select sum(credits) from takes natural join course where student.ID = takes.ID and takes.grade <> 'F' and takes.grade is not null;", "requirement":"Calculate the total sum of credits from courses where the student's grade is neither 'F' nor null, implying successful course completion. This involves a natural join between the 'takes' and 'course' tables and requires matching student IDs in both tables."},
        {"id" : 4, "sql statement" : "update student set tot_cred = (select sum(credits) from takes natural join course where student.ID = takes.ID and takes.grade <> 'F' and takes.grade is not null);", "requirement":"Update the 'tot_cred' attribute for each student to reflect the total sum of credits for courses they have successfully completed, where a successful completion is defined as receiving a grade other than 'F' and not null. This calculation uses a natural join between the 'takes' and 'course' tables, ensuring that the student IDs match between them. Use the SQL UPDATE and SET commands to apply this change."}
    ],
    "edges": [
        {"source": 1, "target": 2},
        {"source": 2, "target": 3},
        {"source": 3, "target": 4}
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
        {"id" : 1, "sql statement" : "SELECT cds, CAST(NumGE1500 AS REAL) / NumTstTakr AS rate FROM satscores WHERE NumGE1500 IS NOT NULL AND NumTstTakr IS NOT NULL AND NumTstTakr != 0;", "requirement":"What is the excellence rate (NumGE1500 / NumTstTakr) for each school where NumGE1500 and NumTstTakr are not null and NumTstTakr is not zero?"},
        {"id" : 2, "sql statement" : "SELECT MIN(CAST(NumGE1500 AS REAL) / NumTstTakr) AS min_rate FROM satscores WHERE NumGE1500 IS NOT NULL AND NumTstTakr IS NOT NULL AND NumTstTakr != 0;", "requirement":"What is the minimum excellence rate (NumGE1500 / NumTstTakr) among schools where NumGE1500 and NumTstTakr are not null and NumTstTakr is not zero?"},
        {"id" : 3, "sql statement" : "SELECT T2.Street, T2.City, T2.Zip, T2.State FROM schools AS T2 INNER JOIN (SELECT cds, CAST(NumGE1500 AS REAL) / NumTstTakr AS rate FROM satscores WHERE NumGE1500 IS NOT NULL AND NumTstTakr IS NOT NULL AND NumTstTakr != 0) AS T1 ON T2.CDSCode = T1.cds WHERE T1.rate = (SELECT MIN(CAST(NumGE1500 AS REAL) / NumTstTakr) AS min_rate FROM satscores WHERE NumGE1500 IS NOT NULL AND NumTstTakr IS NOT NULL AND NumTstTakr != 0) ORDER BY T2.CDSCode;", "requirement":"What is the complete address of the school with the lowest excellence rate? Indicate the Street, City, Zip and State.xecellence Rate = NumGE1500 / NumTstTakr; complete address has Street, City, Zip, State."}
    ],
    "edges": [
        {"source": 1, "target": 3},
        {"source": 2, "target": 3}
    ]
"""
example_template_3 = (f"# Requirement:\n{requirement_3}\n"
                      f"# Sql:\n{sql_3}\n"
                      f"# Graph:\n{graph_3}")

sql_4 = "SELECT T2.name FROM foreign_data AS T1 INNER JOIN cards AS T2 ON T2.uuid = T1.uuid INNER JOIN sets AS T3 ON T3.code = T2.setCode WHERE T3.name = 'Coldsnap' AND T1.language = 'Italian' AND T2.convertedManaCost = (SELECT MAX(convertedManaCost) FROM foreign_data AS T1 INNER JOIN cards AS T2 ON T2.uuid = T1.uuid INNER JOIN sets AS T3 ON T3.code = T2.setCode WHERE T3.name = 'Coldsnap' AND T1.language = 'Italian');"
requirement_4 = "Please list the Italian names of the cards in the set Coldsnap with the highest converted mana cost. card set Coldsnap refers to name = 'Coldsnap'; Italian refers to language = 'Italian'"
#sql_4 = "update student set tot_cred = (select case when sum(credits) is not null then sum(credits) else 0 end from takes natural join course where student.ID = takes.ID and takes.grade <> 'F' and takes.grade is not null);"
# sql_4 = """SELECT County FROM (SELECT County, COUNT(School) AS SchoolCount FROM schools WHERE strftime('%Y', ClosedDate) BETWEEN '1980' AND '1989' AND StatusType = 'Closed' AND SOC = 11 GROUP BY County) WHERE SchoolCount = (SELECT MAX(SchoolCount) FROM (SELECT COUNT(School) AS SchoolCount FROM schools WHERE strftime('%Y', ClosedDate) BETWEEN '1980' AND '1989' AND StatusType = 'Closed' AND SOC = 11 GROUP BY County));"""
# sql_4 = """ SELECT T1.label FROM molecule AS T1 INNER JOIN (SELECT T.molecule_id, COUNT(T.bond_type) AS bond_count FROM bond AS T WHERE T.bond_type = '=' GROUP BY T.molecule_id HAVING bond_count = (SELECT MAX(bond_count) FROM (SELECT molecule_id, COUNT(bond_type) AS bond_count FROM bond WHERE bond_type = '=' GROUP BY molecule_id) AS subquery) ORDER BY bond_count DESC) AS T2 ON T1.molecule_id = T2.molecule_id; """
# requirement_4 = "If a student has not successfully completed any course, the above update operation will make its tot_cred attribute value null. I want to set the tot_cred attribute value of these students to 0."
# requirement_4 = "Which county reported the most number of school closure in the 1980s with school wonership code belonging to Youth Authority Facilities (CEA)? Youth Authority Facilities (CEA) refers to SOC = 11; 1980s = years between 1980 and 1989."
# requirement_4 = " Is the molecule with the most double bonds carcinogenic? double bond refers to bond_type = ' = '; label = '+' mean molecules are carcinogenic. "
prompt = (
"The goal is to build a directed graph representation from the given sqlite SQL statements and requirement text to represent the gradual advancement of functional implementation and eventually complete all requirements."
"Each node in the graph represents a SQL statement, which is a subsequence of the given SQL statement, and the edge represents the execution order. The subsequent nodes are the progression of the previous node, and the last node should be the original given SQL statement."
"At the same time, the SQL statement corresponding to each node should generate the corresponding requirement text, where the requirement text of the last node is the original requirement."
"This graph should faithfully reflect the topological execution order of the SQL statement to achieve the requirements."
"The following includes 3 cases: requirements, Sql and Graph.\n\n"
          "## Example 1\n"
          f"{example_template_1}\n\n"
          "## Example 2\n"
          f"{example_template_2}\n\n"
          "## Example 3\n"
          f"{example_template_3}\n\n"
          "Please build the graph according to the following Requirement and Sql. Please note that just output the final linear graph. Do not include any other superfluous descriptions.\n\n"
          "# Requirements:\n"
          f"{requirement_4}\n"
          "# Sql:\n"
          f"{sql_4}\n"
          "# Graph:\n")

print(prompt)
