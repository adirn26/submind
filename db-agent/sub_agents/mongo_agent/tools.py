import os
from typing import List
from .atlas_client import AtlasClient
from google.adk.tools import ToolContext
from bson import ObjectId
from google import genai
from google.genai.types import EmbedContentConfig



def convert_objectid(obj):
    if isinstance(obj, ObjectId):
        return str(obj)
    elif isinstance(obj, dict):
        return {k: convert_objectid(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [convert_objectid(i) for i in obj]
    else:
        return obj


async def call_db_find(
    collection_name: str,
    filter: dict,
    limit: int,
    tool_context: ToolContext,
):
    """Tool to find documents in a collection.
    
    Args:
        collection_name: str, the name of the collection to query
        filter: dict, the filter to apply to the query
        limit: int, the maximum number of documents to return
        tool_context: dict, the context of the tool
    Returns:
        list, a list of documents
    """
    atlas_uri = os.getenv("ATLAS_URI")
    dbname = os.getenv("ATLAS_DBNAME")
    client = AtlasClient(atlas_uri, dbname)
    items = client.find(collection_name, filter, limit)
    return [convert_objectid(doc) for doc in items]


async def call_db_list_collections(
    tool_context: ToolContext,
):
    """Tool to list collections in a database."""
    atlas_uri = os.getenv("ATLAS_URI")
    dbname = os.getenv("ATLAS_DBNAME")
    client = AtlasClient(atlas_uri, dbname)
    return client.list_collections()


async def call_db_aggregate(
    collection_name: str,
    pipeline: List[dict],
    tool_context: ToolContext,
):
    """Tool to run an aggregate pipeline on a collection.
    
    Args:
        collection_name: str, the name of the collection to query
        pipeline: list, the aggregate pipeline to run
        tool_context: dict, the context of the tool
    Returns:
        list, a list of documents
    """
    atlas_uri = os.getenv("ATLAS_URI")
    dbname = os.getenv("ATLAS_DBNAME")
    client = AtlasClient(atlas_uri, dbname)
    result = client.run_aggregate_pipeline(collection_name, pipeline)
    return convert_objectid(result)

async def call_db_get_info_collection(tool_context: ToolContext):
    """Tool to get metadata from the 'info_collection' collection."""
    atlas_uri = os.getenv("ATLAS_URI")
    dbname = os.getenv("ATLAS_DBNAME")
    client = AtlasClient(atlas_uri, dbname)
    info_docs = client.find("info_collection", filter={}, limit=100)
    return [convert_objectid(doc) for doc in info_docs]


async def call_db_find_advanced(
    collection_name: str,
    filter: dict,
    limit: int,
    projection: dict = None,
    sort: list = None,
    tool_context: ToolContext = None,
):
    """Tool to find documents with projection and sort."""
    atlas_uri = os.getenv("ATLAS_URI")
    dbname = os.getenv("ATLAS_DBNAME")
    client = AtlasClient(atlas_uri, dbname)
    items = client.find(
        collection=collection_name,
        filter=filter,
        limit=limit,
        projection=projection,
        sort=sort,
    )
    return [convert_objectid(doc) for doc in items]


async def call_db_get_collection_schema(collection_name: str, tool_context: ToolContext):
    """Get schema info of a specific collection from 'info_collection'."""
    atlas_uri = os.getenv("ATLAS_URI")
    dbname = os.getenv("ATLAS_DBNAME")
    client = AtlasClient(atlas_uri, dbname)
    results = client.find("info_collection", {"name": collection_name}, limit=1)
    return convert_objectid(results[0]) if results else None