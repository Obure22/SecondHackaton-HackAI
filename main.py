import logging
from app.server import mcp
from app.tools import register_tools

from dotenv import load_dotenv
load_dotenv()
def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
    )

async def startup():
    # Вызов регистрации инструментов
    await register_tools(mcp)

def main():
    setup_logging()
    logging.info("Starting MCP server...")
    mcp.run(
        transport="streamable-http"
    )

if __name__ == "__main__":
    main()
