from app.pipeline.query_pipeline import run_data_query

question = "show revenue by region for 2025-09-01"

response = run_data_query(question)

print("Generated SQL:")
print(response["sql"])

print("\nResults:")
print(response["results"])