"""Top level agent for data agent multi-agents.

-- it get data from database (e.g., BQ) using NL2SQL
-- then, it use NL2Py to do further data analysis as needed
"""

from google.adk.tools import ToolContext
from google.adk.tools.agent_tool import AgentTool

from .sub_agents.mongo_agent import root_agent as mongo_agent
from .sub_agents.postgres_agent import root_agent as postgres_agent


async def call_mongo_agent(
    question: str, 
    tool_context: ToolContext,
):
    """Tool to call mongo query agent."""

    agent_tool = AgentTool(agent=mongo_agent)

    db_agent_output = await agent_tool.run_async(
        args={"request": question}, tool_context=tool_context
    )
    tool_context.state["mongo_query_result"] = db_agent_output
    tool_context.state["mongo_agent_output"] = db_agent_output
    return db_agent_output


async def call_postgres_agent(
    question: str,
    tool_context: ToolContext,
):
    """Tool to call postgres query agent."""

    agent_tool = AgentTool(agent=postgres_agent)

    db_agent_output = await agent_tool.run_async(
        args={"request": question}, tool_context=tool_context
    )
    tool_context.state["postgres_query_result"] = db_agent_output
    tool_context.state["postgres_agent_output"] = db_agent_output
    return db_agent_output