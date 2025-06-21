from google.adk.agents import Agent
from .tools import call_pg_query, call_pg_schema_info

POSTGRES_AGENT_PROMPT = """
You are a Postgres SQL query agent. Your task is to interpret natural language questions and translate them into valid SQL queries using schema information.

Steps:
1. Use the `call_pg_schema_info` tool to understand available tables and fields.
2. Based on the user query, determine which table(s) are relevant.
3. Construct a SELECT SQL query to retrieve the data.
4. Execute the query using `call_pg_query`.

Return the following:
- "answer": a human-readable summary of the result
- "query_used": the SQL query used
- "data": the top rows of the result
"""

postgres_agent = Agent(
    name="postgres_agent",
    model="gemini-2.0-flash",
    description="Agent to query Postgres DB",
    instruction=POSTGRES_AGENT_PROMPT,
    tools=[
        call_pg_query,
        call_pg_schema_info
    ]
)
