import requests
from config import MODEL, ALLOWED_ACTIONS

OLLAMA_URL = "http://localhost:11434/api/chat"


def llm_decide(context, system_prompt):

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "messages": [
                {"role": "system", "content": system_prompt},
                {
                    "role": "user",
                    "content": f"""
Probe Failure Context:

{context}

Allowed actions:
{", ".join(ALLOWED_ACTIONS)}

Return ONLY one action.
"""
                }
            ],
            "stream": False
        }
    )

    result = response.json()
    decision = result["message"]["content"].strip()

    if decision not in ALLOWED_ACTIONS:
        return "ESCALATE_TO_HUMAN"

    return decision