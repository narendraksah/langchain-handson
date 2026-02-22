from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from tavily import TavilyClient

load_dotenv()

tavily = TavilyClient()


@tool
def search(query: str) -> str:
    """
    Tool that searches over internet

    Args:
        query: The query to search for
    Returns:
        The search result
    """
    print(f"Searching for {query}")
    return tavily.search(query=query)


llm = ChatGoogleGenerativeAI(temperature=0.0, model="gemini-2.5-flash-lite")
tools = [search]
agent = create_agent(model=llm, tools=tools)


def main():
    print("Hello from langchain-handson: react-search-agent!")
    result = agent.invoke(
        {"messages": HumanMessage(content="What is the weather in Tokyo?")}
    )
    print(result)


if __name__ == "__main__":
    main()
