## Project Structure

```
customer_support/
├── llm.py
├── notebooks/
│   └── experiments.ipynb
├── data/
│   └── research.md
└── .env
```

---

## What I Built

A minimal Agentic AI system using LangGraph with one node that talks to Google Gemini.

---

## LLM Used

- **Model:** gemini-2.5-flash-lite  
- **Provider:** Google  
- **Why:** Cheapest and fastest Gemini model

---

## How it Works

1. User sends a question
2. LangGraph passes it to `ask_llm` node
3. Node calls Gemini LLM
4. Response is returned

---

## Result

**Q:** What is the capital of France?  
**A:** The capital of France is **Paris**.

---

## Key Learnings

- `get_llm()` makes switching models easy
- `MessagesState` handles chat history automatically
- Never push `.env` to GitHub