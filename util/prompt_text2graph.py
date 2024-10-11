
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

example_template_1 = (f"# Sql:\n{sql_1}\n"
                      f"# Graph:\n{graph_1}")

sql_2 = "update student set tot_cred = (select sum(credits) from takes natural join course where student.ID = takes.ID and takes.grade <> 'F' and takes.grade is not null);"
graph_2 = """
{
    "nodes": [
        {"id" : 1, "sql statement" : "select sum(credits) from takes;"},
        {"id" : 2, "sql statement" : "select sum(credits) from takes natural join course;"},
        {"id" : 3, "sql statement" : "select sum(credits) from takes natural join course where student.ID = takes.ID and takes.grade <> 'F' and takes.grade is not null;"},
        {"id" : 4, "sql statement" : "update student set tot_cred = (select sum(credits) from takes natural join course where student.ID = takes.ID and takes.grade <> 'F' and takes.grade is not null);"}
    ],
    "edges": [
        {"source": 1, "target": 2},
        {"source": 2, "target": 3},
        {"source": 3, "target": 4}
    ]
}
"""
example_template_2 = (f"# Sql:\n{sql_2}\n"
                      f"# Graph:\n{graph_2}")

sql_3 = "SELECT T2.Street, T2.City, T2.Zip, T2.State FROM schools AS T2 INNER JOIN (SELECT cds, CAST(NumGE1500 AS REAL) / NumTstTakr AS rate FROM satscores WHERE NumGE1500 IS NOT NULL AND NumTstTakr IS NOT NULL AND NumTstTakr != 0) AS T1 ON T2.CDSCode = T1.cds WHERE T1.rate = (SELECT MIN(CAST(NumGE1500 AS REAL) / NumTstTakr) AS min_rate FROM satscores WHERE NumGE1500 IS NOT NULL AND NumTstTakr IS NOT NULL AND NumTstTakr != 0) ORDER BY T2.CDSCode;"
graph_3 = """
{
    "nodes": [
        {"id" : 1, "sql statement" : "SELECT cds, CAST(NumGE1500 AS REAL) / NumTstTakr AS rate FROM satscores WHERE NumGE1500 IS NOT NULL AND NumTstTakr IS NOT NULL AND NumTstTakr != 0;"},
        {"id" : 2, "sql statement" : "SELECT MIN(CAST(NumGE1500 AS REAL) / NumTstTakr) AS min_rate FROM satscores WHERE NumGE1500 IS NOT NULL AND NumTstTakr IS NOT NULL AND NumTstTakr != 0;"},
        {"id" : 3, "sql statement" : "SELECT T2.Street, T2.City, T2.Zip, T2.State FROM schools AS T2 INNER JOIN (SELECT cds, CAST(NumGE1500 AS REAL) / NumTstTakr AS rate FROM satscores WHERE NumGE1500 IS NOT NULL AND NumTstTakr IS NOT NULL AND NumTstTakr != 0) AS T1 ON T2.CDSCode = T1.cds WHERE T1.rate = (SELECT MIN(CAST(NumGE1500 AS REAL) / NumTstTakr) AS min_rate FROM satscores WHERE NumGE1500 IS NOT NULL AND NumTstTakr IS NOT NULL AND NumTstTakr != 0) ORDER BY T2.CDSCode;"}
        ],
    "edges": [
        {"source": 1, "target": 3},
        {"source": 2, "target": 3}
    ]
}
"""
example_template_3 = (f"# Sql:\n{sql_3}\n"
                      f"# Graph:\n{graph_3}")


def get_prompt(sql_4):
    prompt = (
        "The goal is to construct a directed graph representation from a given sqlite SQL statement to represent the gradual advancement of functional implementation and eventually complete all requirements."
        "Each node in the graph represents a SQL statement, which is a subsequence of a given SQL statement, and the edge represents the execution order. "
        "Subsequent nodes are the progression of the previous node. ( please attention the last node should be the original given SQL statement. )"
        "This graph should faithfully reflect the topological execution order of SQL statements to achieve requirements. "
        "The following includes three cases, including Sql, and Graph.\n\n"

        "## Example 1\n"
        f"{example_template_1}\n\n"
        "## Example 2\n"
        f"{example_template_2}\n\n"
        "## Example 3\n"
        f"{example_template_3}\n\n"
        "Please build the graph according to the following Sql. Please note that just output the final graph. Do not include any other superfluous descriptions.\n\n"
        "# Sql:\n"
        f"{sql_4}\n"
        "# Graph:\n")

    return prompt


sql = """
DELETE FROM customers
WHERE PostalCode LIKE '%[A-Za-z]%'
   OR Company IS NULL;
"""
print(get_prompt(sql))