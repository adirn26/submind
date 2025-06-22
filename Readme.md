# SubMind – Speak to Your Data, Anywhere

SubMind is a multi-agent system that allows users to query **any database** — MongoDB, PostgreSQL, and more — using **natural language**. Built using **Google’s Agent Development Kit (ADK)** and **Gemini Flash**, it abstracts away complex querying, schema knowledge, and DB-specific syntax.

Whether you're a business user, analyst, or developer — just ask your question, and SubMind handles the rest.

---

## 🚀 Features

- 🔗 Query multiple databases via natural language
- 🧠 Powered by schema-aware agents (MongoDB & Postgres)
- ⚡ Built with Google ADK + Gemini Flash
- 🧩 Modular agent architecture (easily extendable to BigQuery, GCS, etc.)
- 🛠️ No schema migration or data transformation required
- 🧪 Built-in support for filters, sorting, aggregations, and introspection

---

## 📸 Demo Preview

> "Show all UPI payments and related order info"

✅ Orchestrator Agent  
→ routes to Postgres Agent for `payments`  
→ routes to Mongo Agent for `orders`  
→ merges and summarizes

---

## 🧱 Architecture

```text
        +---------------------+
        |  Natural Language   |
        |     User Query      |
        +----------+----------+
                   |
                   v
        +---------------------+
        |   Orchestrator Agent|
        +----+----------+-----+
             |          |
     +-------+          +-------+
     |                          |
     v                          v
Mongo Agent            Postgres Agent
(introspects schema)   (introspects tables)
