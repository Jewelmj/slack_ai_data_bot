from app.llm.sql_generator import generate_sql

question = "show revenue by region for 2025-09-01"

sql = generate_sql(question)

print(sql)