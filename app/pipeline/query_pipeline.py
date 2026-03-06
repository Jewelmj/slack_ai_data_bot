from app.llm.sql_generator import generate_sql
from app.database.postgres import run_query


def run_data_query(question: str):
    sql = generate_sql(question)

    results = run_query(sql)

    formatted_results = format_results(results)

    return {
        "sql": sql,
        "results": formatted_results
    }

def format_results(results):
    """
    Convert database rows into a clean table-like string
    """
    output = "Region | Revenue\n"
    output += "-----------------\n"

    for region, revenue in results:
        output += f"{region} | {revenue}\n"

    return output
