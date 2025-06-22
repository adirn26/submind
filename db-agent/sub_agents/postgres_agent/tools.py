import os
import psycopg2
from google.adk.tools import ToolContext
from psycopg2.extras import RealDictCursor
from decimal import Decimal
from datetime import date, datetime

def json_safe(obj):
    if isinstance(obj, Decimal):
        return float(obj)
    elif isinstance(obj, (date, datetime)):
        return obj.isoformat()
    elif isinstance(obj, dict):
        return {k: json_safe(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [json_safe(i) for i in obj]
    else:
        return obj



def get_postgres_connection():
    return psycopg2.connect(
        dbname=os.getenv("PG_DBNAME"),
        user=os.getenv("PG_USER"),
        password=os.getenv("PG_PASSWORD"),
        host=os.getenv("PG_HOST"),
        port=os.getenv("PG_PORT"),
    )


async def call_pg_query(sql: str, tool_context: ToolContext):
    """Tool to execute a raw SQL SELECT query."""
    conn = get_postgres_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute(sql)
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return json_safe(rows)



async def call_pg_schema_info(tool_context: ToolContext):
    """Tool to fetch schema info from Postgres."""
    conn = get_postgres_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT table_name, column_name, data_type
        FROM information_schema.columns
        WHERE table_schema = 'public'
        ORDER BY table_name, ordinal_position
    """)
    result = cur.fetchall()
    cur.close()
    conn.close()
    return result
