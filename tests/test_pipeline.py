from apps.llm.sql_generator import generate_sql
from apps.database.postgres import run_query

question = "show revenue by region for 2025-09-01"

sql = generate_sql(question)

print("Generated SQL:")
print(sql)

results = run_query(sql)

print("\nQuery Results:")
print(results)