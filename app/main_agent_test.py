# main_agent_test.py
import asyncio
from llm.agent import LLMAgent

async def main():
    agent = LLMAgent()

    print("\n=== USER QUERY ===")
    query = input("Например(Найди вакансии python разработчика в Москве):")
    print(query)

    answer = await agent.ask(query)

    print("\n=== AGENT ANSWER ===")
    print(answer)


if __name__ == "__main__":
    asyncio.run(main())
