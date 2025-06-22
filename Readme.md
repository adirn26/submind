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

## 🧪 How to Run SubMind Locally

### 🛠️ Prerequisites

- Python 3.9+
- [Google ADK (Agent Development Kit)](https://github.com/google/agent-development-kit)
- Docker (for Postgres)
- MongoDB Atlas or a local MongoDB instance

```bash
git clone https://github.com/adirn26/submind.git
cd submind
pip install -r requirements.txt
adk web
```

## 📸 Demo Preview

> "Show all UPI payments and related order info"

✅ Orchestrator Agent  
→ routes to Postgres Agent for `payments`  
→ routes to Mongo Agent for `orders`  
→ merges and summarizes

![Screenshot from 2025-06-22 12-30-39](https://github.com/user-attachments/assets/a5a418b8-bce4-49a4-90c6-645c5d7e36d7)
![Screenshot from 2025-06-22 12-30-28](https://github.com/user-attachments/assets/1238d29f-afc9-4f34-94ee-f175d811e660)
![Screenshot from 2025-06-22 12-30-05](https://github.com/user-attachments/assets/6057235c-2816-41c3-bd7a-90f8f0eda9d0)
![Screenshot from 2025-06-22 12-24-51](https://github.com/user-attachments/assets/9deeb92a-8a3f-42f2-80fb-4c36e2fe83c2)

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
