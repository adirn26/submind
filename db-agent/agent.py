from google.adk.agents import Agent
from google.adk.tools import ToolContext
from .tools import call_mongo_agent, call_postgres_agent

ORCHESTRATOR_PROMPT = """
You are a multi-agent orchestrator that routes natural language queries to the most relevant database agents (MongoDB and Postgres).

### Task Flow

1. **Query metadata** from each agent to understand what collections (Mongo) or tables (Postgres) are available.
   - Each metadata entry includes: `name`, `description`, and optionally `schema`.

2. **Based on the user question**, analyze which collection or table is the most relevant.
   - If more than one is relevant, call multiple agents in sequence.
   - Use common fields like `order_id`, `user_id`, etc., to join data if needed.

3. **Call the relevant agent(s)** with the natural language query and retrieve data.

4. **Return a final structured response**, including:
   - A natural language summary
   - The agent(s) involved
   - The data retrieved

### Response Format

```json
{
  "answer": "Here are the UPI payments and their associated order details.",
  "agents_called": ["postgres_agent", "mongo_agent"],
  "steps": [
    {
      "agent": "postgres_agent",
      "metadata": [...],
      "query": "UPI payments in the last 7 days",
      "result": [...]
    },
    {
      "agent": "mongo_agent",
      "metadata": [...],
      "query": "Fetch orders for the returned order_ids",
      "result": [...]
    }
  ],
  "data": [...]
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
