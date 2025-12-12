# app/llm/llm_client.py
import os
import httpx
from typing import List, Dict, Any

from dotenv import load_dotenv
load_dotenv()

LLM_API_KEY = os.getenv("LLM_API_KEY")
LLM_API_BASE = os.getenv("LLM_API_BASE", "https://foundation-models.api.cloud.ru/v1")
LLM_MODEL = os.getenv("LLM_MODEL", "openai/gpt-oss-120b")


class CloudLLMClient:
    """
    Минимальный клиент для Cloud.ru LLM
    """

    def __init__(self):
        if not LLM_API_KEY:
            raise ValueError("LLM_API_KEY is not set")

        self.headers = {
            "Authorization": f"Bearer {LLM_API_KEY}",
            "Content-Type": "application/json"
        }

    async def chat(self, messages: List[Dict[str, str]]) -> str:
        payload = {
            "model": LLM_MODEL,
            "messages": messages,
            "temperature": 0.2,
        }

        async with httpx.AsyncClient() as client:
            resp = await client.post(
                f"{LLM_API_BASE}/chat/completions",
                json=payload,
                headers=self.headers,
                timeout=60
            )
            resp.raise_for_status()
            data = resp.json()
            return data["choices"][0]["message"]["content"]
