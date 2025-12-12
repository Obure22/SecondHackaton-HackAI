"""
app/tools/__init__.py

This file is for registering tool classes from app/tools/ with the MCP server.

How to use:
- Import your tool classes here.
- Register each tool using the @mcp.tool() decorator inside the register_tools function.
- See the example template below for guidance.

To add a new tool class:
1. Create your tool class in app/tools/ (e.g., my_tool.py).
2. Import your tool class here.
3. Register it in the register_tools function.

For simple tools, you can also define and register them directly in app/tools.py.
"""

from app.tools.search_vacancies import search_vacancies
from app.tools.search_vacancies_advanced import search_vacancies_advanced
from app.tools.get_vacancy_details import get_vacancy_details

def register_tools(mcp):

    # Регистрируем импортированные функции как tools
    mcp.tool()(search_vacancies)
    mcp.tool()(search_vacancies_advanced)
    mcp.tool()(get_vacancy_details)