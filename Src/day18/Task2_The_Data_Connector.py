import sqlite3
import pandas as pd

conn = sqlite3.connect(r"C:\AIml_intern\Src\day18\Task2_The_Data_Connector.db")
query = """
SELECT 
i.intern_name,
i.track,
m.mentor_name
FROM interns i
INNER JOIN mentors m
ON i.track = m.track
"""
df = pd.read_sql_query(query, conn)

print("Joined Data :")
print(df)

conn.close()