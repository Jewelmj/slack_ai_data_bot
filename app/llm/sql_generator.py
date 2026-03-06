from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatOpenAI(
    model="openai/gpt-4o-mini",
    temperature=0,
    base_url=os.getenv("OPENAI_BASE_URL"),
    api_key=os.getenv("OPENAI_API_KEY")
)

PROMPT = """
You are a PostgreSQL expert.

Database table:
sales_daily

Columns:
date
region
category
revenue
orders

Return ONLY a SQL SELECT query.

Question:
"""


def generate_sql(question: str):

    response = llm.invoke(PROMPT + question)

    sql = response.content.strip()

    # remove markdown if present
    sql = sql.replace("```sql", "").replace("```", "").strip()

    return sql