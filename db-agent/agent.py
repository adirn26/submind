from google.adk.agents import Agent
from google.adk.tools import ToolContext
from .tools import call_mongo_agent, call_postgres_agent

ORCHESTRATOR_PROMPT = """
You are an orchestrator agent. Your task is to collect and unify answers from multiple database agents (MongoDB and Postgres).
For every user query:
1. Forward the query to all sub-agents using the tools available.
2. Wait for their responses.
3. Merge the results and summarize the final answer clearly.

Return this JSON:
{
  "summary": "<combined human-readable answer>",
  "mongo_result": {...},
  "postgres_result": {...}
}
"""

root_agent = Agent(
    name="orchestrator_agent",
    model="gemini-2.5-flash",
    instruction=ORCHESTRATOR_PROMPT,
    description="Orchestrates queries across Mongo and Postgres agents.",
    tools=[
        call_postgres_agent, 
        call_mongo_agent
    ]
)
