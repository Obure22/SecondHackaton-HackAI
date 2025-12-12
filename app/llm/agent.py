# app/llm/agent.py
import json
from typing import Dict, Any

from app.llm.llm_client import CloudLLMClient
from app.server import mcp


class LLMAgent:
    def __init__(self):
        self.llm = CloudLLMClient()

    async def _detect_tool(self, query: str) -> Dict[str, Any]:
        """LLM выбирает, какой инструмент использовать."""

        system_prompt = """
Ты — маршрутизатор инструментов MCP.

Доступные инструменты:
1) search_vacancies(text, area, per_page, page)
2) search_vacancies_advanced(text, area, per_page, page, salary_from, salary_to, experience, employment, schedule)
3) get_vacancy_details(vacancy_id)

Верни STRICT JSON:
{
    "tool": "название",
    "args": {...}
}
Если инструмент не нужен:
{ "tool": null }
"""

        answer = await self.llm.chat([
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": query}
        ])

        try:
            return json.loads(answer)
        except Exception:
            return {"tool": None}

    async def _run_tool_via_mcp(self, tool: str, args: dict):
        """Вызываем инструмент через MCP."""
        try:
            result = await mcp.call_tool(tool, args)
            return result
        except Exception as e:
            return {"error": str(e)}

    async def ask(self, query: str) -> str:
        """Главный метод агента"""

        # 1. LLM выбирает инструмент
        tool_info = await self._detect_tool(query)

        tool_name = tool_info.get("tool")
        args = tool_info.get("args", {})

        # 2. Если нужен инструмент → вызываем MCP
        if tool_name:
            tool_result = await self._run_tool_via_mcp(tool_name, args)

            try:
                safe_result = json.dumps(tool_result, ensure_ascii=False)
            except TypeError:
                safe_result = str(tool_result)

            final_answer = await self.llm.chat([
                {"role": "system", "content": "Ты помощник. Преобразуй результат инструмента в понятный ответ."},
                {"role": "assistant", "content": f"Результат инструмента {tool_name}: {safe_result}"},
                {"role": "user", "content": query}
            ])
            return final_answer

        # 3. Если инструмент не нужен → прямой ответ LLM
        return await self.llm.chat([
            {"role": "system", "content": "Ты полезный ассистент."},
            {"role": "user", "content": query}
        ])
