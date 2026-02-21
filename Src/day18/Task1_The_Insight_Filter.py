import sqlite3
import pandas as pd

conn = sqlite3.connect(r"C:\AIml_intern\Src\day18\Task1_The_Insight_Filter.db")

query = """
SELECT 
    track,
    AVG(stipend) AS average_stipend,
    COUNT(*) AS total_interns
FROM interns
GROUP BY track
"""

df = pd.read_sql_query(query, conn)

print(df)

conn.close()