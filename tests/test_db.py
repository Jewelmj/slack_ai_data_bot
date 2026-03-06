from app.database.postgres import run_query

result = run_query("SELECT * FROM sales_daily;")

print(result)