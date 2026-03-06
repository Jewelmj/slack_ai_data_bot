from fastapi import FastAPI, Form
from app.pipeline.query_pipeline import run_data_query

app = FastAPI()


@app.get("/")
def health_check():
    return {"status": "running"}


@app.post("/ask-data")
async def ask_data(text: str = Form(...)):
    """
    Endpoint that receives the Slack question.
    """

    try:
        response = run_data_query(text)

        return {
            "response_type": "in_channel",
            "text": f"""
SQL:
{response['sql']}

Results:
{response['results']}
"""
        }

    except Exception as e:
        return {
            "response_type": "ephemeral",
            "text": f"Error:\n{str(e)}"
        }